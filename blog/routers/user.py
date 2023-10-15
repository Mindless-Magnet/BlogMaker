from fastapi import APIRouter, Depends, status, HTTPException, Response

from sqlalchemy.orm import Session

from typing import List

from .. import models, schemas

from ..database import get_db

from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['user']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def createuser(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def getuser(id:int, db: Session = Depends(get_db)):
    return user.getuser(id, db)