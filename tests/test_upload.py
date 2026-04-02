from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_and_search():
    with open("test/sample.jpg","rb") as f:
        response = client.post("/upload", files={"file": ("sample.jpg", f,"image/jpeg")})
        assert response.status_code == 200
        data = response.json
        assert "filename" in data
        assert "attributes" in data
