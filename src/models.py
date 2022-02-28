import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = __tablename__ = 'people'
    name = Column(String(250), nullable=False)
    homeworld = column(string(20),ForeignKey('planet.id'))
    starships = column(string(30),ForeignKey('starship.id'))
    children = relationship("planets")

class PeopleFav(Base):
    __tablename__ = 'peopleFav'

    id = Column(Integer, primary_key=True)


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(250))
    population = Column(String(250), )
    climate = Column(Integer, )
    water = Column (String(40))
    People_ID= Column(Integer, ForeignKey('people.id'))
    parent = relationship("people")

class PlanetFav(Base):
    __tablename__ = 'planetFav'

    id = Column(Integer, primary_key=True)



class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column (String(40))
    model = Column(String(40))

class StarshipFav(Base):
    __tablename__ = 'starshipFav'

    id = Column(Integer, primary_key=True)

class Vehicles(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    model = Column(String(40))

class VehicleFav (Base):
    __tablename__ = 'vehicleFav'

    id = Column(Integer, primary_key=True)




class Favourites(Base) :
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')