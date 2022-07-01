# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : __init__.py.py
# Time       ：1/7/2022 1:11 PM
# Author     ：xionzhi
# version    ：python 3.9
# Description：
"""

from flask import Flask
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

from urllib.parse import quote_plus


app = Flask(__name__, static_folder='../static')

app.config.from_object('config.production')
app.debug = app.config['APP_DEBUG']
app.config['JSON_AS_ASCII'] = False


app.config.setdefault('SQLALCHEMY_DATABASE_URI',
                      f'mysql+pymysql://{quote_plus(app.config["DATABASE_USER"])}:{quote_plus(app.config["DATABASE_PASSWORD"])}@'
                      f'{app.config["DATABASE_HOST"]}:{app.config["DATABASE_PORT"]}/{app.config["DATABASE_NAME"]}')
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
app.config.setdefault('SQLALCHEMY_ECHO', app.config['SQL_DEBUG'])
app.config.setdefault('SQLALCHEMY_POOL_RECYCLE', 3333)
app.config.setdefault('SQLALCHEMY_POOL_SIZE', 50)
app.config.setdefault('SQLALCHEMY_MAX_OVERFLOW', 50)

db = SQLAlchemy(app)

redis_store = FlaskRedis(app, decode_responses=True)


def init_app():
    from service.urls import site
    app.register_blueprint(site)


init_app()
