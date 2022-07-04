import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=True, nullable=False)

    favorites = relationship("Favorite", backref = "user")

   

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(30))
    skin_color = Column(String(15))
    eye_color = Column(String(15))
    birth_year = Column(String(10))
    gender = Column (String(15))
    homeworld = Column(String(20),ForeignKey('planet.id'))
    starships = Column(String(30),ForeignKey('starship.id'))

    planets = relationship("Planets")
    favorites = relationship("Favorite", backref = "user")
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    starship_id = Column(Integer, ForeignKey('starships.id'))

     
class Planets(Base):
    __tablename__ = 'planets'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(250))
    population = Column(String(250), )
    climate = Column(String(50))
    water = Column (String(40))

    people = relationship("People")
    favorites = relationship("Favorite", backref = "planets")
    user_id = Column(Integer, ForeignKey('user.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    starship_id = Column(Integer, ForeignKey('starships.id'))


class Starships(Base):
    __tablename__ = 'starships'

    id = Column(Integer, primary_key=True)
    name = Column (String(40))
    model = Column(String(40))
    manufacturer = Column(String(50))
    cost_in_credits = Column(Integer)
    lenght = Column(Integer)
    max_atmosphering_speed = Column (Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(40))
    hyperdrive_rating = Column(Integer)

    people = relationship("People")
    favorites = relationship("Favorite", backref = "starships")
    user_id = Column(Integer, ForeignKey('user.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))


class Favourites(Base) :
    __tablename__="favorite"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    starship_id = Column(Integer, ForeignKey('starships.id'))

   
    
    



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')