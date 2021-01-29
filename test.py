#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/27 20:48
# @Author : way
# @Site : 
# @Describe: api 测试

import time
import base64
import requests
from hashlib import md5

key = 'fileparse'


def test(path):
    if path.startswith('http'):
        content = requests.get(path).content
        fileData = base64.b64encode(content)
    else:
        with open(path, 'rb') as f:
            fileData = base64.b64encode(f.read())
    t = int(time.time() * 1000)
    data = {
        'fileData': fileData,
        'fileType': path.split('.')[-1],
        't': t,
        'token': md5(f'{key}{t}'.encode(encoding='utf-8')).hexdigest()
    }
    url = 'http://127.0.0.1:9527/openapi/parse'
    res = requests.post(url, data=data).json()
    return res


test_list = [
    '123.bmp',
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.jpg',
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.png',
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.doc',
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.docx',
    'https://gitee.com/TurboWay/blogimg/raw/master/img/test.pdf'
]
for path in test_list:
    res = test(path)
    print(path, res)
