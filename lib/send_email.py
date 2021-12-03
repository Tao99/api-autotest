#!/usr/bin/env python3.9.2
# _*_ coding:utf-8 _*_
# order by tao

import smtplib
from lib.logger import log
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from config import setting
from lib.read_write import Files
data = Files(setting.CONFIG).get_data().get("email", {})


def send_email(file):
    # 邮件配置
    username_send = data['username_send']  # 发件人
    log.info("发件人是：" + username_send)
    username_received = data['username_received']  # 收件人可以是多人
    # print("收件人是：" + username_received)
    email_server = data['email_server']  # 邮箱服务端url
    pwd_send = data['pwd_send']  # 邮箱授权码
    """
    # 邮件发送
    content = "这是一份邮件"
    email = MIMEText(content, 'plain', 'uft-8')  # 文本形式的邮件
    email['Subject'] = '邮件主题'
    email['From'] = username_send
    email['To'] = ','.join(username_received)
    # 图片文件附件
    att1 = MIMEBase('application', 'octet-stream')
    att1.set_payload(open("123.jpeg", 'rb').read())
    att1.add_header('Content-Disposition', 'attachment', filename=Header('123.jpeg', 'gbk').encode())
    encoders.encode_base64(att1)
    email.attach(att1)
    """
    # 附件配置构建根容器
    email = MIMEMultipart()
    # 设置根容器属性
    email['Subject'] = '接口自动化测试报告'
    email['From'] = username_send
    email['To'] = ','.join(username_received)
    # 邮件内容加到根容器
    text_msg = MIMEText("Hi, \n\n 这是接口测试的自动化测试报告")
    email.attach(text_msg)
    # 邮件附件加到根容器
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(open(file, 'rb').read())
    att.add_header('Content-Disposition', 'attachment', filename=Header(file, 'gbk').encode())
    encoders.encode_base64(att)
    email.attach(att)

    # 发邮件
    try:
        smtp = smtplib.SMTP_SSL(email_server, port=465)
        smtp.login(username_send, pwd_send)
        smtp.sendmail(username_send, ','.join(username_received), email.as_string())
        smtp.quit()
        log.info("邮件发送成功")
    except Exception as e:
        print("邮件发送失败" + str(e))
        log.error("邮件发送失败，请检查邮件配置")
