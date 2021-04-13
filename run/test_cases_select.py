import json
import os

from config.logConfig import LogCustom,logging
from public.parse_excel import ParseExcel
from test_case.test_cases_driver import TestCaseFormExcel,TestCaseFormYaml

file= '../test_case/excels/接口.xlsx'
file_type = 'yaml'
isFuzzy = True
isAll = True
testcase_matching = ['01']

def testCaseSelect(file,file_type='excel',testcase_matching=None,isFuzzy=False,isAll=False):
    print('开始创建用例执行列表')
    with open('../source/testCaseDriver.json', mode='w', encoding='utf-8') as a:
        if isAll == False:
            if isFuzzy == False:
                a.write(json.dumps(testcase_matching, ensure_ascii=False, indent=2))
            else:
                temp_list = []
                if file_type.lower() == 'yaml':
                    for _ in os.listdir('../test_case/yamls'):
                        __: str
                        for __ in testcase_matching:
                            if __ in _:
                                temp_list.append(_)
                elif file_type.lower() == 'excel':
                    for _ in [i for i in ParseExcel(file).get_excel()[1].keys()]:
                        for __ in testcase_matching:
                            if __ in _:
                                temp_list.append(_)
                else:
                    LogCustom().logger().error('文件类型非yaml、excel，创建用例执行列表失败')

                a.write(json.dumps(temp_list, ensure_ascii=False, indent=2))
        else:
            if file_type.lower() == 'yaml':
                a.write(json.dumps(os.listdir('../test_case/yamls'), ensure_ascii=False, indent=2))
            elif file_type.lower() == 'excel':
                a.write(json.dumps([i for i in ParseExcel(file).get_excel()[1].keys()], ensure_ascii=False, indent=2))

if __name__ == '__main__':
    testCaseSelect(file,testcase_matching=testcase_matching,isFuzzy=isFuzzy)
    with open('../source/testCaseDriver.json',mode='r',encoding='utf-8') as a:
        print(a.read())