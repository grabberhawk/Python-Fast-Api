from fastapi import APIRouter,Depends,status, HTTPException,Response
from sqlalchemy.orm import Session
from .. import database, schemas,models,utils,oauth2
# using built-in utility form to retrieve user id and password 
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
router=APIRouter(tags=['Authentication'])

@router.post('/login', response_model=schemas.Token)
def login(#  trivial method: user_credentials: schemas.UserLogin, when email is retrived via this method this is saves as username not email // use username here //// in trivial method email is used ---- user_cre....email ->.username
          db: Session=Depends(database.get_db),
          user_credentials:OAuth2PasswordRequestForm=Depends()):
    user=db.query(models.User).filter(models.User.email== user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f'Invalid Credentials')
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f'Invalid Credentials')
    access_token=oauth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type":'bearer'}   
    
    