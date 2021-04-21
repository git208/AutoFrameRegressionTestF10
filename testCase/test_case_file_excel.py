import json
import unittest

from ddt import ddt, file_data, unpack

from common.file_to_case import FileToCase
from config.testCaseConfig import USE_CASE_ID,ALL,FILE,FILE_TYPE

if ALL == True:
    USE_CASE_ID = True

ENVIRONMENT1 = '114.80.155.57:22013'
ENVIRONMENT2 = '58.63.252.23:22013'

@ddt
class TestCaseFormExcel(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.case = FileToCase(
            file=FILE,
            file_type=FILE_TYPE,
            use_case_id=USE_CASE_ID
        )

    @file_data('../source/testCaseDriver.json')
    # @unpack
    def test_01(self, case):
        # print(case)
        self.case.select_test(case[0],case[1])
        print(self.case.testCaseName+'\n')
        response1 = self.case.requests(ENVIRONMENT1)

        response2 = self.case.requests(ENVIRONMENT2)


        print(ENVIRONMENT1 + '\n' + json.dumps(response1.json(), ensure_ascii=False, indent=2))
        print(ENVIRONMENT2 + '\n' + json.dumps(response2.json(), ensure_ascii=False, indent=2))
        self.assertEqual(response1.json(),response2.json())



    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()