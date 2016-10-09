FROM centos:centos7

RUN rpm -ivh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
RUN yum -y update
RUN yum -y install nginx

# install pip.
RUN curl -kL https://bootstrap.pypa.io/get-pip.py | python
# install uwsgi
RUN yum -y install gcc python-devel
RUN pip install Flask uwsgi
RUN pip install --upgrade pip setuptools

# add flask app.
ADD ./myapp /opt/myapp/

# copy nginx config for flask app.
ADD ./flask.conf /etc/nginx/conf.d/flask.conf
RUN mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf_backup

#WORKDIR /opt/myapp
#RUN uwsgi --socket /tmp/uwsgi.sock --module app --callable app --chmod-socket=666 &

ADD ./init.sh /opt/init.sh
RUN chmod u+x /opt/init.sh

# start nginx
EXPOSE 80 443
# CMD nginx -g "daemon off;"
CMD ["./opt/init.sh"]