import sqlite3
import json

DB_PATH = "image.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.cursor()
    conn.execute("""
                 CREATE TABLE IF NOT EXISTS images (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 filename TEXT,
                 caption TEXT,
                 attributes TEXT,
                 annotation TEXT,
                 type TEXT,
                 color TEXT
                 )
                 """)
    conn.commit()
    conn.close()

def insert_image(filename, caption, attrs):
    conn = sqlite3.connect(DB_PATH)
    conn.cursor()
    conn.execute("INSERT INTO images (filename, caption, attributes, type, color) VALUES (?, ?, ?, ?, ?)",
                 (filename, caption, json.dumps(attrs), attrs.get("type","UNKNOWN"), attrs.get("color","UNKNOWN"))
                 )
    conn.commit()
    conn.close()
    # return {"filename": filename, "caption":caption,  **attrs}

def search_image(query):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c = conn.execute("SELECT filename, caption, attributes, annotation FROM images WHERE caption LIKE ?",(f"{query}%",))
    rows = c.fetchall()
    conn.close()
    return [{"filename": r[0], "caption": r[1], "attributes":json.loads(r[2]), "annotation":r[3]} for r in rows]

def update_annotation(filename, note):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE images SET annotation= ? WHERE filename = ?",(note,filename))
    conn.commit()
    conn.close()

def query_image(type= None,color= None):
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT filename, type, color FROM images WHERE 1=1"
    params = []

    if type:
        query += " AND type = ?"
        params.append(type)
    if color:
        query += " AND color= ?"
        params.append(color)
    cur = conn.execute(query, params)
    rows = cur.fetchall()
    conn.close()
    return [{"filename": r[0], "type": r[1],"color": r[2]} for r in rows]