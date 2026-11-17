from fastapi import FastAPI



# GET /profile	{"name":"민수","interest":"파이썬"}을 돌려준다.
# GET /hello/{name}	이름 뒤에 님, 안녕하세요를 붙인 message를 돌려준다.
# GET /repeat	word와 정수 count를 쿼리로 받는다. 기본값은 안녕, 1이다. 반복한 text를 돌려준다.
# POST /introduce	본문의 name, interest로 이름님은 관심사에 관심이 있습니다라는 message를 돌려준다.

app = FastAPI()

@app.get("/profile")
def profile():
    return {"name":"민수","interest":"파이썬"}


@app.get("/hello/{name}")
def hello(name):
    result = name + "님, 안녕하세요!"
    return {"message": result}


@app.get("/repeat")
def repeat(word: str = "안녕", count: int = 1):
    result = word * count
    return {"message": result} 

@app.post("/introduce")
def introduce(data: dict):
    result = data["name"] + "님은 " + data["interest"] + "에 관심이 있습니다"
    return {"message": result}

@app.get("/length/{text}")
def introduce(text):
    result = len(text)
    return {"count": result}    