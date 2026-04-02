from app.model import classify_image

def evaluate(image_path, expected_keywords):
    with open("image_path", "rb") as f:
        caption = classify_image(f.read())
    print("Caption:",caption)
    for kw in expected_keywords:
        print(f"{kw}:{'success' if kw in caption.lower() else 'not sucess'}")