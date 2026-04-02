from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_end_to_end():
    with open("test/sample.jpg","rb") as f:
        client.post("/upload", files={"file": ("sample.jpg", f, "image/jpeg")})
        response = client.get("/search", params={"type":"dress"})
        assert response.status_code==200