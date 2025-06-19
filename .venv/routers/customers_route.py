from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database import get_db
import crud, schemas

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.post("/", response_model=schemas.CustomerRead)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, customer)

@router.get("/", response_model=list[schemas.CustomerRead])
def get_all_customers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_all_customers(db, skip, limit)

@router.get("/advanced", response_model=list[schemas.CustomerRead])
def get_customers_advanced(
    search: str = None,
    sort_by: str = "name",
    sort_order: str = "asc",
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    return crud.get_customers_advanced(db, search, sort_by, sort_order, skip, limit)

@router.get("/{customer_id}", response_model=schemas.CustomerRead)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = crud.get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.put("/{customer_id}", response_model=schemas.CustomerRead)
def update_customer(customer_id: int, updates: schemas.CustomerUpdate, db: Session = Depends(get_db)):
    customer = crud.update_customer(db, customer_id, updates)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.delete("/{customer_id}", response_model=schemas.CustomerRead)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = crud.delete_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

