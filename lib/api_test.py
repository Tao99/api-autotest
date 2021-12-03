#!/usr/bin/env python3.9
# encoding: utf-8

import json
import unittest

import datetime
import ddt
import requests

from config import setting
from lib import read_write
from lib.assert_result import assert_contains
from lib.logger import log

test_data = read_write.Files(setting.TESTCASE_YAML).get_data()


@ddt.ddt()
class Api_Test(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @ddt.data(*test_data)
    def test_api(self, data):
        for j in range(len(data)):
            name = data[j].get('name')
            url = data[j].get('url')
            method = data[j].get('method')
            params = data[j].get('params', {})  # 请求数据
            headers = data[j].get('headers', {})  # 请求头
            cookies = data[j].get('cookies', {})  # 请求cookies
            assert_data = data[j].get('assert', {})
            code = assert_data['status code']
            if method == 'get':
                start_time = datetime.datetime.now()
                res = requests.get(url=url, params=params, cookies=cookies, headers=headers)
                end_time = datetime.datetime.now()
                log.warning("-----------------------------------------------------")
                log.info("当前测试的用例是：" + name)
                log.info("执行用时：" + str(round(((end_time - start_time).total_seconds()) * 1000, 3)) + "毫秒")
                if res.status_code == 200:
                    assert_contains(code=code, data=str(assert_data['ok']), result_code=res.status_code,
                                    result_data=str(res.json()['ok']))
                elif res.status_code != 200:
                    assert_contains(code=code, data=str(assert_data['error']), result_code=res.status_code,
                                    result_data=str(res.json()['error']))

            elif method == 'post':
                start_time = datetime.datetime.now()
                params_json = json.dumps(params)  # 将数据解析为json
                res = requests.post(url=url, data=params_json, cookies=cookies, headers=headers)
                end_time = datetime.datetime.now()
                log.warning("-----------------------------------------------------")
                log.info("当前执行的用例是：" + name)
                log.info("执行用时：" + str(round(((end_time - start_time).total_seconds()) * 1000, 3)) + "毫秒")
                if res.status_code == 200:
                    assert_contains(code=code, data=str(assert_data['ok']), result_code=res.status_code,
                                    result_data=str(res.json()['ok']))
                elif res.status_code != 200:
                    assert_contains(code=code, data=str(assert_data['error']), result_code=res.status_code,
                                    result_data=str(res.json()['error']))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
