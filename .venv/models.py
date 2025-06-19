from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, DECIMAL, Table
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

# Association Tables
actor_play = Table(
    'actor_play',
    Base.metadata,
    Column('actor_id', Integer, ForeignKey('actors.id'), primary_key=True),
    Column('play_id', Integer, ForeignKey('plays.id'), primary_key=True)
)

director_play = Table(
    'director_play',
    Base.metadata,
    Column('director_id', Integer, ForeignKey('directors.id'), primary_key=True),
    Column('play_id', Integer, ForeignKey('plays.id'), primary_key=True)
)


class Play(Base):
    __tablename__ = 'plays'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    duration = Column(Integer, nullable=False)
    genre = Column(String(20), nullable=False)
    synopsis = Column(String(200))

    actors = relationship('Actor', secondary=actor_play, back_populates='plays')
    directors = relationship('Director', secondary=director_play, back_populates='plays')
    showtimes = relationship('ShowTime', back_populates='play')


class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    gender = Column(String(1), nullable=False)
    date_of_birth = Column(Integer)

    plays = relationship('Play', secondary=actor_play, back_populates='actors')


class Director(Base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    date_of_birth = Column(Integer)
    citizenship = Column(String(100))

    plays = relationship('Play', secondary=director_play, back_populates='directors')


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    telephone_no = Column(String(100))

    tickets = relationship('Ticket', back_populates='customer')


class ShowTime(Base):
    __tablename__ = 'showtimes'

    date_and_time = Column(DateTime, primary_key=True, default=datetime.utcnow)
    play_id = Column(Integer, ForeignKey('plays.id'), primary_key=True)

    play = relationship('Play', back_populates='showtimes')
    tickets = relationship('Ticket', back_populates='showtime')


class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, index=True)
    ticket_no = Column(String(10), unique=True, nullable=False)
    seat_row_no = Column(Integer, nullable=False)
    seat_no = Column(Integer, nullable=False)

    showtime_date = Column(DateTime, nullable=False)
    showtime_play_id = Column(Integer, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)

    showtime = relationship('ShowTime', primaryjoin="""and_(
        Ticket.showtime_date==ShowTime.date_and_time,
        Ticket.showtime_play_id==ShowTime.play_id
    )""", back_populates='tickets')

    customer = relationship('Customer', back_populates='tickets')


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)  # <-- Add this line
    hashed_password = Column(String, nullable=False)
    # Add other fields as needed
