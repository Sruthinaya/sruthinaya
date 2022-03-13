from re import template
from urllib import response
from urllib.request import Request
from fastapi import FastAPI,requests

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from typing import Optional
from pydantic import BaseModel

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static",StaticFiles(directory="static"),name="static")
templates= Jinja2Templates(directory="templates")



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

@app.get("/webpage",response_class=HTMLResponse)
async def webpage():
    html_code ="""
                <html>
                <head>

                </head>
                <body>
                <h1>hellow folks</h1>
                </body>
                </html>
             """
    return html_code

@app.get ("/filehtml",response_class=HTMLResponse)
async def webpage(request=Request):
    return templates.TemplateResponse('index.html',context={'request': request})

       