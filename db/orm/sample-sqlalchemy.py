# -*- coding: utf-8 -*-

import sqlalchemy as sa
import zoo
from sqlalchemy.ext.declarative import declarative_base

conn = sa.create_engine('sqlite:///zoo.db')
Base = declarative_base()
Base.metadata.create_all(conn)

first = zoo.Zoo('duck', 10, 0.0)
second = zoo.Zoo('bear', 2, 1000.0)
third = zoo.Zoo('weasel', 1, 2000.0)

print first
print second
print third

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=conn)
session = Session()

session.add(first)
session.add_all([second, third])
session.commit()
#session.rollback()
