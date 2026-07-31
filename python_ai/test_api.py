import requests

data = {
    "temperature": 120,
    "pressure": 160,
    "vibration": 9
}

response = requests.post(
    "http://127.0.0.1:5000/analyze",
    json=data
)

print(response.json())