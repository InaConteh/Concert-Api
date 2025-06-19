from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import datetime

import models
import schemas
from auth_utils import hash_password


# -------------------- PLAY SERVICES --------------------
def create_play(db: Session, play_data: schemas.PlayCreate):
    play = models.Play(**play_data.model_dump())
    db.add(play)
    db.commit()
    db.refresh(play)
    return play

def get_all_plays(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Play).offset(skip).limit(limit).all()

def get_play(db: Session, play_id: int):
    return db.query(models.Play).get(play_id)

def update_play(db: Session, play_id: int, updates: schemas.PlayUpdate):
    play = db.query(models.Play).get(play_id)
    if not play:
        return None
    for field, value in updates.model_dump(exclude_unset=True).items():
        setattr(play, field, value)
    db.commit()
    db.refresh(play)
    return play

def delete_play(db: Session, play_id: int):
    play = db.query(models.Play).get(play_id)
    if play:
        db.delete(play)
        db.commit()
    return play

def get_plays_advanced(db: Session, search: Optional[str] = None, sort_by: str = "title", sort_order: str = "asc", skip: int = 0, limit: int = 10):
    query = db.query(models.Play)
    if search:
        query = query.filter(models.Play.title.ilike(f"%{search}%"))
    sort_column = getattr(models.Play, sort_by, None)
    if sort_column:
        query = query.order_by(sort_column.desc() if sort_order == "desc" else sort_column.asc())
    return query.offset(skip).limit(limit).all()

# -------------------- ACTOR SERVICES --------------------
def create_actor(db: Session, actor_data: schemas.ActorCreate):
    actor = models.Actor(**actor_data.model_dump())
    db.add(actor)
    db.commit()
    db.refresh(actor)
    return actor

def get_all_actors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Actor).offset(skip).limit(limit).all()

def get_actor(db: Session, actor_id: int):
    return db.query(models.Actor).get(actor_id)

def update_actor(db: Session, actor_id: int, updates: schemas.ActorUpdate):
    actor = db.query(models.Actor).get(actor_id)
    if not actor:
        return None
    for field, value in updates.model_dump(exclude_unset=True).items():
        setattr(actor, field, value)
    db.commit()
    db.refresh(actor)
    return actor

def delete_actor(db: Session, actor_id: int):
    actor = db.query(models.Actor).get(actor_id)
    if actor:
        db.delete(actor)
        db.commit()
    return actor

def get_actors_advanced(db: Session, search: Optional[str] = None, sort_by: str = "name", sort_order: str = "asc", skip: int = 0, limit: int = 10):
    query = db.query(models.Actor)
    if search:
        query = query.filter(models.Actor.name.ilike(f"%{search}%"))
    sort_column = getattr(models.Actor, sort_by, None)
    if sort_column:
        query = query.order_by(sort_column.desc() if sort_order == "desc" else sort_column.asc())
    return query.offset(skip).limit(limit).all()

# -------------------- DIRECTOR SERVICES --------------------
def create_director(db: Session, director_data: schemas.DirectorCreate):
    director = models.Director(**director_data.model_dump())
    db.add(director)
    db.commit()
    db.refresh(director)
    return director

def get_all_directors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Director).offset(skip).limit(limit).all()

def get_director(db: Session, director_id: int):
    return db.query(models.Director).get(director_id)

def update_director(db: Session, director_id: int, updates: schemas.DirectorUpdate):
    director = db.query(models.Director).get(director_id)
    if not director:
        return None
    for field, value in updates.model_dump(exclude_unset=True).items():
        setattr(director, field, value)
    db.commit()
    db.refresh(director)
    return director

def delete_director(db: Session, director_id: int):
    director = db.query(models.Director).get(director_id)
    if director:
        db.delete(director)
        db.commit()
    return director

def get_directors_advanced(db: Session, search: Optional[str] = None, sort_by: str = "name", sort_order: str = "asc", skip: int = 0, limit: int = 10):
    query = db.query(models.Director)
    if search:
        query = query.filter(models.Director.name.ilike(f"%{search}%"))
    sort_column = getattr(models.Director, sort_by, None)
    if sort_column:
        query = query.order_by(sort_column.desc() if sort_order == "desc" else sort_column.asc())
    return query.offset(skip).limit(limit).all()

# -------------------- CUSTOMER SERVICES --------------------
def create_customer(db: Session, customer_data: schemas.CustomerCreate):
    customer = models.Customer(**customer_data.model_dump())
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

def get_all_customers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Customer).offset(skip).limit(limit).all()

def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).get(customer_id)

def update_customer(db: Session, customer_id: int, updates: schemas.CustomerUpdate):
    customer = db.query(models.Customer).get(customer_id)
    if not customer:
        return None
    for field, value in updates.model_dump(exclude_unset=True).items():
        setattr(customer, field, value)
    db.commit()
    db.refresh(customer)
    return customer

def delete_customer(db: Session, customer_id: int):
    customer = db.query(models.Customer).get(customer_id)
    if customer:
        db.delete(customer)
        db.commit()
    return customer

def get_customers_advanced(db: Session, search: Optional[str] = None, sort_by: str = "name", sort_order: str = "asc", skip: int = 0, limit: int = 10):
    query = db.query(models.Customer)
    if search:
        query = query.filter(models.Customer.name.ilike(f"%{search}%"))
    sort_column = getattr(models.Customer, sort_by, None)
    if sort_column:
        query = query.order_by(sort_column.desc() if sort_order == "desc" else sort_column.asc())
    return query.offset(skip).limit(limit).all()

# -------------------- SHOWTIME SERVICES --------------------
def create_showtime(db: Session, showtime_data: schemas.ShowTimeCreate):
    showtime = models.ShowTime(**showtime_data.model_dump())
    db.add(showtime)
    db.commit()
    db.refresh(showtime)
    return showtime

def get_all_showtimes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ShowTime).offset(skip).limit(limit).all()

def get_showtime(db: Session, showtime_id: int):
    return db.query(models.ShowTime).get(showtime_id)

def update_showtime(db: Session, showtime_id: int, updates: schemas.ShowTimeUpdate):
    showtime = db.query(models.ShowTime).get(showtime_id)
    if not showtime:
        return None
    for field, value in updates.model_dump(exclude_unset=True).items():
        setattr(showtime, field, value)
    db.commit()
    db.refresh(showtime)
    return showtime

def delete_showtime(db: Session, showtime_id: int):
    showtime = db.query(models.ShowTime).get(showtime_id)
    if showtime:
        db.delete(showtime)
        db.commit()
    return showtime

def get_showtimes_advanced(db: Session, search: Optional[str] = None, sort_by: str = "date_and_time", sort_order: str = "asc", skip: int = 0, limit: int = 10):
    query = db.query(models.ShowTime)
    if search:
        query = query.filter(models.ShowTime.date_and_time.cast(str).ilike(f"%{search}%"))
    sort_column = getattr(models.ShowTime, sort_by, None)
    if sort_column:
        query = query.order_by(sort_column.desc() if sort_order == "desc" else sort_column.asc())
    return query.offset(skip).limit(limit).all()

# -------------------- TICKET SERVICES --------------------
def create_ticket(db: Session, ticket_data: schemas.TicketCreate):
    ticket = models.Ticket(**ticket_data.model_dump())
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket

def get_all_tickets(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Ticket).offset(skip).limit(limit).all()

def get_ticket(db: Session, ticket_id: int):
    return db.query(models.Ticket).get(ticket_id)

def update_ticket(db: Session, ticket_id: int, updates: schemas.TicketUpdate):
    ticket = db.query(models.Ticket).get(ticket_id)
    if not ticket:
        return None
    for field, value in updates.model_dump(exclude_unset=True).items():
        setattr(ticket, field, value)
    db.commit()
    db.refresh(ticket)
    return ticket

def delete_ticket(db: Session, ticket_id: int):
    ticket = db.query(models.Ticket).get(ticket_id)
    if ticket:
        db.delete(ticket)
        db.commit()
    return ticket

def get_tickets_advanced(db: Session, search: Optional[str] = None, sort_by: str = "ticket_no", sort_order: str = "asc", skip: int = 0, limit: int = 10):
    query = db.query(models.Ticket)
    if search:
        query = query.filter(models.Ticket.ticket_no.ilike(f"%{search}%"))
    sort_column = getattr(models.Ticket, sort_by, None)
    if sort_column:
        query = query.order_by(sort_column.desc() if sort_order == "desc" else sort_column.asc())
    return query.offset(skip).limit(limit).all()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
