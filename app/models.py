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

    def __init__(self, name, email, password, location, about_me):
        self.name = name
        self.email = email
        self.password = password
        self.location = location
        self.about_me = about_me
