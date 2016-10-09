## dockerコマンド
#### stop 〜削除
docker stop webserver
docker rm webserver
docker rmi webserver

#### build 〜 コンテナログイン
docker build -t webserver .
docker run -d -p 80:80 --name webserver webserver
docker start webserver
docker exec -it webserver /bin/bash


## 参考
### pipインストールについて
https://pip.pypa.io/en/latest/installing/

### uWSGIについて
http://flask.pocoo.org/docs/0.11/deploying/uwsgi/

### Nginx
デフォルト設定
/etc/nginx/nginx.conf
/var/log/nginx/error.log

#### Centos7で利用可能のパッケージを http://nginx.org/packages/centos/ で確認
rpm -ivh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
cat /etc/yum.repos.d/nginx.repo
yum list |grep nginx
yum -y install nginx
nginx -v

