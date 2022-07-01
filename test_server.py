# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_server.py
# Time       ：1/7/2022 1:27 PM
# Author     ：xionzhi
# version    ：python 3.9
# Description：
"""

from service import app


if __name__ == '__main__':
    app.run(debug=True)
