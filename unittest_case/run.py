# coding=utf-8

import datetime
import os
import unittest

from BeautifulReport import BeautifulReport
#这是执行文件
root_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
test_dir = root_dir
report_dir = root_dir + '/report'

discover = unittest.defaultTestLoader.discover(test_dir, 'unittest_*.py', None)
now = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
filename = '测试报告' + str(now)
BeautifulReport(discover).report(description='测试', filename=filename, log_path=report_dir)