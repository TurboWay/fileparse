#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/27 20:48
# @Author : way
# @Site : 
# @Describe: api 测试

import base64
import requests

def test(path):
    if path.startswith('http'):
        content = requests.get(path).content
        fileData = base64.b64encode(content)
    else:
        with open(path, 'rb') as f:
            fileData = base64.b64encode(f.read())
    data = {
        'fileData': fileData,
        'fileType': path.split('.')[-1],
        'auth': 'fileparse_key'
    }
    url = 'http://127.0.0.1:9527/openapi/parse'
    res = requests.post(url, data=data).json()
    return res

test_list = [
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.jpg',
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.png',
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.doc',
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.docx',
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.pdf'
]
for path in test_list:
    res = test(path)
    print(path, res)