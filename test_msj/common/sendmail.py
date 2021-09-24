#!/usr/bin/python
# -*- coding:utf-8 -*-

import smtplib  # smtplib这个模块是管发邮件
from email.mime.text import MIMEText  # 构造邮件内容
from email.mime.multipart import MIMEMultipart  # 发带附件的邮件用的
from common.route import Route
from common.logger import Log

log = Log('run').get_log()
class SendMail(object):

    def __init__(self, username, passwd, recv, title, file=None, email_host='smtp.163.com', port=25):
        '''
        发送邮件封装
        :param username: 发送者账号
        :param passwd: 发送者邮箱的授权码
        :param recv: 收件人
        :param title: 邮件主题
        :param file:附件
        :param email_host:邮箱服务器地址 smtp.163.com   smtp.qq.com   smtp.mxhichina.com
        :param port:端口
        '''
        self.username = username
        self.passwd = passwd
        self.recv = recv
        self.title = title
        self.file = file
        self.email_host = email_host
        self.port = port

    def send_mail(self):
        # 发送内容的对象
        msg = MIMEMultipart()
        # 处理附件
        if self.file:
            att = MIMEText(open(self.file).read())
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="%s"'%self.file
            msg.attach(att)
        with open(self.file, 'r', encoding='utf-8') as f:
            mail_body = f.read()
        msg.attach(MIMEText(mail_body,'html','utf-8'))              # 邮件的内容
        msg['Subject'] = self.title                                 # 邮件主题
        msg['From'] = self.username                                 # 发送者账号
        msg['To'] = ','.join(self.recv)                             # 接收者账号列表
        self.smtp = smtplib.SMTP(self.email_host, port=self.port)   # 发送邮件服务器的对象
        self.smtp.login(self.username, self.passwd)
        try:
            self.smtp.sendmail(self.username, self.recv, msg.as_string())
        except Exception as e:
            print('邮件出错了。。', e)
            log.info('测试报告邮件发送失败')
        else:
            print('邮件发送成功！')
            log.info('测试报告邮件发送成功')

    def __del__(self):
        self.smtp.quit()


if __name__ == '__main__':
    reportpath = Route().is_report("report/") + "report.html"
    smtp_receiver = ['1123@163.com']
    m = SendMail(
        username='123@163.com', passwd='123456', recv= smtp_receiver,
        title='自动化测试报告',file=reportpath
    )
    m.send_mail()