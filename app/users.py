from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas, utils, oauth2
from app.db_connection import get_db

router = APIRouter(
    prefix="/api/v1",
    tags=["Users"]
)


@router.post('/register-user/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_users(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hashed_password(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Add the created_at field
    user_dict = new_user.__dict__
    user_dict['created_at'] = datetime.now()

    return user_dict


@router.get("/users/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f"User with id: {user_id} not found")
    return user


@router.get('/me/', response_model=schemas.UserOut)
def get_user_profile(current_user: models.User = Depends(oauth2.get_current_user),
                     db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == current_user.id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    return user
