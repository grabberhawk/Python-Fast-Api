#from typing import Optional,List
from fastapi import FastAPI,Response,status,HTTPException,Depends
# from typing import Union;
# from passlib.context import CryptContext
#Routers
from .routers import post,user,auth
from pydantic import BaseModel
# import psycopg2
# from psycopg2.extras import RealDictCursor
import time
from . import models,schemas,utils
from .database import engine, get_db
from sqlalchemy.orm import Session
# pwd_context = CryptContext(schemes=["bcrypt"])
models.Base.metadata.create_all(bind=engine)
app=FastAPI()
# while True:
#     try:
#         conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='password',cursor_factory=RealDictCursor)
#         cursor =conn.cursor()
#         print("DB connected!")
#         break
#     except Exception as error:
#         print("DB failed")   
#         print("Error: ",error)
#         time.sleep(2)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
@app.get("/") 
async def root():
    
    return {"message": "Welcome Home"}


    
 


