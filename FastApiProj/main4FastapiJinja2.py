#Для запуска python -m uvicorn main4FastapiJinja2:app
# Swagger /docs
from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class User(BaseModel):
    id: int
    username: str
    age: int

users = []

@app.get("/", response_class=HTMLResponse)
async def getf(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.post("/user/", response_model=User)
async def postf(user: User) -> User:
    user.id = len(users)
    users.append(user)
    return user

@app.put("/user/{user_id}", response_model=User)
async def putf(user_id: int, user: User) -> User:
    if user_id >= len(users):
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = user
    return user

@app.delete("/user/{user_id}", response_class=HTMLResponse)
async def deletef(user_id: int) -> str:
    if user_id >= len(users):
        raise HTTPException(status_code=404, detail="User not found")
    users.pop(user_id)
    return "User deleted successfully"