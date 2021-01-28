#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/27 18:54
# @Author : way
# @Site : 
# @Describe: 直接调用解析函数

from utils.parse import parse

test_list = [
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.jpg',
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.png',
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.doc',
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.docx',
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.pdf'
]

for path in test_list:
    file_type = path.split('.')[-1]
    issuccess, content = parse(path, file_type)
    print(path, issuccess, content)
