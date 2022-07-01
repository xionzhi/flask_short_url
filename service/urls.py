# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : urls.py
# Time       ：1/7/2022 1:12 PM
# Author     ：xionzhi
# version    ：python 3.9
# Description：
"""

from flask import Blueprint
from service.views import (decoding_url, short_url)


site = Blueprint('short', __name__, url_prefix='/')


site.add_url_rule('/<base_62>', view_func=decoding_url, methods=['GET'])
site.add_url_rule('/short_url', view_func=short_url, methods=['POST'])
