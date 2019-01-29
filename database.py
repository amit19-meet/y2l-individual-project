from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///comments.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_comment(name, comment,type_dance):
    new_comment = Comments(name=name, comment=comment, type_dance=type_dance)
    session.add(new_comment)
    session.commit()

def get_all_comments(type_dance):
    comments = session.query(Comments).filter_by(type_dance=type_dance).all()
    return comments


def add_user(username, password):
	new_user = Users(username=username, password=password)
	session.add(new_user)
	session.commit()

def get_user_by_username(username):
	user= session.query(Users).filter_by(username=username).one()
	return user
