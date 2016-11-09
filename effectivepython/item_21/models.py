# -*- coding: utf-8 -*-

class User():
    def __init__(self, **kwargs):
        self.user_id = kwargs.pop('user_id', '')
        self.name = kwargs.pop('name', '')
        if kwargs:
             raise TypeError('Unexpected **kwargs: %r' % kwargs)