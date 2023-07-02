import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}


favorite_characters = Table(
    "favorite_characters",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("character_id", ForeignKey("characters.id")),
)

favorite_planets = Table(
    "favorite_planets",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("planet_id", ForeignKey("planets.id")),
)
favorite_starships = Table(
    "favorite_starships",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("starship_id", ForeignKey("starships.id")),
)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)


    name = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)

    
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)

    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favorite_characters = relationship('Characters',secondary=favorite_characters)
    favorite_planets = relationship('Planets',secondary=favorite_planets)
    favorite_starships = relationship('Starships',secondary=favorite_starships)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)

    name = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)


class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)

    model = Column(String(250), nullable=False)
    starship_class = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')