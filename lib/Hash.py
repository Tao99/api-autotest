# encoding:utf-8
# 封装算法加密的方法
import base64
from hashlib import md5, sha1
from urllib.parse import quote, unquote
from pyDes import des, CBC, PAD_PKCS5


def my_md5(msg):
    """
    md5模式加密
    :param msg:
    :return:
    """
    hl = md5()
    hl.update(msg.encode('utf-8'))
    return hl.hexdigest()


def my_sha1(msg):
    """
    sha1模式加密
    :param msg:
    :return:
    """
    sh = sha1()
    sh.update(msg.encode('utf-8'))
    return sh.hexdigest()


def url_quote(url):
    """
    url加密
    :param url:
    :return:
    """
    return quote(url)


def url_unquote(url):
    """
    url解密
    :param url:
    :return:
    """
    return unquote(url)


def pwd_encrypt(pwd=None, secret_key=None, iv=None):
    """
    密码加密
    :param pwd: 密码
    :param secret_key: 加密密钥,must be exactly 8 bytes long
    :param iv: 偏移
    :return:
    """
    if iv is None and secret_key is not None:
        iv = secret_key
    des_obj = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    pwd_bytes = des_obj.encrypt(pwd)  # 返回字节
    return base64.b64encode(pwd_bytes).decode()  # 返回16进制


def pwd_crypt(pwd=None, secret_key=None, iv=None):
    """
    密码解密
    :param pwd:
    :param secret_key:
    :param iv:
    :return:
    """
    if iv is None and secret_key is not None:
        iv = secret_key
    des_obj = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    decrypt_str = des_obj.decrypt(base64.b64decode(pwd))
    return decrypt_str.decode()


if __name__ == '__main__':
    print(pwd_encrypt('123', '00000000'))
    print(pwd_crypt('HPrgvA8kL6k=', '00000000'))
    print(url_quote('192.168.1.103:20210/user="泰语"'))
