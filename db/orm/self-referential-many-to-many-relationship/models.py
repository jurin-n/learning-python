# -*- coding: utf-8 -*-
from sqlalchemy import Integer, ForeignKey, String, Column, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

item_item = Table("item_item", Base.metadata,
    Column("parent_item_id", String(64), ForeignKey("items.item_id"), primary_key=True),
    Column("child_item_id", String(64), ForeignKey("items.item_id"), primary_key=True)
)

class Item(Base):
    __tablename__ = 'items'
    item_id = Column(String(64), primary_key=True)
    name = Column(String(255))
    type = Column(String(10))
    items = relationship("Item",
        secondary=item_item,
        primaryjoin=(item_id==item_item.c.parent_item_id),
        secondaryjoin=(item_id==item_item.c.child_item_id),
        backref="parent_item"
    )

    def to_dict(self):
        return {
            'item_id': self.item_id,
            'name': self.name,
            'type': self.type,
            'items': [i.to_dict() for i in self.items]
            }