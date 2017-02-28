# -*- coding: utf-8 -*-
import unittest
import json

from models import Base, Item
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session, sessionmaker

class ItemTestCase(unittest.TestCase):
    # テストクラスが初期化される際に一度だけ呼ばれる (python2.7以上)
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///models_test.db', echo=True)

    # テストクラスが解放される際に一度だけ呼ばれる (python2.7以上)
    @classmethod
    def tearDownClass(cls):
        cls.engine = None

    # テストクラスが初期化される際に一度だけ呼ばれる (python2.7以上)
    def setUp(self):
        #engine = create_engine('sqlite:///models_test.db', echo=False)
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine, autocommit=True)
        self.session = Session()
    
    def tearDown(self):
        self.session.rollback()
        self.session.close()
    
    def test(self):
        item1 = Item(item_id=u'I001', name=u'商品１', type='item')
        item2 = Item(item_id=u'I002', name=u'商品2', type='item')
        with self.session.begin():
            self.session.add_all([item1, item2])

        got_item1 = self.session.query(Item).get(u'I001')
        got_item2 = self.session.query(Item).get(u'I002')
        
        service = Item(item_id=u'S001', name=u'サービス', type='service')
        service.items.append(got_item1)
        service.items.append(got_item2)

        with self.session.begin():
            self.session.add(service)

        got_service = self.session.query(Item).get(u'S001')
        json_text = json.dumps(got_service.to_dict(), ensure_ascii=False, indent=4)
        print('[DEBUG]001')
        print(json_text)
        
        got_item1 = self.session.query(Item).get(u'I001')
        with self.session.begin():
            self.session.delete(got_item1)

        got_service = self.session.query(Item).get(u'S001')
        json_text = json.dumps(got_service.to_dict(), ensure_ascii=False, indent=4)
        print('[DEBUG]002')
        print(json_text)
        
        print('[DEBUG]003 print backref parent_item')
        print(got_service.items[0].parent_item[0].item_id)


if __name__ == '__main__':
    unittest.main()