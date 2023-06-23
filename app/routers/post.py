from .. import models,schemas,utils,oauth2
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List
from typing import Optional
router =APIRouter(
    prefix='/posts',
    tags=['Posts']
    )

@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.Post )
def create_posts(post:schemas.PostCreate,db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    # print(new_post)
    # print(new_post.dict())  //to print in console 
    # post_dict =new_post.dict()
    # post_dict['id'] =randrange(0,1000000)
    # my_posts.append(post_dict)
    # new_post=models.Post(title=post.title,content=post.content,published=post.published)    <<<<<<<<<<----------IMPORTANT------------->>>>>>>>>>>>
    # print(**post.dict())
    # print(current_user.id)
    new_post=models.Post(
         owner_id=current_user.id,
        **post.dict()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post) #to retrieve the post just created!
    return new_post
#return {"new_post" : new_post} can be used

@router.get("/",response_model=List[schemas.Post])        # error as we are retriving a list of posts thats why we need to import list from typing
def get_posts(db: Session = Depends(get_db),
              current_user:int=Depends(oauth2.get_current_user),limit:int=10,search:Optional[str]=""):
    # cursor.execute("""SELECT * FROM "posts" """)
    # posts=cursor.fetchall()
    # print(posts)
    # if q=="" :
        # posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).all()
    #     return posts
    # elif q=="post":
        posts=db.query(models.Post).filter(models.Post.owner_id==current_user.id).all()
        return posts
# @router.get("/post",response_model=List[schemas.Post])        # error as we are retriving a list of posts thats why we need to import list from typing
# def get_posts(db: Session = Depends(get_db),
#               current_user:int=Depends(oauth2.get_current_user),limit:int=10,search:Optional[str]=""):
#     # cursor.execute("""SELECT * FROM "posts" """)
#     # posts=cursor.fetchall()
#     # print(posts)
#     #posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).all()
#      posts=db.query(models.Post).filter(models.Post.owner_id==current_user.id).limit(limit).all()
#      return posts

@router.get('/{id}',response_model=schemas.Post)
def get_posts(id: int,db: Session = Depends(get_db), current_user:int=Depends(oauth2.get_current_user)):
    # print(type(id))
    # post =find_post(int(id))
    post=db.query(models.Post).filter(models.Post.id== id).first()
    if not post:
        # response.status_code=status.HTTP_400_BAD_REQUEST
        # return {'message': f'post with id: {id} not found'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"request unavailable! {id}")
    if post.owner_id != current_user.id:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Unauthorized to Perform the Requested Action')
    # print(post)
    # # return {"post_detail":f"request available! {id}"}
    return post

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int,db: Session = Depends(get_db),
                current_user:int=Depends(oauth2.get_current_user)):
    # index=find_index_post(id)
    
    # my_posts.pop(index)
    # 
   # return {"message":f'post with id: {id} deleted siccessfully'}
   post_query=db.query(models.Post).filter(models.Post.id==id)
   post=post_query.first()
   if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} doesnot exist')
   if post.owner_id != current_user.id:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Unauthorized to Perform the Requested Action')
   post_query.delete(synchronize_session=False)
   db.commit()
   
       
   return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put('/{id}',response_model=schemas.Post)
def update_post(id :int ,updated_post:schemas.PostCreate,db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    #  index=find_index_post(id)
    post_query=db.query(models.Post).filter(models.Post.id ==id)
    post =post_query.first()
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} doesnot exist')
    if post.owner_id != current_user.id:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Unauthorized to Perform the Requested Action')
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    return post_query.first()