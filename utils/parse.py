#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/27 21:09
# @Author : way
# @Site : 
# @Describe:

import requests
from io import BytesIO
from utils.file_parse import docx_parse, doc_parse, pdf_parse
from utils.img_ocr import img_parse


def parse(fb, file_type=None):
    """
    :param fb: A filename (string), pathlib.Path object, file url or a file object
    :param file_type: 文件类型
    :return: 识别是否成功，识别内容
    """
    if isinstance(fb, str) and not file_type:
        file_type = fb.split('.')[-1]

    if isinstance(fb, str) and fb.startswith('http'):
        fb = BytesIO(requests.get(fb).content)

    if file_type in ('jpg', 'png', 'bmp', 'gif'):
        return True, img_parse(fb)
    elif file_type == 'doc':
        return True, doc_parse(fb)
    elif file_type == 'docx':
        return True, docx_parse(fb)
    elif file_type == 'pdf':
        return True, pdf_parse(fb)
    return False, '不支持的文件格式'
