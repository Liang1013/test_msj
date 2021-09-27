from common import HTMLTestRunner
from common.route import Route
from common.sendmail import SendMail
from common.logger import Log

import unittest

class SendReport():
    logger = Log("SendReport").get_log()

    '''
    获取测试用例路径，test*.py是用例
    '''
    discover = unittest.defaultTestLoader.discover(start_dir=
                                                   Route().js_route_report("case"),
                                                   pattern="test_login.py")

    # 获取写入报告路 已二进制写入路径下
    reportpath = Route().js_route_report("report/" + "reprot.html")
    fg = open(reportpath, "wb")

    reunner = HTMLTestRunner.HTMLTestRunner(stream=fg,
                                            title="msj工具自动化测试")

    '''生成报告'''
    reunner.run(discover)
    logger.info("测试报告生成成功")


    '''发送邮件'''
    parameter = Route().js_route_mail("mail")
    smtp_receiver = parameter["smtp_receiver"]
    m = SendMail(
        username=parameter["username"], passwd=parameter["password"], recv=smtp_receiver,
        title='自动化测试报告', email_host=parameter["email_stmp"],file=reportpath
    )
    m.send_mail()
