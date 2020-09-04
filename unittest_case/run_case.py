# coding=utf-8

import unittest
import os
import HTMLTestRunner
import time


class RunCase(unittest.TestCase):

    def test_run(self):
        timedata = time.strftime('%Y.%m.%d', time.localtime(time.time()))
        suite = unittest.defaultTestLoader.discover(os.getcwd(), 'unittest_*.py')
        file_path = 'D:/xuexi/SuperStudy/superstudy/unittest_case/report/'+timedata+'.html'
        # os.getcwd()+'\\report\\'+timedata+'.html'
        f = open(file_path, 'wb')
        #unittest.TextTestRunner().run(suite)
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='自动化测试报告',description=u'这是s.wanxue.cn的测试报告',verbosity=2)
        runner.run(suite)


if __name__ == '__main__':
    unittest.main()
