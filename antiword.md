## 1. 下载安装包

```shell
wget http://www.winfield.demon.nl/linux/antiword-0.37.tar.gz
```

## 2. 解压安装包
```shell
tar -zxvf antiword-0.37.tar.gz
cd antiword-0.37
```

## 3. 编译安装包
```shell
make && make install
```

## 4. 修改权限

```shell
cp /root/bin/*antiword /usr/local/bin/
mkdir /usr/share/antiword
cp -R /root/.antiword/* /usr/share/antiword/
chmod 777 /usr/local/bin/*antiword
chmod 755 /usr/share/antiword/*
```

## 5. 测试读取doc文档

```shell
antiword -mUTF-8 test.doc
```