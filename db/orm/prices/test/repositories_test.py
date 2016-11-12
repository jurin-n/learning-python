# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
from unittest import TestCase, main
from repositories import Repository
from domains import Base, AccountingPattern, Price
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session

class RepositoryTestCase(TestCase):
    
    def setUp(self):
        engine = create_engine('sqlite:///repositories_test.db')
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        self.session = Session(engine)
    
    def test_add(self):
        pattern = AccountingPattern(pattern_id='ID001', name=u'テスト　太郎')
        self.session.add_all([pattern])
        self.session.add_all([Price(price_id='P001', name=u'プライス１', accounting_pattern=pattern)])

        # sut = Repository()
        # sut.addAccountingPatterns()
        self.session.commit()

    def tearDown(self):
        self.sut = None

if __name__ == '__main__':
    main()
