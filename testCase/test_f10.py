import json
import unittest

from common import HTMLTestRunner
from ddt import ddt, file_data, unpack

from common.file_to_case import FileToCase
from config.testCaseConfig import USE_CASE_ID

@ddt
class TestCaseFormExcel(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @file_data('../source/testCaseDriver.json')
    @unpack
    def test_01(self, case):
        print(case)
        case = FileToCase(
            file='../testCase/excels/接口.xlsx',
            file_type='excel',
            sheet_name=case[0],
            case_identifier=case[1],
            use_case_id=USE_CASE_ID
        )
        print(case.testCaseName)
        response = case.requests()
        print(json.dumps(response.json(), ensure_ascii=False, indent=2))
        pass

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    print(unittest.TestLoader().getTestCaseNames(TestCaseFormExcel))
    suit = unittest.defaultTestLoader.discover('../testCase','test*.py')
    # for temp in unittest.TestLoader().getTestCaseNames(TestCaseFormExcel):
    #     suit.addTest(TestCaseFormExcel(temp))
    with open('../reports/dasdada.html', mode='wb') as a:
        HTMLTestRunner.HTMLTestReport(stream=a, title='溜冰的测试报告', description='huhuxbaasd', tester='Liu Bin').run(suit)