# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : views.py
# Time       ：1/7/2022 1:12 PM
# Author     ：xionzhi
# version    ：python 3.9
# Description：
"""

from flask import request, redirect, jsonify
from common.base62 import code
from common.validate import url_validate

from service import (app, db, redis_store)
from service.models import DiabloShortUrlModel


def decoding_url(base_62):
    if not base_62:
        return '', 404

    _url = redis_store.get(f'DIABLO_SHORT:{base_62}')
    if not _url:
        short_query = db.session.query(DiabloShortUrlModel). \
            filter(DiabloShortUrlModel.id == code.decode_62to10(base_62)).first()
        if not short_query:
            return '', 404

        _url = short_query.url
        redis_store.set(f'DIABLO_SHORT:{base_62}', _url, nx=True, ex=600)

    return redirect(_url, code=301)


def short_url():
    try:
        url = request.json.get('url')
        if not url:
            return jsonify(dict(msg=f'not url', code=400)), 400
    except Exception as e:
        return jsonify(dict(msg=f'not url', code=400)), 400

    if not url_validate(url):
        return jsonify(dict(msg=f'not url', code=400)), 400

    reverse_url = url[::-1]

    try:
        short_query = db.session.query(DiabloShortUrlModel). \
            filter(DiabloShortUrlModel.reverse_url == reverse_url).first()
        if short_query:
            base_62 = short_query.base62

        else:
            short_query = DiabloShortUrlModel(base62='', url=url, reverse_url=reverse_url)
            db.session.add(short_query)
            db.session.flush()

            if isinstance(short_query.id, int) is False:
                return jsonify(msg=f'{short_query.id}', code=500), 500

            base_62 = code.encode_10to62(short_query.id)
            short_query.base62 = base_62

            db.session.commit()

    except Exception as e:
        db.session.rollback()
        return jsonify(dict(msg=f'{e}', code=500)), 500

    # set redis
    redis_store.set(f'DIABLO_SHORT:{base_62}', url, nx=True, ex=600)

    _short_url = f'{app.config["HOST"]}/{base_62}'

    return jsonify(dict(short_url=_short_url, code=200)), 200
