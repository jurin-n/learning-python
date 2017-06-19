## MySQL使う場合
↓下記でドライバインストール
pip install PyMySQL


## 参考
#### Self Referential Many to Many Relationship
http://docs.sqlalchemy.org/en/latest/orm/join_conditions.html#self-referential-many-to-many-relationship

#### relatinship params primaryjoin
http://docs.sqlalchemy.org/en/latest/orm/relationship_api.html#sqlalchemy.orm.relationship.params.primaryjoin

#### relatinship params secondaryjoin
http://docs.sqlalchemy.org/en/latest/orm/relationship_api.html#sqlalchemy.orm.relationship.params.secondaryjoin

#### join conditions relationship primaryjoin
http://docs.sqlalchemy.org/en/latest/orm/join_conditions.html#relationship-primaryjoin

#### Self-Referential Query Strategies
http://docs.sqlalchemy.org/en/latest/orm/self_referential.html#self-referential-query-strategies

#### SQLAlchemy + MySQL を使ってみる（その１）
http://qiita.com/nskydiving/items/88377d57040db17281fe



### テスト
python -m unittest models_test.ItemTestCase.${テストメソッド名}
