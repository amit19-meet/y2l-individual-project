from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    comment = Column(String)
    type_dance = Column(String)


class Users(Base):
	__tablename__= "users"
	id= Column(Integer, primary_key= True)
	username = Column(String)
	password = Column(String)
