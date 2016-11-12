# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, String, ForeignKey)
from sqlalchemy.orm import relationship
Base = declarative_base()

class AccountingPattern(Base):
    
    __tablename__ = 'accounting_patterns'

    pattern_id = Column(String(10), primary_key=True)
    name = Column(String(100))
    
    _price = relationship("Price")
    
    def __init__(self , **kwargs):
        self.pattern_id = kwargs.pop('pattern_id', '')
        self.name = kwargs.pop('name', '')
        self.accounting_elements = kwargs.pop('accounting_elements', None)
        if kwargs:
             raise TypeError('Unexpected **kwargs: %r' % kwargs)


class Price(Base):
    __tablename__ = 'prices'

    price_id = Column(String(255), primary_key=True)
    name = Column(String(100))
    pattern_id = Column(String(10), ForeignKey('accounting_patterns.pattern_id'))
    
    def __init__(self , **kwargs):
        self.price_id = kwargs.pop('price_id', '')
        self.name = kwargs.pop('name', '')
        self.accounting_pattern = kwargs.pop('accounting_pattern', None)
        self.pattern_id = self.accounting_pattern.pattern_id
        if kwargs:
             raise TypeError('Unexpected **kwargs: %r' % kwargs)


'''
class AccountingElement():
    
    __tablename__ = 'accounting_elements'
    
    element_id = Column(String(255), primary_key=True)
    name = Column(String(100))
    
    def __init__(self , **kwargs):
        self.element_id = kwargs.pop('element_id', '')
        self.name = kwargs.pop('name', '')
        if kwargs:
             raise TypeError('Unexpected **kwargs: %r' % kwargs)


class AccountingPatternElement():
    __tablename__ = 'accounting_pattern_elements'
    
    pattern_id = Column(String(255), ForeignKey('accounting_patterns.pattern_id'), primary_key=True)
    element_id = Column(String(255), ForeignKey('accounting_elements.element_id'), primary_key=True)


class ConfiguredPrice():
    
    __tablename__ = 'configured_prices'

    configured_id = Column(String(255), primary_key=True)
    name = Column(String(100))
    price_id = Column(String(255), ForeignKey('prices.price_id'))
   
    def __init__(self , **kwargs):
        self.configured_price_id = kwargs.pop('configured_price_id', '')
        self.name = kwargs.pop('name', '')
        self.accounting_element_value = kwargs.pop('accounting_element_value', None)
        if kwargs:
            raise TypeError('Unexpected **kwargs: %r' % kwargs)


class AccountingElementValue():
    
    __tablename__ = 'accounting_element_values'
    
    value_id = Column(String(255), primary_key=True)
    element_id = Column(String(255))
    value = Column(String(100))
    configured_id = Column(String(255), ForeignKey('configured_prices.configured_id'))

    def __init__(self , **kwargs):
        self.element_id = element_id
        self.value = value
        if kwargs:
            raise TypeError('Unexpected **kwargs: %r' % kwargs)
'''
