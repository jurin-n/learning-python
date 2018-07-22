# -*- coding: utf-8 -*-
import unittest
from models import Base, User, Address
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session, sessionmaker
from sqlalchemy import inspect

class UserTestCase(unittest.TestCase):
    
    def setUp(self):
        engine = create_engine('sqlite:///models_test.db', echo=True)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        # self.session = Session(engine)
        Session = sessionmaker(bind=engine, autocommit=True)
        Session2 = sessionmaker(bind=engine, autocommit=False)
        self.session = Session()
        self.session_auto_false = Session2()

    @unittest.skip("スキップ理由・・・")  
    def test_add(self):
        with self.session.begin():
            ed_user = User(name='taro', fullname=u'テスト　太郎', password='xxxx')
            self.session.add_all([ed_user])
            # self.session.commit()
 
    @unittest.skip("スキップ理由・・・")  
    def test_query(self):
        with self.session.begin():
            user = User(name='taro', fullname=u'テスト　太郎', password='xxxx')
            self.session.add_all([user])
        got_user = self.session.query(User).filter_by(name='taro').first()
        # print our_user  #TODO:マルチバイト文字列が入ると __repr__で UnicodeEncodeError。このエラーが解決できてない。
        self.assertTrue(user is got_user) 
        self.assertEqual(1, user.id)
    
    @unittest.skip('一時的にスキップ')
    def test_join_query(self):
        self._fixture()
        for u, a in self.session.query(User, Address).filter(User.id == Address.user_id).filter(User.password == 'xxxx').all():
            print str(u.id) + ',' + u.name + ',' + a.email_address
    
    def test_query(self):
        self._fixture()
        for u in self.session.query(User).filter(
                                    User.addresses.any(
                                        Address.email_address == 'jiro@google.com')).all():
            print u.fullname

    def test_query2(self):
        self._fixture()
        user = self.session_auto_false.query(User).get(1)
        insp = inspect(user)
        #self.session_auto_false.expunge(user)
        print(insp.detached)
        print('[DEBUG]before del user.addresses[0]')
        del user.addresses[0]
        print('[DEBUG]after del user.addresses[0]')
        self.session_auto_false.commit()
        print('[DEBUG]after commit')
        #with self.session.begin():
        for state in ['transient', 'pending', 'persistent', 'detached']:
            print('{:>10}: {}'.format(state, getattr(insp, state)))
        
    
    def _fixture(self):
        with self.session.begin():
            user1 = User(name='taro', fullname=u'テスト　太郎', password='xxxx')
            user1.addresses = [
                Address(email_address='taro@google.com'),
                Address(email_address='taro@yahoo.com')
                ]
            user2 = User(name='jiro', fullname=u'テスト　二郎', password='xxxx')
            user2.addresses = [
                Address(email_address='jiro@google.com'),
                Address(email_address='jiro@yahoo.com')
                ]
            user3 = User(name='sabu', fullname=u'テスト　三郎', password='0000')
            user3.addresses = [
                Address(email_address='sabu@google.com'),
                Address(email_address='sabu@yahoo.com')
                ]
            self.session.add_all([user1, user2, user3])

            
if __name__ == '__main__':
    unittest.main()
