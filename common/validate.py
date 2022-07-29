# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : validate.py
# Time       ：1/7/2022 12:47 PM
# Author     ：xionzhi
# version    ：python 3.9
# Description：
"""

from urllib.parse import urlparse


def url_validate(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
