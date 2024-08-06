#Для запуска python -m uvicorn main4FastapiJinja2:app
# Swagger /docs
from fastapi import FastAPI, Path, Body, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
templates = Jinja2Templates(directory="templates")
app = FastAPI()
users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get("/")
async def getf(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {request: "request", "user": users})

@app.post("/user/{username}/{age}")
async def postf(user: User) -> str:
    User.id = len(users)
    users.append(user)
    return f"{user}"

@app.put("/user/{user_id}/{username}/{age}")
async def putf(user_id: int, username: str, age: int) -> str:
    try:
        edit_user = users[user_id]
        edit_user.username = username
        edit_user.age = age
        return f"{users[user_id]}"
    except IndexError:
        raise HTTPException(status_code = 404, detail= "Message not found")

@app.delete("/user/{user_id}")
async def deletef(user_id: int) -> List[User]:
    try:
        users.pop(user_id)
        return f"Удалено"
    except IndexError:
        raise HTTPException(status_code = 404, detail= "Message not found")