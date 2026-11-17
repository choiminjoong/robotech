from fastapi import FastAPI
from fastapi.responses import PlainTextResponse



app = FastAPI()

@app.get("/")
def home():
    return {"message": "안녕하세요"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/info")
def info():
    return {"name": "연습 서버", "version": "1"}


@app.get("/fruits", response_class=PlainTextResponse)
def fruits():
    fruits = ["사과", "바나나"]
    # 2개의 데이터가 있습니다: ["사과", "바나나"]

    # return "2개의 데이터가 있습니다: " + fruits  => Internal Server Error
    # return "2개의 데이터가 있습니다: " + str(fruits)
    return f"2개의 데이터가 있습니다: {fruits}"
    

@app.get("/hello/{name}")
def hello(name):
    return {"message": name + "님, 안녕하세요"}

# 약타입 언어 -> js, python
# 강타입 언어 -> c, java
@app.get("/double/{number}")
def double(number: int):
    return (number * 2)
