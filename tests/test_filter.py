from app.db import insert_image,query_image

def test_query_image():
    insert_image("test.jpg",{"type":"dress","color":"red"})
    results = query_image(type="dress")
    assert any(r["filename"] == "test.jpg" for r in results)