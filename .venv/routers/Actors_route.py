from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database import get_db
import crud, schemas

router = APIRouter(prefix="/actors", tags=["Actors"])

@router.post("/", response_model=schemas.ActorRead)
def create_actor(actor: schemas.ActorCreate, db: Session = Depends(get_db)):
    return crud.create_actor(db, actor)

@router.get("/", response_model=list[schemas.ActorRead])
def get_all_actors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_all_actors(db, skip, limit)

@router.get("/advanced", response_model=list[schemas.ActorRead])
def get_actors_advanced(
    search: str = None,
    sort_by: str = "name",
    sort_order: str = "asc",
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    return crud.get_actors_advanced(db, search, sort_by, sort_order, skip, limit)

@router.get("/{actor_id}", response_model=schemas.ActorRead)
def get_actor(actor_id: int, db: Session = Depends(get_db)):
    actor = crud.get_actor(db, actor_id)
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor

@router.put("/{actor_id}", response_model=schemas.ActorRead)
def update_actor(actor_id: int, updates: schemas.ActorUpdate, db: Session = Depends(get_db)):
    actor = crud.update_actor(db, actor_id, updates)
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor

@router.delete("/{actor_id}", response_model=schemas.ActorRead)
def delete_actor(actor_id: int, db: Session = Depends(get_db)):
    actor = crud.delete_actor(db, actor_id)
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor

