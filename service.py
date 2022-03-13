from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class CV(BaseModel):
    name: str
    age: int
    dev:bool
    hobby:Optional[list]
        
class EMPLOYEE(BaseModel):
    name:str
    exp:int
    yop:int
    age:int
    employed:bool

@app.get("/hello/{my_query}")
def read_root(my_query,q:Optional[str]=None):
    return {"Hello": "World","user_input":my_query,"query":q}

@app.put("/endpoint2")
async def endpoint( resume: CV):
    "some code db here"
    return {"username": resume.name}

@app.post("/mypostendpoint")
async def mpep(emp:EMPLOYEE):
    return{"empname":emp.name}

@app.get("/mysecureendpoint")
async def msep(token:str):
    authtoken = "d2VkZGV2"
    if token!="" or token==authtoken:
        authorisation = "success welcome home"
    else:
        authorisation = "go back"
    return{"serverpass":authorisation}
       
