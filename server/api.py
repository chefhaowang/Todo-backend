from pymongo import MongoClient
from fastapi import FastAPI 
from pydantic import BaseModel
todo = FastAPI()


client = MongoClient("mongodb://localhost:27017/")

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
    try:
        items = list(collection.find({}, {"_id": 0})) 
        return items
    
    except:
        return "getting unsuccessful"
    

@todo.post("/createtodo")
async def create_todo(todo_item: TodoItem):
    todo_item = {
        "id": todo_item.id,  
        "added_time": todo_item.added_time,
        "content": todo_item.content,
        "last_update_time": todo_item.last_update_time  
    }

    try:
        collection.insert_one(todo_item)
        return "Creation successful"
    except:
        return "Creation unsuccessful"
    


@todo.put("/updatetodo")
async def update_todo(item: TodoItem):
    filter = {"id": item.id}
    update = {
        "$set": {
            "content": item.content,
            "added_time": item.added_time,
            "last_update_time": item.last_update_time,
        }
    }
    try:
        collection.update_one(filter, update)
        return "update successful"
    except:
        return "update unsuccessfull"


@todo.delete("/deletetodo")
async def delete_todo(item: TodoItem):
    delete_filter = {"id": item.id}
    try:
        collection.delete_one(delete_filter)
        return "deletion successful"
    except:
        return "deletion unsuccessful"

