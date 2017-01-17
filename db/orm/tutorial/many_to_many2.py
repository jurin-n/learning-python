# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import (create_engine, MetaData, Table, Column, Integer,
    String, DateTime, Float, ForeignKey, and_)
from sqlalchemy.orm import mapper, relationship, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

association_table = Table('parent_child', Base.metadata,
    Column('parent_id', Integer, ForeignKey('parent.id')),
    Column('child_id', Integer, ForeignKey('child.id'))
)

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(String(30), primary_key=True)
    name = Column(String(30))
    children = relationship("Child",
                    secondary=association_table,
                    backref="parents")
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Child(Base):
    __tablename__ = 'child'
    id = Column(String(30), primary_key=True)
    name = Column(String(30))
    
    def __init__(self, id, name):
        self.id = id
        self.name = name

if __name__ == '__main__':
    engine = create_engine('sqlite:///many_to_many2.db')
    Base.metadata.create_all(engine)

    session = Session(engine)
    
    c1, c2, c3, c4 = (
        Child('CHILD001','SA T-Shirt'),
        Child('CHILD002','SA Mug'),
        Child('CHILD003','SA Hat'),
        Child('CHILD004','MySQL Crowbar')
    )
    session.add_all([c1, c2, c3, c4])
    session.commit()
    
    p1 = Parent('PARENT001','john smith')
    p1.children.append(c1)
    p1.children.append(c2)
    p1.children.append(c3)
    session.add(p1)
    session.commit()

    session2 = Session(engine)
    p2 = Parent('PARENT002','bill smith')
    c1 = session2.query(Child).filter_by(id='CHILD001').one()
    c2 = session2.query(Child).filter_by(id='CHILD002').one()
    p2.children.append(c1)
    p2.children.append(c1)
    session2.add(p2)
    session2.commit()