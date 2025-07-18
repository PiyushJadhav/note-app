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

@app.get("/notes/{noteid}")
def return_specific_note(noteid: int):
    if noteid in db:
        response = {"id" : noteid,  **db[noteid].dict()}
        return response
    else:
        return {"error:", "Note not found"}, 404
    
# change the input to a note instead of title, content
@app.put("/notes/{noteid}")
def update_specific_note(noteid: int, note: Note):
    if noteid in db:
        # Update the note in the database
        db[noteid] = note
        response = {"id": noteid, **note.dict()}
        return response
    else:
        # Raise an HTTPException if the note is not found
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Note not found")  

@app.delete("/notes/{noteid}")
def delete_note(noteid: int):
    if noteid in db:
        del db[noteid]
        response = {f"{noteid}" : "deleted successfuly"}
        return response
    else:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Note doesn't exist")





    


