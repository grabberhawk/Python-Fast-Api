from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
class Post(BaseModel):
    title : str
    content : str
    published : bool=True
    
class PostBase(BaseModel):
    title : str
    content : str
    published : bool=True

class PostCreate(Post):
    pass

class UserOut(BaseModel):
    id :int
    email : EmailStr
    created_at :datetime
    
    class Config:
        orm_mode=True
        
        
class Post(BaseModel):
    id:int
    title : str
    content : str
    published : bool
    created_at: datetime
    owner_id:int
    owner:UserOut
    class Config:
        orm_mode=True  
        
class UserCreate(BaseModel):
    email : EmailStr
    password: str
    created_at : datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    

        
class UserLogin(BaseModel):
    email : EmailStr
    password : str 
        
# scehema for token bcoz they have to be posted        
class Token(BaseModel):
    access_token : str
    token_type : str
            
class TokenData(BaseModel):
    id: Optional[str]=None           