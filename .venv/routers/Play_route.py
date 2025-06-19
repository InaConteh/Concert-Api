from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database import get_db
from models import Play, Actor, Director, Customer, ShowTime, Ticket
import schemas
import crud  # <-- Add this line


router = APIRouter(prefix="/concert", tags=["Concert"])

@router.post("/plays/", response_model=schemas.Play)
def create_play(play: schemas.PlayCreate, db: Session = Depends(get_db)):
    return crud.create_play(db, play)

@router.get("/plays/", response_model=list[schemas.Play])
def get_all_plays(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_all_plays(db, skip, limit)

@router.get("/plays/advanced", response_model=list[schemas.Play])
def get_plays_advanced(
    search: str = None,
    sort_by: str = "title",
    sort_order: str = "asc",
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    return crud.get_plays_advanced(db, search, sort_by, sort_order, skip, limit)

@router.get("/plays/{play_id}", response_model=schemas.Play)
def get_play(play_id: int, db: Session = Depends(get_db)):
    play = crud.get_play(db, play_id)
    if not play:
        raise HTTPException(status_code=404, detail="Play not found")
    return play

@router.put("/plays/{play_id}", response_model=schemas.Play)
def update_play(play_id: int, updates: schemas.PlayUpdate, db: Session = Depends(get_db)):
    play = crud.update_play(db, play_id, updates)
    if not play:
        raise HTTPException(status_code=404, detail="Play not found")
    return play

@router.delete("/plays/{play_id}", response_model=schemas.Play)
def delete_play(play_id: int, db: Session = Depends(get_db)):
    play = crud.delete_play(db, play_id)
    if not play:
        raise HTTPException(status_code=404, detail="Play not found")
    return play


