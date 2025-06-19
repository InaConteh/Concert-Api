from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database import get_db
import crud, schemas

router = APIRouter(prefix="/directors", tags=["Directors"])

@router.post("/", response_model=schemas.DirectorRead)
def create_director(director: schemas.DirectorCreate, db: Session = Depends(get_db)):
    return crud.create_director(db, director)

@router.get("/", response_model=list[schemas.DirectorRead])
def get_all_directors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_all_directors(db, skip, limit)

@router.get("/advanced", response_model=list[schemas.DirectorRead])
def get_directors_advanced(
    search: str = None,
    sort_by: str = "name",
    sort_order: str = "asc",
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    return crud.get_directors_advanced(db, search, sort_by, sort_order, skip, limit)

@router.get("/{director_id}", response_model=schemas.DirectorRead)
def get_director(director_id: int, db: Session = Depends(get_db)):
    director = crud.get_director(db, director_id)
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    return director

@router.put("/{director_id}", response_model=schemas.DirectorRead)
def update_director(director_id: int, updates: schemas.DirectorUpdate, db: Session = Depends(get_db)):
    director = crud.update_director(db, director_id, updates)
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    return director

@router.delete("/{director_id}", response_model=schemas.DirectorRead)
def delete_director(director_id: int, db: Session = Depends(get_db)):
    director = crud.delete_director(db, director_id)
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    return director

