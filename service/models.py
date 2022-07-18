# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : models.py
# Time       ：1/7/2022 1:11 PM
# Author     ：xionzhi
# version    ：python 3.9
# Description：
"""

from service import db


class DiabloShortUrlModel(db.Model):
    __tablename__ = 'diablo_short_url'

    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    base62 = db.Column(db.VARCHAR(64), comment='短链接key')
    reverse_url = db.Column(db.VARCHAR(1024), index=True, comment='长链接反转 index len 32')
