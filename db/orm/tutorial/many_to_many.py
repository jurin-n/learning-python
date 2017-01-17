# -*- coding: utf-8 -*-
"""basic_association.py

illustrate a many-to-many relationship between an
"Service" and a collection of "Item" objects, associating a purchase price
with each via an association object called "ServiceItem"

The association object pattern is a form of many-to-many which
associates additional data with each association between parent/child.

The example illustrates an "service", referencing a collection
of "items", with a particular price paid associated with each "item".

"""

from datetime import datetime

from sqlalchemy import (create_engine, MetaData, Table, Column, Integer,
    String, DateTime, Float, ForeignKey, and_)
from sqlalchemy.orm import mapper, relationship, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Service(Base):
    __tablename__ = 'service'

    service_id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    service_date = Column(DateTime, nullable=False, default=datetime.now())
    items = relationship("ServiceItem", cascade="all, delete-orphan",
                            backref='service')

    def __init__(self, name):
        self.name = name

class Item(Base):
    __tablename__ = 'item'
    item_id = Column(Integer, primary_key=True)
    description = Column(String(30), nullable=False)
    price = Column(Float, nullable=False)

    def __init__(self, description, price):
        self.description = description
        self.price = price

    def __repr__(self):
        return 'Item(%r, %r)' % (
                    self.description, self.price
                )

class ServiceItem(Base):
    __tablename__ = 'service_item'
    service_id = Column(Integer, ForeignKey('service.service_id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('item.item_id'), primary_key=True)
    price = Column(Float, nullable=False)

    def __init__(self, item, price=None):
        self.item = item
        self.price = price or item.price
    item = relationship(Item, lazy='joined')

if __name__ == '__main__':
    engine = create_engine('sqlite:///many_to_many.db')
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = Session(engine)

    # create catalog
    item1, item2, item3, item4 = (
        Item('SA T-Shirt', 10.99),
        Item('SA Mug', 6.50),
        Item('SA Hat', 8.99),
        Item('MySQL Crowbar', 16.99)
    )
    session.add_all([item1, item2, item3, item4])
    session.commit()

    # create an service
    service = Service('Service No1')

    # add three ServiceItem associations to the Service and save
    service.items.append(ServiceItem(item1))
    service.items.append(ServiceItem(item2, 10.99))
    service.items.append(ServiceItem(item3))
    session.add(service)
    session.commit()

    # create an service
    service2 = Service('Service No2')

    # add three ServiceItem associations to the Service and save
    service2.items.append(ServiceItem(item1))
    service2.items.append(ServiceItem(item2))
    service2.items.append(ServiceItem(item4))
    session.add(service2)
    session.commit()

    # query the service, print items
    service = session.query(Service).filter_by(name='Service No1').one()
    print([(service_item.item.description, service_item.price)
           for service_item in service.items])

    # print customers who bought 'MySQL Crowbar' on sale
    q = session.query(Service).join('items', 'item')
    q = q.filter(and_(Item.description == 'MySQL Crowbar'))

    print([service.name for service in q])