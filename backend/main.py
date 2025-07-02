from fastapi import FastAPI 
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware



db = {}
id = 0

class Note(BaseModel):
    title: str
    content: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Only allow requests from React dev server
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers (like Content-Type)
)


@app.post("/notes/")
async def create(note : Note):
    global id
    db[id] = note
    response = {"id" : id, **note.dict()}
    id += 1
    return response

@app.get("/notes/")
def return_all_notes():
    return db

@app.get("notes/{noteid}")
def return_specific_note(noteid):
    if noteid in db:
        response = {noteid : db[noteid]}
        return response
    else:
        return -1
        





    


