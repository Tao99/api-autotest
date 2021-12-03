# -*- coding: UTF-8 -*-

import time
from config import setting
import unittest
from lib.api_test import Api_Test
from lib import HTMLTestRunner
from lib.new_report import new_report
from lib.send_email import send_email
from lib.logger import log

if __name__ == '__main__':
    testsuite = unittest.TestSuite()
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(Api_Test))
    now = time.strftime('%Y%m%d-%H%M%S')
    file_name = './report/' + now + '.html'
    f = open(file_name, 'w', encoding='utf-8')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title=u'DL接口测试报告',
                                           description=u'测试环境：window 10， 浏览器：Chrome', verbosity=2)
    runner.run(testsuite)
    f.close()
    report = new_report(setting.TESTCASE_REPORT)
    send_email(report)
    log.info("测试报告保存在report文件夹中")
