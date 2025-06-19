from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


# -------------------- PLAY --------------------
class PlayBase(BaseModel):
    title: str
    description: Optional[str] = None


class PlayCreate(PlayBase):
    pass


class PlayUpdate(PlayBase):
    pass


class Play(PlayBase):
    id: int

    class Config:
        orm_mode = True


class PlayRead(PlayBase):
    id: int

    class Config:
        form_attributes = True


# -------------------- ACTOR --------------------
class ActorBase(BaseModel):
    name: str
    gender: str = Field(..., min_length=1, max_length=1)
    date_of_birth: int


class ActorCreate(ActorBase):
    pass


class ActorUpdate(BaseModel):
    name: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[int] = None


class ActorRead(ActorBase):
    id: int

    class Config:
        form_attributes = True


# -------------------- DIRECTOR --------------------
class DirectorBase(BaseModel):
    name: str
    date_of_birth: int
    citizenship: str


class DirectorCreate(DirectorBase):
    pass


class DirectorUpdate(BaseModel):
    name: Optional[str] = None
    date_of_birth: Optional[int] = None
    citizenship: Optional[str] = None


class DirectorRead(DirectorBase):
    id: int

    class Config:
        form_attributes = True


# -------------------- CUSTOMER --------------------
class CustomerBase(BaseModel):
    name: str
    telephone_no: str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    telephone_no: Optional[str] = None


class CustomerRead(CustomerBase):
    id: int

    class Config:
        form_attributes = True


# -------------------- SHOWTIME --------------------
class ShowTimeBase(BaseModel):
    date_and_time: datetime
    play_id: int


class ShowTimeCreate(ShowTimeBase):
    pass


class ShowTimeUpdate(BaseModel):
    date_and_time: Optional[datetime] = None
    play_id: Optional[int] = None


class ShowTimeRead(ShowTimeBase):
    play: Optional[PlayRead]

    class Config:
        form_attributes = True


# -------------------- TICKET --------------------
class TicketBase(BaseModel):
    ticket_no: str
    seat_row_no: int
    seat_no: int
    showtime_date: datetime
    showtime_play_id: int
    customer_id: int


class TicketCreate(TicketBase):
    pass


class TicketUpdate(BaseModel):
    ticket_no: Optional[str] = None
    seat_row_no: Optional[int] = None
    seat_no: Optional[int] = None
    showtime_date: Optional[datetime] = None
    showtime_play_id: Optional[int] = None
    customer_id: Optional[int] = None


class TicketRead(TicketBase):
    id: int
    customer: Optional[CustomerRead]
    showtime: Optional[ShowTimeRead]

    class Config:
        form_attributes = True

# -------------------- AUTHENTICATION --------------------
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    is_active: bool

class UserInDB(User):
    hashed_password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True