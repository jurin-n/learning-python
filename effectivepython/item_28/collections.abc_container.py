# -*- coding: utf-8 -*-
import logging

try:
    try:
        # ABCs live in "collections.abc" in Python >= 3.3
        from collections.abc import Sequence
    except ImportError:
        # fall back to import from "backports_abc"
        from backports_abc import Sequence #TODO:backports_abcにSequenceが内容だが調べきれてない。
    
    class BadType(Sequence):
        pass
    
    foo = BadType()
except:
    logging.exception('Expected')
else:
    assert False