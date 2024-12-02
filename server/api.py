from fastapi import FastAPI # type: ignore
todo = FastAPI()


@todo.get("/")
async def index():
    return {"message": "Hello World"}

@todo.get("/gettodo")
async def get_todo():
    pass


@todo.get("/updatetodo")
async def update_todo():
    pass


@todo.get("/createtodo")
async def create_todo():
    pass


@todo.get("/deletetodo")
async def delete_todo():
    pass
