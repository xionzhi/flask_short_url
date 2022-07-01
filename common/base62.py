# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : base62.py
# Time       ：1/7/2022 1:15 PM
# Author     ：xionzhi
# version    ：python 3.9
# Description：
"""

import string


class Base62:
    def __init__(self):
        self.BASE_STR = string.ascii_letters + string.digits
        self.BASE = len(self.BASE_STR)

    def __10to62(self, digit, value=None):
        if value is None:
            value = list()
        rem = int(digit % self.BASE)
        value.append(self.BASE_STR[rem])
        div = int(digit / self.BASE)
        if div > 0:
            value = self.__10to62(div, value)
        return value

    def __62to10(self, str_value):
        value_list = list(str_value)
        value_list.reverse()
        temp_list = [self.BASE_STR.index(ele) * (self.BASE ** n) for n, ele in enumerate(value_list)]
        return sum(temp_list)

    def encode_10to62(self, digit: int) -> str:
        """
        10进制转为62进制
        """
        if not isinstance(digit, int) or digit < 0:
            raise TypeError('base10 number error')
        value = self.__10to62(digit)
        value.reverse()
        value = ''.join(value)
        return value

    def decode_62to10(self, str62: str) -> int:
        """
        62进制转为10进制
        """
        check = sum([1 for ele in str62 if ele not in self.BASE_STR])
        if check > 0 or len(str62) == 0 or not isinstance(str62, str):
            raise TypeError('base62 number error')
        return self.__62to10(str62)
