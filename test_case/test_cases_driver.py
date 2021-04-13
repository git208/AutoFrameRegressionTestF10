import json
import os
import unittest

import HTMLTestRunner
from ddt import ddt, file_data, unpack

from public.file_to_case import FileToCase

file='excels/接口.xlsx'
file_type='excel'
sheet_name=None

@ddt
class TestCaseFormExcel(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @file_data('../source/testCaseDriver.json')
    @unpack
    def test_01(self, case_identifier):
        print(case_identifier)
        case = FileToCase(file=file,
                          file_type=file_type,
                          case_identifier=case_identifier,
                          use_case_id=True
                          )
        print(case.testCaseName)
        response = case.requests()
        print(json.dumps(response.json(), ensure_ascii=False, indent=2))
        pass

    def tearDown(self) -> None:
        pass

@ddt
class TestCaseFormYaml(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @file_data('../source/testCaseDriver.json')
    @unpack
    def test_01(self,yaml_file):
        case = FileToCase(file=f'../test_case/yamls/{yaml_file}',
                          file_type='yaml')
        print(case.testCaseName)
        response = case.requests()
        # print(json.dumps(response.json(),ensure_ascii=False,indent=2))
        print(json.dumps(response.json(), ensure_ascii=False, indent=2))
        pass

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    print(unittest.TestLoader().getTestCaseNames(TestCaseFormYaml))
    suit = unittest.TestSuite()
    for temp in unittest.TestLoader().getTestCaseNames(TestCaseFormYaml):
        suit.addTest(TestCaseFormYaml(temp))
    with open('../reports/dasdada.html',mode='wb') as a:
        HTMLTestRunner.HTMLTestReport(stream=a, title='溜冰的测试报告',description='huhuxbaasd').run(suit)