# -*- coding: utf-8 -*-
from unittest import TestCase, main
from domains import Base, User
from repositories import addUser, getAllUser, getUser
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session, sessionmaker

class RepositoriesTestCase(TestCase):
    def setUp(self):
        engine = create_engine('sqlite:///repositories_test.db', echo=True)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        # self.session = Session(engine)
        Session = sessionmaker(bind=engine, autocommit=True)
        self.session = Session()

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
        user = getUser(self.session, 'jiro')
        self.assertEqual('jiro', user.name)

if __name__ == '__main__':
    main()
