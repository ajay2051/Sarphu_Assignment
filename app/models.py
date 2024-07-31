from sqlalchemy import Column, Integer, String

from .db_connection import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    location = Column(String)
    about_me = Column(String)

    class Config:
        orm_mode = True


class Token(Base):
    __tablename__ = 'token'
    id = Column(Integer, primary_key=True)
    access_token = Column(String)
    refresh_token = Column(String)

    class Config:
        orm_mode = True
