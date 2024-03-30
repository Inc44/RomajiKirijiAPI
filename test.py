import requests
from test_data import japanese_text, romaji_expected_text, kiriji_expected_text

URL = "http://127.0.0.1:8000/translate/"
payload = {"japanese_text": japanese_text}
response = requests.post(URL, json=payload)
assert response.status_code == 200
data = response.json()
assert data["romaji_text"] == romaji_expected_text
assert data["kiriji_text"] == kiriji_expected_text
