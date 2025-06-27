from fastapi import FastAPI 
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    email: str
    age: int

app = FastAPI()


# get is like get users info and then this would return it but not sens info
@app.get("/")
async def root():
    return {"message": "hi!"}

# post could be to create a new user 
@app.post("/info")
async def info(inf : Item):
    item_dic = inf.dict()
    if 'pj' in item_dic or 'pj' in item_dic.values():
        return {"message": "success!"}
    else:
        return {"message": "failure!"}

