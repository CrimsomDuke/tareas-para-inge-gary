

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = FastAPI()

#cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("templates", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

counter = 1

todos = [
    {
        "id" : counter,
        "title" : "Hola comprar 3 pesos de dinero",
        "finished" : False
    }
]

@app.get("/")
async def root(request: Request):
    context = {
        "items" : todos
    }
    return context

@app.post("/")
async def create_item(request: Request, title : str = Form(...)):
    global counter
    counter += 1
    new_item = {
        "id" : counter,
        "title" : title,
        "finished" : False
    }
    todos.append(new_item)
    return new_item

@app.put("/{id}")
async def edit_item(request: Request, id : int):
    for item in todos:
        if item["id"] == id:
            item["finished"] = True
            return item
    return {"error" : "Item not found"}

@app.delete("/{id}")
async def delete_item(request : Request, id : int):
    for index, item in enumerate(todos):
        if item["id"] == id:
            todos.pop(index)
            return {"message" : "Item deleted"}
    return {"error" : "Item not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)




