from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


users_db = []
current_id = 1


class User(BaseModel):
    id: int = None
    name: str
    email: str

# Получить всех пользователей
@app.get("/users")
def get_all_users():
    return users_db

# Получить пользователя по ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    return {"error": "User not found"}

# Добавить пользователя
@app.post("/users")
def create_user(user: User):
    global current_id
    user.id = current_id
    current_id += 1
    users_db.append(user)
    return user

# Обновить пользователя
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            updated_user.id = user_id
            users_db[i] = updated_user
            return updated_user
    return {"error": "User not found"}

# Удалить пользователя
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            users_db.pop(i)
            return {"message": "User deleted"}
    return {"error": "User not found"}
