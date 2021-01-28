#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/27 18:37
# @Author : way
# @Site : 
# @Describe: PaddleOCR

import numpy as np
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image

OCR = PaddleOCR(use_gpu=False)  # need to run only once to download and load model into memory


def img_parse(fb):
    """
    :param fb: A filename (string), pathlib.Path object or a file object.
    :return: result txt
    """
    fb = Image.open(fb).convert('RGB')
    result = OCR.ocr(np.array(fb))
    return '\n'.join([line[1][0] for line in result])


def img_parse_test(fb):
    """
    :param fb: A filename (string), pathlib.Path object or a file object.
    :return: show pic
    """
    image = Image.open(fb).convert('RGB')
    result = OCR.ocr(np.array(image))
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='/path/to/PaddleOCR/doc/simfang.ttf')
    im_show = Image.fromarray(im_show)
    im_show.show()
