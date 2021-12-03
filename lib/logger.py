#!/usr/bin/env python3.9
# encoding: utf-8
import logging
import time
import os
from config import setting


class Logger(object):
    """
    终端打印不同颜色的日志，在pycharm中如果强行规定了日志的颜色， 这个方法不会起作用， 但是
    对于终端，这个方法是可以打印不同颜色的日志的。
    """

    # 在这里定义StreamHandler，可以实现单例， 所有的logger()共用一个StreamHandler
    ch = logging.StreamHandler()

    def __init__(self):
        # 文件的命名
        self.logname = os.path.join(setting.LOG_DIR, '%s.log' % time.strftime('%Y%m%d%H%M%S'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter(
            '[%(asctime)s] [%(filename)s|%(funcName)s] [line:%(lineno)d] %(levelname)-s: %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地日志文件
        fh = logging.FileHandler(self.logname, encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.set_color_formatter('\033[0;34m%s\033[0m')
        self.logger.debug(message)

    def info(self, message):
        self.set_color_formatter('\033[0;32m%s\033[0m')
        self.logger.info(message)

    def warning(self, message):
        self.set_color_formatter('\033[0;33m%s\033[0m')
        self.logger.warning(message)

    def error(self, message):
        self.set_color_formatter('\033[0;35m%s\033[0m')
        self.logger.error(message)

    def critical(self, message):
        self.set_color_formatter('\033[0;31m%s\033[0m')
        self.logger.critical(message)

    def set_color_formatter(self, color):
        # 不同的日志输出不同的颜色
        formatter = logging.Formatter(color % self.formatter)
        self.ch.setFormatter(formatter)
        self.ch.setLevel(logging.INFO)
        self.logger.addHandler(self.ch)

log = Logger()
