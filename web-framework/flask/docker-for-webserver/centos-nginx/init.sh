#!/bin/bash

cd /opt/myapp
uwsgi --socket /tmp/uwsgi.sock --module app --callable app --chmod-socket=666 &

nginx -g "daemon off;"
