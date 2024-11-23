from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

# запуск - python -m uvicorn module_16_3:app
info_ed = ('Домашнее задание по теме "CRUD Запросы: Get, Post, Put Delete.".<br>'
           'Цель: выработать навык работы с CRUD запросами.<br>'
           'Задача "Имитация работы с БД":<br>'
           'Студент Крылов Эдуард Васильевич<br>'
           'Дата: 23.11.2024г.')


# Вместо главной страници
# http://127.0.0.1:8000/
@app.get("/", response_class=HTMLResponse)
async def welcome():
    return info_ed


# Информация о пользователях
@app.get("/users")
async def get_users() -> dict:
    return users


# Добавляет пользователя в базу данных
@app.post("/user/{username}/{age}")
async def old_users(username: Annotated[str, Path(min_length=2, max_length=20,
                                                  description="Введите Ваше имя", example="Edison")],
                    age: Annotated[int, Path(ge=18, le=120, description="Введите ваш возраст", example="25")]) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    add_user = f'Имя: {username}, возраст: {age}'
    users[current_index] = add_user
    return f'Данные пользователя №: {current_index}, Имя: {username}, Возраст: {age} зарегестрированы.'


# Изменение данных пользователя
@app.put("/user/{user_id}/{username}/{age}")
async def put_user(user_id: int, username: Annotated[str, Path(min_length=2, max_length=20,
                                                               description="Введите Ваше имя", example="Edison")],
                   age: Annotated[int, Path(ge=18, le=120, description="Введите ваш возраст", example="25")]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'Данные пользователя № {user_id} обновены.'


# Удаление пользователя по id
@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f'Данные пользователя № {user_id} удалены.'
