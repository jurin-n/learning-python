### 参考資料
* SQLAlchemy in Flask [http://flask.pocoo.org/docs/0.11/patterns/sqlalchemy/]
* Flask-SQLAlchemy [http://flask-sqlalchemy.pocoo.org/2.1/]

### MySQLコンテナ
#### 永続化用のDisk作成
docker run -v /var/lib/mysql --name mysql_data busybox
#### MySQLコンテナ作成
docker run --volumes-from mysql_data --name mysql -e MYSQL_ROOT_PASSWORD=mysql -d -p 3306:3306 mysql
#### MySQLコンテナ接続
docker exec -it mysql /bin/bash
#### MySQLコンテナのOSでmysqlに接続
mysql -s -u root -h localhost -pmysql