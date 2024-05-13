#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2024-4-27 8:45
# Author:Yanglei
# @File:send_email_base.py
# @Software:PyCharm
import smtplib
from email.mime.text import MIMEText
msg = MIMEText('我是测试邮件的正文','plain','utf-8')
msg['From'] = '3373209715@qq.com'
msg['To'] = '3373209715@qq.com'
msg['Subject'] = '接口测试报告主题'
smtp = smtplib.SMTP_SSL('smtp.qq.com')
smtp.login('3373209715@qq.com','aqbfswmimygrdacg')
smtp.sendmail('3373209715@qq.com','3373209715@qq.com', msg.as_string())
smtp.quit()