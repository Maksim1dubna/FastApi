#Для запуска python -m uvicorn main1Fastapi:app
# Swagger /docs
from fastapi import FastAPI, Path
app = FastAPI()
@app.get("/")
async def main_page():
    return "Главная страница"

@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user_page(user_id: int = Path(ge = 1, le = 100, description = "Enter User ID", example= "93")):
    return f"Вы вошли как пользователь № {user_id}"
#http://127.0.0.1:8000/user/100

@app.get("/user/{username}/{age}")
async def user_age_page(username: str = Path(min_length = 5, max_length = 20, description="Enter username", example = "UrbanUser"),
                        age: int = Path(ge = 18, le = 120, description="Enter age", example = "24")):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

    # http://127.0.0.1:8000/user/UrbanUser/24
    #http://127.0.0.1:8000/user?username=user&age=25 для другой вариации
