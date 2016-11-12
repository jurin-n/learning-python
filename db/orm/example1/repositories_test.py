# -*- coding: utf-8 -*-
from unittest import TestCase, main
from domains import Base, User
from repositories import addUser
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
            addUser(self.session,[user])


if __name__ == '__main__':
    main()