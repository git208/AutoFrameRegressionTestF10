import json
import os

from common.yaml_RW import YamlRW
from config.logConfig import LogCustom,logging
from common.parse_excel import ParseExcel

def testCaseSelect(file,file_type='excel',
                   testcase_matching=None,
                   sheet_names=None,
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
    ym = YamlRW('../source/testCaseDriver.yaml')
    if isAll == False:
        if isFuzzy == False:
            ym.wightYaml(testcase_matching)
        else:
            temp_list = []
            if file_type.lower() == 'yaml':
                for _ in os.listdir('../testCase/yamls'):
                    __: str
                    for __ in testcase_matching:
                        if __ in _:
                            temp_list.append(_)

            elif file_type.lower() == 'excel':
                excel = ParseExcel(file)
                excel.get_excel_new()
                if sheet_names != None:
                    if type(sheet_names) == list:
                        for sheet_name in sheet_names:
                            for _ in excel.excel_data[sheet_name][1].keys:
                                temp_list.append((sheet_name,_))
                    else:
                        for _ in excel.excel_data[sheet_names][1].keys:
                            temp_list.append((sheet_names, _))
                else:
                    for sheet_name in testcase_matching.keys():
                        for __ in excel.excel_data[sheet_name][1].keys:
                            for _ in testcase_matching[sheet_name]:
                                if __ in _:
                                    temp_list.append((sheet_name, _))

            else:
                LogCustom().logger().error('文件类型非yaml、excel，创建用例执行列表失败')

            ym.wightYaml(temp_list)
    else:
        if file_type.lower() == 'yaml':
            ym.wightYaml(os.listdir('../testCase/yamls'))
        elif file_type.lower() == 'excel':
            temp_list = []
            excel = ParseExcel(file)
            excel.get_excel_new()
            i = 0
            A = excel.excel_data.keys()
            for _ in A:
                i += 1
                j = 0
                B = excel.excel_data[_][1].keys()
                for __ in B:
                    j += 1
                    temp_list.append([_,__])
                    print(f'总共{len(A)}个接口,当前为第{i}个接口，总共包含{len(B)}条用例,选择至第{j}条用例，数据{(_,__)}')
            ym.wightYaml(temp_list)

# if __name__ == '__main__':
#     testCaseSelect(FILE,isAll=True)
#     with open('../source/testCaseDriver.json', mode='r', encoding='utf-8') as a:
#         print(a.read())