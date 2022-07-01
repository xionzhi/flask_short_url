# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : production.py
# Time       ：1/7/2022 1:15 PM
# Author     ：xionzhi
# version    ：python 3.9
# Description：
"""

APP_DEBUG = False

DATABASE_HOST = '127.0.0.1'
DATABASE_PASSWORD = '123456'
DATABASE_USER = 'user'
DATABASE_NAME = 'short'
DATABASE_PORT = 3306

SQL_DEBUG = False

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'

HOST = 'https://xxx.com'
