# -*- coding: utf-8 -*-
# from unittest import TestCase, main
import unittest
from domains import Base, User, Address
from repositories import addUser, getAllUser, getUser
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session, sessionmaker

class RepositoriesTestCase(unittest.TestCase):
    # [メモ]テスト単位でセットアップでもいいとおもったけど、テストケース単位での
    # [メモ]セットアップもそれほど遅くないのでテストケース単位にした。
    # @classmethod
    # def setUpClass(cls):
    #    engine = create_engine('sqlite:///repositories_test.db', echo=False)
    #    Base.metadata.drop_all(engine)
    #    Base.metadata.create_all(engine)
    #    # self.session = Session(engine)
    #    Session = sessionmaker(bind=engine, autocommit=True)
    #    session = Session()

    def setUp(self):
        engine = create_engine('sqlite:///repositories_test.db', echo=True)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        # self.session = Session(engine)
        Session = sessionmaker(bind=engine, autocommit=True)
        self.session = Session()

    # @unittest.skip("スキップ理由・・・")
    def test_add(self):
        with self.session.begin():
            user = User(name='taro', fullname=u'テスト　太郎', password='tarotaro')
            addUser(self.session, [user])
    
    def test_get_all_users(self):
        with self.session.begin():
            user1 = User(name='taro', fullname=u'テスト　太郎', password='tarotaro')
            user2 = User(name='jiro', fullname=u'テスト　次郎', password='jirojiro')
            user3 = User(name='sabu', fullname=u'テスト　三郎', password='sabusabu')
            addUser(self.session, [user1, user2, user3])
        users = getAllUser(self.session)
        self.assertEqual(3, users.count())
    
    def test_get_an_user(self):
        with self.session.begin():
            user1 = User(name='taro', fullname=u'テスト　太郎', password='tarotaro')
            user2 = User(name='jiro', fullname=u'テスト　次郎', password='jirojiro')
            user3 = User(name='sabu', fullname=u'テスト　三郎', password='sabusabu')
            addUser(self.session, [user1, user2, user3])
        user = getUser(self.session, name='jiro')
        self.assertEqual('jiro', user.name)

    def test_add_an_user_with_addresses(self):
        jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
        jack.addresses = [
                Address(email_address='jack@google.com'),
                Address(email_address='j25@yahoo.com')
                ]
        with self.session.begin():
            addUser(self.session, [jack])
            
    def test_get_an_user_with_addresses(self):
        jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
        jack.addresses = [
                Address(email_address='jack@google.com'),
                Address(email_address='j25@yahoo.com')
                ]
        with self.session.begin():
            addUser(self.session, [jack])
        user = getUser(self.session, name='jack')
        
        self.assertEqual('jack', user.name)
        self.assertEqual(2, len(user.addresses))

if __name__ == '__main__':
    unittest.main()
