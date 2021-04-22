import json
import unittest

from ddt import ddt,unpack,file_data,data
from common.yaml_RW import YamlRW

@ddt()
class tttttt(unittest.TestCase):
    # open('./source/testCaseDriver.json')

    @file_data('yyy.yaml')
    # @unpack
    def test_01(self,data):
        print(data)

    def tearDown(self) -> None:
        print('成功了')
if __name__ == '__main__':
    # unittest.main()

    print('doc11' and '大事' or 'name11')