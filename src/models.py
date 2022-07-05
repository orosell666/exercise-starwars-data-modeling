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
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False)


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    image = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    date = Column(String(20))
    likes_id = Column(Integer, ForeignKey('person.id'))
    comments_id = Column(Integer, ForeignKey('comments.id'))
    inbox_id = Column(Integer, ForeignKey('inbox.id'))


class Notifications(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    date = Column(String(20))
    follower_id = Column(Integer, ForeignKey('follower.id'))
    follow_request = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))

class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    text = Column(String(300))
    likes_id =  Column(Integer, ForeignKey('likes.id'))

class Like(Base):
    __tablename__ = 'like'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id')) 


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    likes_id =  Column(Integer, ForeignKey('likes.id'))
    text = Column(String(300))
    image = Column(String(250))
    emojis = Column(String(25))
    gifs = Column(String(250))
    histories_id = Column(Integer, ForeignKey('histories.id')) 
    posts_id = Column(Integer, ForeignKey('post.id')) 
    
class Follower(Base):
    __tablename__ = 'followers'

    id = Column(Integer, primary_key=True)
    date = Column(String(20))
    user_id = Column(Integer, ForeignKey('user.id'))


    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e