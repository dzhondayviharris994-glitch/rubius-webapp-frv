from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, FastAPI!"}

@app.get("/about")
def about():
    return {"author": "Сергей Рогожкин"}


@app.get("/tasks")
def get_tasks():
    return {"tasks": "BLUBLUBLU"}


@app.post("/tasks")
def post_tasks():
    return {"ULBULBULB"}


@app.delete("/tasks/{id}")
def delete_tasks():
    return {"..."}
