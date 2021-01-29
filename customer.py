#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/27 18:54
# @Author : way
# @Site : 
# @Describe: 直接调用解析函数

from utils.parse import parse

test_list = [
    '123.bmp',
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.jpg',
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.png',
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.doc',
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.docx',
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.pdf'
]

for path in test_list:
    issuccess, content = parse(path)
    print(path, issuccess, content)
