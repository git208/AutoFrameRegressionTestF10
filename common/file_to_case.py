import json

import requests

from common.parse_excel import ParseExcel
from common.parse_yaml import ParseYaml
from common.form_data_format import form_data_format_body,form_data_format_header
from config.logConfig import LogCustom


class FileToCase():

    def __init__(self,file,file_type='yaml',**kwargs):
        """
            :param file: 用例所在的路径
            :param file_type: 用例所属文件类型，可以是yaml,excel
            :param case_identifier: 用例格式为excel时的用例标识，为用例ID或用例序号
            :param sheet_name: 用例格式为excel时用例所在的sheet页
            :param use_case_id: 用例格式为excel时是否使用用例ID来进行驱动，置为False将使用用例序号进行驱动，默认False
        """
        if file_type.lower() == 'yaml':
            self.handle = ParseYaml(file)
            self.testCaseName = self.handle.get_testName()
            self.url = self.handle.get_url()
            self.method = self.handle.get_method().lower() if self.handle.get_method() != None else None
            self.type = self.handle.get_type().lower() if self.handle.get_type() != None else None
            self.headers = self.handle.get_headers()
            self.params = self.handle.get_params()
            self.body = self.handle.get_body()
        elif file_type.lower() == 'excel':
            self.handle = ParseExcel(file,**kwargs)
            self.testCaseID = self.handle.get_test_case_id()
            self.testCaseName = self.handle.get_test_case_name()
            self.url = self.handle.get_url()
            self.method = self.handle.get_method().lower() if self.handle.get_method() != None else None
            self.type = self.handle.get_type().lower() if self.handle.get_type() != None else None
            self.headers = self.handle.get_headers()
            self.params = self.handle.get_params()
            self.body = self.handle.get_body()
            self.path = self.handle.get_path()
        else:
            LogCustom().logger().error('文件类型须为yaml、excel类型')

    def requests(self,environment = None):
        if environment != None:
            self.url = f'http://{environment}{self.path}'

        if self.method == 'get':
            response = requests.request(method='get',url=self.url,headers=self.headers,params=self.params)
        elif self.method == 'post':
            if self.type == 'form-data':
                if self.headers == None:
                    headers = form_data_format_header()
                else:
                    headers = self.headers.update(form_data_format_header())
                body = form_data_format_body(self.body)
                response = requests.request(method='post',url=self.url,headers=headers,data=body)

            elif self.type == 'x-www-form-urlencoded':
                headers = {'Content-Type':'application/x-www-form-urlencoded'}
                if self.headers == None:
                    headers = headers
                else:
                    headers = self.headers.update(headers)
                response = requests.request(method='post', url=self.url, headers=headers, data=self.body)

            elif self.type == 'json':
                headers = {'Content-Type': 'application/json'}
                if self.headers == None:
                    headers = headers
                else:
                    headers = self.headers.update(headers)
                response = requests.request(method='post', url=self.url, headers=headers, json=self.body)
            elif self.type == 'text':
                headers = {'Content-Type': 'text/plain'}
                if self.headers == None:
                    headers = headers
                else:
                    headers = self.headers.update(headers)
                response = requests.request(method='post', url=self.url, headers=headers, json=self.body)
            elif self.type == 'javascript':
                headers = {'Content-Type': 'application/javascript'}
                if self.headers == None:
                    headers = headers
                else:
                    headers = self.headers.update(headers)
                response = requests.request(method='post', url=self.url, headers=headers, json=self.body)
            elif self.type == 'html':
                headers = {'Content-Type': 'text/html'}
                if self.headers == None:
                    headers = headers
                else:
                    headers = self.headers.update(headers)
                response = requests.request(method='post', url=self.url, headers=headers, json=self.body)
            elif self.type == 'xml':
                headers = {'Content-Type': 'application/xml'}
                if self.headers == None:
                    headers = headers
                else:
                    headers = self.headers.update(headers)
                response = requests.request(method='post', url=self.url, headers=headers, json=self.body)
            else:
                LogCustom().logger().error(f'用例[{self.testCaseName}]请求内容类型有误，请检查用例')
                response = None
        else:
            LogCustom().logger().error(f'用例[{self.testCaseName}]请求方式有误，请检查用例')
            response = None
        return response


if __name__ == '__main__':
    # def kkkk(aaa,bbb,ccc):
    #     print(aaa)
    #     print(bbb)
    #     print(ccc)
    # def jiji(**dsdds):
    #     kkkk(**dsdds)
    #
    # jiji(aaa='dasd',bbb='fdsss',ccc="dwff")
    # class tree:
    #     high = 12
    #     age = 23
    #
    #     def ddddddd(self):
    #         print('创建了一次对象！')
    #         self.dsds = 'zhubaoping'
    #         self.fjfjf = 90
    #         self.febb = [10,23,56,'dad']
    #
    #     def inter11(ww):
    #         print(ww.dsds,ww.fjfjf,ww.febb)
    #
    # ioooo = tree()
    # ioooo.ddddddd()
    # ioooo.dsds = 'ssss'
    # ioooo.fjfjf = 'aaaaa'
    # ioooo.febb = 'fffff'
    # ioooo.inter11()
    # ioooo.dsds = 'ssss'
    # ioooo.fjfjf = 'aaaaa'
    # ioooo.febb = 'fffff'
    # ioooo.inter11()
    # print(tree.high)
    # io = tree()
    # io.inter11()
    class Chinese:
        def __init__(self,a,b):
            self.area1=a
            self.area2=b
        def inter(self):
            print('中国：',self.area1,self.area2)

    class US:
        def __init__(self,a,b,name):
            self.area11=a
            self.area22=b
            self.name=name
        def inter(self):
            print(self.name,'：',self.area11,self.area22)

    class Earth(US,Chinese):
        def inter(self):
            super(US, self).inter()
        # def __init__(self):
        pass
    io=Earth(Chinese,US,'n')
    io.area2='jjjjj'
    io.area1='sssss'
    io.inter()
    print(io.area2)





