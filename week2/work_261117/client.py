import requests



response = requests.post(
    "http://127.0.0.1:8000/count", 
    json={"items": ["a", "b", "c"]}
)
print(response.status_code)
print(response.json())