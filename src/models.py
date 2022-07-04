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
    password = Column(String(80), unique=False, nullable=False)
    favorites = relationship("Favorite", backref = "user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }


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
    homeworld = column(string(20),ForeignKey('planet.id'))
    starships = column(string(30),ForeignKey('starship.id'))

    children = relationship("planets")

     def serialize(self):
        return {     
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year":self.birth_year,
            "gender": self.gender,
            "homeworld": self.homeworld,
            "starships": self.starship
        }


class PeopleFav(Base):
    __tablename__ = 'peopleFav'

    id = Column(Integer, primary_key=True)


class Planets(Base):
    __tablename__ = 'planets'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(250))
    population = Column(String(250), )
    climate = Column(String(50))
    water = Column (String(40))

    parent = relationship("people")

    def serialize(self):
        return {     
            "name": self.name,
            "id": self.id,
            "diameter": self.diameter,
            "population": self.population,
            "climate": self.climate,
            "water": self.climate
        }

class PlanetFav(Base):
    __tablename__ = 'planetFav'

    id = Column(Integer, primary_key=True)



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

    parent = relationship("people")

    def serialize(self):
        return {     
            "name": self.name,
            "id": self.id,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "lenght": self.lenght,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "hyperdrive_rating": self.hyperdrive_rating,
        }



class StarshipFav(Base):
    __tablename__ = 'starshipFav'

    id = Column(Integer, primary_key=True)


class Favourites(Base) :
     __tablename__="favorite"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
   
    def serialize(self):
        people = People.get_by_id(self.people_id)
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id,
            "planet_id": self.planet_id,
        }
    



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')