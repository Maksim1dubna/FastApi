#Для запуска python -m uvicorn main2FastapiCrud:app
# Swagger /docs
from fastapi import FastAPI, Path
app = FastAPI()
users = {1: 'Имя: Example, возраст: 18'}

@app.get("/users")
async def getf() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def postf( username: str = Path(min_length = 5, max_length = 20, description="Enter username", example = "UrbanUser"),
               age: int = Path(ge = 18, le = 120, description="Enter age", example = "24")) -> str:
    cur_index = int(max(users, key=int)) + 1
    users[cur_index] = f"Имя: {username}, Возраст: {age}"
    return f"User {cur_index} is registered"
@app.put("/user/{user_id}/{username}/{age}")
async def putf(user_id: int = Path(ge = int(min(users, key=int)), le = int(max(users, key=int))),
               username: str = Path(min_length = 5, max_length = 20, description="Enter username", example = "UrbanUser"),
               age: int = Path(ge = 18, le = 120, description="Enter age", example = "24")) -> str:
    users[user_id] = f"Имя: {username}, Возраст: {age}"
    return f"The user {user_id} is registered"

@app.delete("/user/{user_id}")
async def deletef(user_id:int = Path(ge = int(min(users, key=int)), le = int(max(users, key=int)), description = "Enter User ID", example= "93")) -> str:
    users.pop(user_id)
    return f"The user {user_id} is deleted"

