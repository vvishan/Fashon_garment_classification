from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from datetime import datetime
from .model import classify_image
from .db import init_db, insert_image, search_image,update_annotation
from .utils import parse_caption
import shutil
import os


app = FastAPI(title="Fashion AI Web App")
init_db()

@app.get("/")
def root():
    return {"message":"fashion AI API is running"}

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    upload_dir = "uploads"
    os.makedirs(upload_dir,exist_ok = True)
    file_path = os.path.join(upload_dir, file.filename)
    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    caption = classify_image(file_path)
    attrs = parse_caption(caption)
    insert_image(file.filename,caption, attrs)
    return JSONResponse({"filename":file.filename,"caption": caption,"attributes":attrs})

@app.get("/search")
def search(type: str=None, color: str=None, note: str = None):
    from app.db import search_image
    filter =[]
    if type:
        filter.append(f"type LIKE '%{type}%'")
    if color:
        filter.append(f"color LIKE '%{color}%'")
    if note:
        filter.append(f"annotation LIKE '%{note}%'")
    where_clause = "AND".join(filter) if filter else "1=1"
    results = search_image(where_clause)
    #results = query_image(type = type,color=color)
    return JSONResponse({"results": results})

@app.post("/annotate")
def annotate_image(filename: str = Form(...), note: str = Form(...)):
    try:
        update_annotation(filename,note)
        return{"message": f"Annotation added for {filename}","note": note}
    except Exception as e:
        return {"error": str(e)}


