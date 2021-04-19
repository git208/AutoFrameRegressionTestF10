import json
import unittest

from ddt import ddt, file_data, unpack

from common.file_to_case import FileToCase


@ddt
class TestCaseFormYaml(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @file_data('../source/testCaseDriver.json')
    @unpack
    def test_01(self,yaml_file):
        case = FileToCase(file=f'../testCase/yamls/{yaml_file}',
                          file_type='yaml')
        print(case.testCaseName)
        response = case.requests()
        # print(json.dumps(response.json(),ensure_ascii=False,indent=2))
        print(json.dumps(response.json(), ensure_ascii=False, indent=2))
        pass

    def tearDown(self) -> None:
        pass
