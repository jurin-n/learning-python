# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'
    
    item_id = Column(String(64), primary_key=True)
    name = Column(String(255))
    type = Column(String(5))

    parent_id = Column(String(64), ForeignKey('items.item_id'))
    parent = relationship("Item", backref=('items'), remote_side=[item_id])

    def to_dict(self):
        return {
            'item_id': self.item_id,
            'name': self.name,
            'type': self.type,
            'items': [i.to_dict() for i in self.items]
            }