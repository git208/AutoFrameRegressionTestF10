'''
需要执行的用例在此页面配置
'''


#测试用例文件的路径，可以是相对路径或绝对路径
FILE= '../testCase/excels/接口.xlsx'

#用例文件类型，该框架中支持yaml、excel两种
FILE_TYPE = 'yaml'

#用例文件类型为excel时此参数有效，此参数为用例所在sheet页,当需要在多个sheet中匹配时，可传入sheetName列表
SHEET_NAME = None

'''
测试用例匹配项，与 FUZZY 参数搭配使用；

当 FUZZY 为 True 时，将根据该参数列表中的所有关键字模糊匹配用例；
示例：TESTCASE_MATCHING = ['01','GG']，将根据'01'和'GG'去模糊匹配数据

当 FUZZY 为 False 时，该参数列表中数据将作为用例驱动标识列表；
示例：TESTCASE_MATCHING = [(<sheetname>,<用例标识>),(<sheetname>,<用例标识>),...]

'''
TESTCASE_MATCHING = ['01']

#是否进行模糊匹配
FUZZY = True

#为True时执行文件中所有用例
ALL = True

#用例文件为excel时此参数有效，为False时，使用excel行序号作为用例标识，为True时，使用用例ID作为用例标识
USE_CASE_ID = False