from fastapi import FastAPI 
from pydantic import BaseModel


db = {}
id = 0

class Note(BaseModel):
    title: str
    content: str

app = FastAPI()


@app.post("/notes/")
async def create(note : Note):
    global id
    db[id] = note
    id += 1
    response = {"id" : id, **note.dict()}
    return response


    


