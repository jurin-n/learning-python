# -*- coding: utf-8 -*-
import unittest
from domains import Base, User, Address
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session, sessionmaker

class UserTestCase(unittest.TestCase):
    
    def setUp(self):
        engine = create_engine('sqlite:///domains_test.db', echo=True)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        # self.session = Session(engine)
        Session = sessionmaker(bind=engine, autocommit=True)
        self.session = Session()

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
        
    def test_join_query(self):
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

        for u, a in self.session.query(User, Address).filter(User.id == Address.user_id).filter(User.password == 'xxxx').all():
            print str(u.id) + ',' + u.name + ',' + a.email_address

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
    unittest.main()
