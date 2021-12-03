#!/usr/bin/env python3.9
# encoding: utf-8

from lib.logger import log


def assert_contains(code, data, result_code, result_data):
    """

    :param code : 预期状态码
    :param data: 预期返回内容
    :param result_code: 实际状态码
    :param result_data: 实际返回内容
    :return:
    """
    if code and data:  # 预期code和data都填写时
        log.debug("开始校验code状态码：-> 预期返回：" + str(code) + " , " + "实际返回：" + str(result_code))
        log.debug("开始校验data返回值：-> 预期返回：" + str(data) + " , " + "实际返回：" + str(result_data))
        try:
            assert code == result_code
            assert data in result_data
            log.info("用例测试通过")
        except AssertionError as e:
            log.error("用例测试失败" + str(e))
            return False
        return True
    if code:  # 预期只有code填写时
        log.debug("开始校验code状态码：-> 预期返回：" + str(code) + " , " + "实际返回：" + str(result_code))
        try:
            assert code == result_code
            log.info("用例测试通过")
        except AssertionError as e:
            log.error("用例测试失败" + str(e))
            return False
        return True
    if data:  # 预期只有data填写时
        log.debug("开始校验data返回值：-> 预期返回：" + str(data) + " , " + "实际返回：" + str(result_data))
        try:
            assert data in result_data
            log.info("用例测试通过")
        except AssertionError as e:
            log.error("用例测试失败" + str(e))
            return False
        return True
    else:
        log.debug("未设置预期结果，需设置校验后再判断")


if __name__ == '__main__':
    code = 200
    name = "Tao"
    result_code = 200
    result_data = "{'name':'Tao', 'age': 18}"
    print(assert_contains(code, name, result_code, result_data))
