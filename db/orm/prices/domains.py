# -*- coding: utf-8 -*-

class Price():
    def __init__(self , **kwargs):
        self.price_id = kwargs.pop('price_id', '')
        self.name = kwargs.pop('name', '')
        self.accounting_pattern = kwargs.pop('accounting_pattern', None)
        if kwargs:
             raise TypeError('Unexpected **kwargs: %r' % kwargs)

class AccountingPattern():
    def __init__(self , **kwargs):
        self.pattern_id = kwargs.pop('pattern_id', '')
        self.name = kwargs.pop('name', '')
        self.accounting_elements = kwargs.pop('accounting_elements', None)
        if kwargs:
             raise TypeError('Unexpected **kwargs: %r' % kwargs)

class AccountingElement():
    def __init__(self , **kwargs):
        self.element_id = kwargs.pop('element_id', '')
        self.name = kwargs.pop('name', '')
        if kwargs:
             raise TypeError('Unexpected **kwargs: %r' % kwargs)

class ConfiguredPrice():
    def __init__(self , **kwargs):
        self.configured_price_id = kwargs.pop('configured_price_id', '')
        self.name = kwargs.pop('name', '')
        self.accounting_element_value = kwargs.pop('accounting_element_value', None)
        if kwargs:
            raise TypeError('Unexpected **kwargs: %r' % kwargs)

class AccountingElementValue():
    def __init__(self , **kwargs):
        self.element_id = element_id
        self.value = value
        if kwargs:
            raise TypeError('Unexpected **kwargs: %r' % kwargs)