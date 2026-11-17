from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "안녕하세요"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/info")
def info():
    return {"name": "연습 서버", "version": 1}


@app.get("/fruits")
def fruits():
    return ["사과", "바나나"]

@app.get("/languages")
def languages():
    return ["Python", "JavaScript"]

@app.get("/hello/{name}")
def hello(name):
    return {"message": name + "님, 안녕하세요"}


@app.get("/double/{number}")
def double(number: int):
    return {"result": number * 2}

@app.get("/length/{text}")
def length(text):
    return {"length": len(text)}

@app.get("/greet")
def greet(name: str = "민수"):
    return {"message": name + "님, 반갑습니다"}


@app.get("/repeat")
def repeat(word: str = "안녕", count: int = 1):
    return {"text": word * count}

@app.get("/add")
def add(left: int = 0, right: int = 0):
    return {"result": left + right}

@app.post("/echo")
def echo(data: dict):
    return data


@app.post("/welcome")
def welcome(data: dict):
    return {"message": data["name"] + "님, 환영합니다"}

@app.post("/count")
def count(data: dict):
    count = len(data["items"])
    response = {"count": count}
    return response
