# fileparse
文件通用解析服务

# 说明

| 文件格式  |  是否支持  |  实现方法  |
| ------------ | ------------ | ------------ |
| 图片（jpg、png、bmp、gif） |  √  | paddleocr |
| pdf  |  √  | pdfplumber |
| docx  |  √  | python-docx  |
| doc  |  √  | windows 使用 pypiwin32 转 docx <br> linux 使用 antiword 直接解析, [如何安装 antiword](antiword.md) |

# 安装

```
pip install paddlepaddle==2.0.0rc1 -i https://mirror.baidu.com/pypi/simple
pip install paddleocr -i https://mirror.baidu.com/pypi/simple
pip install pdfplumber
pip install python-docx
pip install flask
```

window 环境需要安装

```
pip install pywin32
```


# 使用（客户端）

直接调用解析函数即可

```python
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
```

# 使用（服务端）

运行 server.py，就可以直接使用文件解析 api 

**请求URL：**
- ` http://127.0.0.1:9527/openapi/parse `

**请求方式：**
- POST

**参数：**

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|fileData | 是 |string |  文件内容的base64字符串  |
|fileType | 是 |string |  文件类型  |
|t | 是 |int | 当前时间戳  |
|token | 是 |string | token。生成方式：md5(key+当前时间戳)，默认 key 为 fileparse  |

 **返回示例**

```
{
    'errorMessage': '', 
    'result': '首先请您选择您的版本\n如果您的计算机没有NVIDIAGPU，请安装CPU版的PaddlePaddle\n如果您的计算机有NVIDIA@GPU，请确保满足以下条件并且安装GPU版PaddlePaddlle\nOCUDA工具包9.0/10.0配合CuDNNv7.3+\n·GPU运算能力超过1.0的硬件设备\n您可参考NVIDIA官方文档了解CUDA和CUDNN的安装流程和配置方法，请见CUDA，cuDNN', 
    'success': True
}

```

 **返回参数说明**

|参数名|类型|说明|
|:-----  |:-----|-----                           |
|success | bool | 调用成功标识，true:成功 false:失败 |
|errorMessage | string | 错误信息 |
|result | string | 识别结果|






