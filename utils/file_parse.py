#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/27 18:53
# @Author : way
# @Site : 
# @Describe:

import docx
import pdfplumber
import tempfile
import subprocess
import os
import uuid
import platform
from io import BytesIO

try:
    import pythoncom
    import win32com.client as wc
except:
    ...


def docx_parse(fb):
    """
    :param fb: A filename (string), pathlib.Path object or a file object.
    :return: result txt
    """
    doc = docx.Document(fb)
    paras = [para.text for para in doc.paragraphs if para.text]
    content = '\n'.join(paras) if paras else ''
    return content


def pdf_parse(fb):
    """
    :param fb: A filename (string), pathlib.Path object or a file object.
    :return: result txt
    """
    pdf = pdfplumber.open(fb)
    paras = [page.extract_text() for page in pdf.pages if page.extract_text()]
    content = '\n'.join(paras) if paras else ''
    return content


def linux_doc_parse(fb):
    """
    :param fb: A filename (string), pathlib.Path object or a file object.
    :return: result txt
    """
    if isinstance(fb, BytesIO):
        byte_content = fb.read()
        fb.close()
    else:
        with open(fb, 'rb') as fb:
            byte_content = fb.read()
    with tempfile.NamedTemporaryFile() as f:
        f.write(byte_content)
        cmd = f'antiword -mUTF-8 {f.name}'
        with tempfile.TemporaryFile(mode='w+') as f2:
            p = subprocess.Popen(cmd, stdout=f2, shell=True)
            p.communicate()
            f2.seek(0)
            return f2.read()


def win_doc_parse(fb):
    """
    :param fb: A filename (string), pathlib.Path object or a file object.
    :return: result txt
    """
    if isinstance(fb, BytesIO):
        byte_content = fb.read()
        fb.close()
    else:
        with open(fb, 'rb') as fb:
            byte_content = fb.read()
    filename = f'{os.getcwd()}\{str(uuid.uuid4())}.doc'  # 需要使用绝对路径
    with open(filename, 'wb') as f:
        f.write(byte_content)
    try:
        pythoncom.CoInitialize()
        word = wc.Dispatch("Word.Application")
        doc = word.Documents.Open(filename)
        doc.SaveAs(filename + 'x', 16)
        doc.Close()
        word.Quit()
        content = docx_parse(filename + 'x')
    except Exception as e:
        print(e)
        content = ''
    finally:
        pythoncom.CoUninitialize()
        if os.path.exists(filename):
            os.remove(filename)
        if os.path.exists(filename + 'x'):
            os.remove(filename + 'x')
    return content


def doc_parse(*args, **kwargs):
    if platform.system() == 'Windows':
        return win_doc_parse(*args, **kwargs)
    else:
        return linux_doc_parse(*args, **kwargs)
