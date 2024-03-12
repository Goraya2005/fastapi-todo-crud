
from typing import Union

from fastapi import FastAPI
import uvicorn



app = FastAPI()


@app.get("/", tags = ["HOME"])
def home():
    return {"data": {
        "name": "Goraya",
        "Institution" : "PIAIC",
        "Quarter" : 3
        }}

@app.get("/blog/{blog_id}", tags = ['BLOGS'])
def blog(blog_id):
    return {"data": blog_id}

@app.get("/blog/{blog_id}/comments")
def comments(blog_id):
    return {'data' : {
        'Comments1' : 'Welcome', 
        'Comments2' : 'Wellldone'}}







@app.get("/about", tags = ['ABOUT'])
def about():
    return {"date": {
        "University": "University of Agriculture, Faisalabad"
    }}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}





@app.get("/todo", tags = ['todos'])
async def get_todo()-> dict:
    return {"data" : todos}


@app.post("/todo", tags = ['todos'])
async def add_todo(todo : dict):
    todos.append(todo)
    return {"data" : "A New todo has successfully added in the list"}





@app.put("/todo{id}", tags = ['todos'])
async def update_todo(id : int, body : dict)-> dict:
    for todo in todos:
        if (todo['id']) == id:
            todo['activity'] = body['activity'];
            return { "data" : f"The id No. {id} is updated successfully"}

    return {"data" : f"The id No. {id} is not available in list"}




@app.delete("/todo", tags = ['todos'])
async def delete_todo(id : int)->dict:
    for todo in todos:
        if todo['id'] == id :
            todos.remove(todo)
            return { "data" : "Th todo id No. {id} is deleted from lis"}
    return { "data" : "The requested id No. {id} is not found in list"}









todos = [
    {
        "id": 1,
        "activity" : "Learn FastAPI"
    },
    {
        "id": 2,
        "activity" : "Learn CRUD in FastAPI"
    },
    
]






# if __name__ == "__main__":
#     uvicorn.run("main:app", port=8000, reload=True) 