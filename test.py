import requests

def test_frontend_backend_integration():
    frontend_url = "http://192.168.49.2:30145"
    response = requests.get(frontend_url)
    assert response.status_code == 200
    assert "Hello from the backend" in response.text
test_frontend_backend_integration()