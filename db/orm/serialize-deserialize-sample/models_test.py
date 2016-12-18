# -*- coding: utf-8 -*-
import unittest
from models import Base, User, Address, UserSchema
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session, sessionmaker
from sqlalchemy.orm import joinedload
from sqlalchemy import inspect
from marshmallow import pprint

class UserTestCase(unittest.TestCase):
    
    def setUp(self):
        engine = create_engine('sqlite:///models_test.db', echo=False)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine, autocommit=True)
        self.session = Session()
   
    @unittest.skip('一時的にスキップ')
    def test_query(self):
        UserFixture.three_user_add(self.session)
        
        user = self.session.query(User).get(1)
        
        insp = inspect(user)
        print(insp.detached)
        for state in ['transient', 'pending', 'persistent', 'detached']:
            print('{:>10}: {}'.format(state, getattr(insp, state)))
    
    def test_serialize(self):
        UserFixture.three_user_add(self.session)
        user_schema = UserSchema()

        user = self.session.query(User).options(joinedload('addresses')).get(2)
        
        dump_data = user_schema.dumps(user).data
        #print(dump_data)
        pprint(dump_data, indent=2)
        
    @unittest.skip('一時的にスキップ')
    def test_deserialize(self):
        user_schema = UserSchema()
        user_schema.load(dump_data, session=self.session).data
        
class UserFixture():
    @staticmethod
    def three_user_add(session):
        with session.begin():
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
            session.add_all([user1, user2, user3])

            
if __name__ == '__main__':
    unittest.main()
