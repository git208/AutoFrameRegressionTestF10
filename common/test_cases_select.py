import json
import os

from config.logConfig import LogCustom,logging
from common.parse_excel import ParseExcel

def testCaseSelect(file,file_type='excel',
                   testcase_matching=None,
                   sheet_name=None,
                   isFuzzy=False,
                   isAll=False):
    """
        :param file: 用例所在的路径
        :param file_type: 用例所属文件类型，可以是yaml,excel
        :param testcase_matching:list 用例匹配关键字列表，isFuzzy为True时，根据列表中关键字模糊匹配用例，isFuzzy为False时，该参数为用例列表
        :param isFuzzy: 是否根据关键字列表进行模糊匹配
        :param isAll: 为True时执行所有用例
    """
    print('开始创建用例执行列表')
    with open('../source/testCaseDriver.json', mode='w', encoding='utf-8') as a:
        if isAll == False:
            if isFuzzy == False:
                a.write(json.dumps(testcase_matching, ensure_ascii=False, indent=2))
            else:
                temp_list = []
                if file_type.lower() == 'yaml':
                    for _ in os.listdir('../testCase/yamls'):
                        __: str
                        for __ in testcase_matching:
                            if __ in _:
                                temp_list.append(_)
                elif file_type.lower() == 'excel':
                    if type(sheet_name) == list:
                        for temp in sheet_name:
                            for _ in [i for i in ParseExcel(file,sheet_name=temp).get_excel()[1].keys()]:
                                for __ in testcase_matching:
                                    if __ in _:
                                        temp_list.append((sheet_name,_))
                    else:
                        for _ in [i for i in ParseExcel(file, sheet_name=sheet_name).get_excel()[1].keys()]:
                            for __ in testcase_matching:
                                if __ in _:
                                    temp_list.append((sheet_name, _))
                else:
                    LogCustom().logger().error('文件类型非yaml、excel，创建用例执行列表失败')

                a.write(json.dumps(temp_list, ensure_ascii=False, indent=2))
        else:
            if file_type.lower() == 'yaml':
                a.write(json.dumps(os.listdir('../testCase/yamls'), ensure_ascii=False, indent=2))
            elif file_type.lower() == 'excel':
                temp_list = []
                for _ in  ParseExcel(file).get_sheetnames():
                    for __ in ParseExcel(file,sheet_name=_).get_excel()[1].keys():
                        temp_list.append((_,__))
                a.write(json.dumps(temp_list, ensure_ascii=False, indent=2))

# if __name__ == '__main__':
#     testCaseSelect(FILE,isAll=True)
#     with open('../source/testCaseDriver.json', mode='r', encoding='utf-8') as a:
#         print(a.read())