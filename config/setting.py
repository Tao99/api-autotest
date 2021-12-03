# -*- coding: UTF-8 -*-
import os
import sys

BASE = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE)
print(BASE)
# 测试用例主文件
TESTCASE_YAML = os.path.join(BASE, 'testcase/PMA', 'main.yml')
# 测试目录
TESTCASE_DIE = os.path.join(BASE, 'testcase/PMA')
# 测试报告
TESTCASE_REPORT = os.path.join(BASE, 'report')
# 配置文件
CONFIG = os.path.join(BASE, 'config', 'config.yml')
# 日志
LOG_DIR = os.path.join(BASE, 'logs')
