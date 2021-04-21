import json
import os
import time


from common import HTMLTestRunner

from common.test_cases_select import testCaseSelect
import config.testCaseConfig as TCC
from testCase.test_case_file_excel import TestCaseFormExcel,unittest


if __name__ == '__main__':
    testCaseSelect(
        file=TCC.FILE,
        file_type=TCC.FILE_TYPE,
        testcase_matching=TCC.TESTCASE_MATCHING,
        sheet_names=TCC.SHEET_NAME,
        isFuzzy=TCC.FUZZY,
        isAll=TCC.ALL
    )
    suit = unittest.TestSuite()
    # suit = unittest.defaultTestLoader.discover('')
    for temp in unittest.TestLoader().getTestCaseNames(TestCaseFormExcel):
        suit.addTest(TestCaseFormExcel(temp))

    now = time.strftime('%Y-%m-%d_%H-%M-%S')
    reportname = '../reports/TestResult_' + now + '.html'
    with open(reportname, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestReport(
            stream=f,
            title='测试报告',
            description='Test the import testcase'
        ).run(suit)