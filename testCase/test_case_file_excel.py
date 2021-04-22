import json
import unittest

from ddt import ddt, file_data, unpack
from config.logConfig import LogCustom
from common.file_to_case import FileToCase
from config.testCaseConfig import USE_CASE_ID,ALL,FILE,FILE_TYPE,ENVIRONMENT1,ENVIRONMENT2

if ALL == True:
    USE_CASE_ID = True


@ddt
class TestCaseFormExcel(unittest.TestCase):

    def delH(self,h):
        del h['User-Agent']
        del h['Accept-Encoding']
        del h['Connection']
        del h['Accept']
        return h

    @classmethod
    def setUpClass(cls) -> None:
        cls.case = FileToCase(
            file=FILE,
            file_type=FILE_TYPE,
            use_case_id=USE_CASE_ID
        )

    @file_data('../source/testCaseDriver.yaml')
    # @unpack
    def test_01(self, case):
        # print(case)
        self.case.select_test(case[0],case[1])
        print(self.case.testCaseName+'\n')

        response1 = self.case.requests(ENVIRONMENT1)
        print(
            f'请求头:{self.delH(response1.request.headers)}\n接口返回:{json.dumps(response1.json(), ensure_ascii=False, indent=2)}\n')

        response2 = self.case.requests(ENVIRONMENT2)
        print(
            f'请求头:{self.delH(response2.request.headers)}\n接口返回:{json.dumps(response2.json(), ensure_ascii=False, indent=2)}\n')

        self.assertEqual(response1.json(),response2.json())



    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()