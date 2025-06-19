from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database import get_db
import crud, schemas

router = APIRouter(prefix="/showtimes", tags=["Showtimes"])

@router.post("/", response_model=schemas.ShowTimeRead)
def create_showtime(showtime: schemas.ShowTimeCreate, db: Session = Depends(get_db)):
    return crud.create_showtime(db, showtime)

@router.get("/", response_model=list[schemas.ShowTimeRead])
def get_all_showtimes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_all_showtimes(db, skip, limit)
