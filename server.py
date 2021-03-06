#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/27 19:53
# @Author : way
# @Site : 
# @Describe:  api 服务

import base64
from io import BytesIO
from flask import Flask, jsonify, make_response, request
from hashlib import md5
from utils.parse import parse

app = Flask(__name__)
key = 'fileparse'  # 设置 api 秘钥


@app.route('/openapi/parse', methods=['POST'])
def fileparse():
    t = request.form.get('t')
    token = request.form.get('token')
    if key and token != md5(f'{key}{t}'.encode(encoding='utf-8')).hexdigest():
        return make_response(jsonify({'success': False, 'result': '', 'errorMessage': 'token error !'}), 404)
    fileData = request.form.get('fileData')
    fileType = request.form.get('fileType')
    if not fileData or not fileType:
        return make_response(jsonify({'success': False, 'result': '', 'errorMessage': 'fileData、fileType 不能为空'}), 405)
    try:
        file = BytesIO(base64.b64decode(fileData))
        issuccess, content = parse(file, fileType)
    except Exception as e:
        issuccess, content = False, str(e)
    if issuccess:
        return make_response(jsonify({'success': True, 'result': content, 'errorMessage': ''}), 200)
    return make_response(jsonify({'success': False, 'result': '', 'errorMessage': content}), 503)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9527, threaded=True)
