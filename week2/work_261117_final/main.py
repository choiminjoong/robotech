import requests



response = requests.post(
    "http://127.0.0.1:8000/introduce", 
    json={"name":"민수","interest":"파이썬"}
)
print(response.status_code)
print(response.json())

response = requests.post(
    "http://127.0.0.1:8000/introduce", 
    json={"name":"지수","interest":"그림"}
)
print(response.status_code)
print(response.json())