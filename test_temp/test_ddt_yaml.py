import json
import unittest

from ddt import ddt,unpack,file_data,data
from common.yaml_RW import YamlRW

@ddt()
class tttttt(unittest.TestCase):
    # open('./source/testCaseDriver.json')

    @file_data('yyy.yaml')
    @unpack
    def test_01(self,data):
        print(data)

if __name__ == '__main__':
    unittest.main()

#     data = [
# 	["最新指标", "newindex_2"],
# 	["最新指标", "newindex_3"],
# 	["最新指标", "newindex_4"],
# 	["最新指标", "newindex_5"],
# 	["最新指标", "newindex_6"],
# 	["最新指标", "newindex_7"],
# 	["最新指标", "newindex_8"],
# 	["最新指标", "newindex_9"],
# 	["最新指标", "newindex_10"]
# ]
#     YamlRW('yyy.yaml').wightYaml(data)