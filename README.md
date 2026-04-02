# Fashon_garment_classification
Inspiration Web  App
## Overview
A minimal FastAPI app that classifies fashion images using BLIP and stores searchable metadata.

## Run
1. Install dependencies:
   pip install -r requirements.txt
2. Start server:
   uvicorn app.main:app --reload
3. Open in browser:
   http://127.0.0.1:8000/docs

## Usage
- POST `/upload` with image file → returns attributes
- GET `/search?type=dress&color=red`

## Model
Uses BLIP for captioning. Simple parsing logic in `utils.py`.

## Limitations
- Parsing is naive
- No vector search
- Only two attributes

## Next Steps
- Improve parsing with regex or LLM
- Add more attributes
- Use vector similarity search
