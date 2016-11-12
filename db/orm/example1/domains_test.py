# -*- coding: utf-8 -*-
from unittest import TestCase, main

from domains import Base, User
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session, sessionmaker

class UserTestCase(TestCase):
    
    def setUp(self):
        engine = create_engine('sqlite:///domains_test.db', echo=True)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        # self.session = Session(engine)
        Session = sessionmaker(bind=engine, autocommit=True)
        self.session = Session()
        
    def test_add(self):
        with self.session.begin():
            ed_user = User(name='taro', fullname=u'テスト　太郎', password='xxxx')
            self.session.add_all([ed_user])
            # self.session.commit()
 
    def test_query(self):
        with self.session.begin():
            user = User(name='taro', fullname=u'テスト　太郎', password='xxxx')
            self.session.add_all([user])
        got_user = self.session.query(User).filter_by(name='taro').first()
        # print our_user  #TODO:マルチバイト文字列が入ると __repr__で UnicodeEncodeError。このエラーが解決できてない。
        self.assertTrue(user is got_user) 
        self.assertEqual(1, user.id)


# class UserTestCase2(TestCase):
#     
#     def setUp(self):
#         engine = create_engine('sqlite:///domains_test.db', echo=True)
#         Base.metadata.drop_all(engine)
#         Base.metadata.create_all(engine)
#         self.session = Session(engine)
#         
#     def test_add(self):
#         ed_user = User(name='jiro', fullname=u'テスト　次郎', password='jirojiro')
#         self.session.add_all([ed_user])
#         self.session.commit()
            
if __name__ == '__main__':
    main()
