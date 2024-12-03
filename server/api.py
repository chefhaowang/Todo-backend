from pymongo import MongoClient
from fastapi import FastAPI 
from pydantic import BaseModel
todo = FastAPI()


client = MongoClient("mongodb://localhost:27017/")

# Access the 'todo' database
db = client["todo"]
collection = db["todo"]

class TodoItem(BaseModel):
    id: str
    content: str
    added_time: str
    last_update_time: str


@todo.get("/")
async def index():
    return {"message": "Hello World"}

@todo.get("/gettodo")
async def get_todo():
    pass


@todo.get("/createtodo")
async def create_todo(todo_item: TodoItem):
    # Data to insert
    todo_item = {
        "id": 1,  # or generate a unique ID
        "added_time": "2024-12-03T10:00:00Z",  # ISO format for added time
        "content": "Buy groceries",
        "last_update_time": "2024-12-03T10:30:00Z"  # ISO format for last update time
    }

    # Insert the document into the 'todo' collection
    result = collection.insert_one(todo_item)


@todo.get("/updatetodo")
async def update_todo():
    pass


@todo.get("/deletetodo")
async def delete_todo():
    pass
