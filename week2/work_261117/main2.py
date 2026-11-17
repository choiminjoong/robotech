from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/status")
def status():
    return {"running": True}