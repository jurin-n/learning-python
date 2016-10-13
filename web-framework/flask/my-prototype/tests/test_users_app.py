# -*- coding: utf-8 -*-

import os
from users_app import app, db, initdb_command
import pytest
import tempfile
import json

@pytest.fixture
def client(request):
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    # app.config['DATABASE'] = 'sqlite:////tmp/users_app.db'

    client = app.test_client()
    db.drop_all(app=app)
    db.create_all(app=app)
    return client

def test_include_405_test_in_body(client):
    rv = client.get('/')
    assert b'405' in rv.data

def test_post_an_user(client):
    rv = client.post('/', data=json.dumps(dict(username='test taro', email='test.taro@xxx.co.jp')), content_type='application/json')
    assert b'SUCCESS' in rv.data
    