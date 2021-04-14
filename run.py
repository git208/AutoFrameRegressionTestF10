import json
import os
import time
import unittest

from common import HTMLTestRunner

from common.test_cases_driver import TestCaseFormExcel
from common.test_cases_select import testCaseSelect
import config.testCaseConfig as TCC


if __name__ == '__main__':
    testCaseSelect(
        file=TCC.FILE,
        file_type=TCC.FILE_TYPE,
        testcase_matching=TCC.TESTCASE_MATCHING,
        sheet_name=TCC.SHEET_NAME,
        isFuzzy=TCC.FUZZY,
        isAll=TCC.ALL
    )
    suit = unittest.TestSuite()
    for temp in unittest.TestLoader().getTestCaseNames(TestCaseFormExcel):
        suit.addTest(TestCaseFormExcel(temp))
    now = time.strftime('%Y-%m-%d_%H-%M-%S')
    reportname = '../reports' + '\\' + 'TestResult_' + now + '.html'
    with open(reportname, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestReport(
            stream=f,
            title='测试报告',
            description='Test the import testcase'
        ).run(suit)