# -*- coding: utf-8 -*-
from domains import User

def addUser(session=None, users=None):
    session.add_all(users) 

def getAllUser(session=None):
    return session.query(User).order_by(User.id)

def getUser(session=None, name=None):
    return session.query(User).filter_by(name=name).first()
