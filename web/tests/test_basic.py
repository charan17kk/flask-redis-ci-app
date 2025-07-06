import requests
import time

def test_flask_endpoint():
    time.sleep(2)  # give time for web to start
    response = requests.get("http://web:5004")
    assert response.status_code == 200
    assert "This page has been viewed" in response.text # or whatever string you return in your Flask route
