import json

import yaml

class YamlRW():
    def __init__(self,file):
        self.file = file

    def readYaml(self):
        with open(self.file,mode='r',encoding='utf-8') as a:
            return yaml.load(a.read(),Loader=yaml.FullLoader)

    def wightYaml(self,data):
        with open(self.file,mode='w',encoding='utf-8') as a:
            yaml.dump(data,stream=a,allow_unicode=True)


# if __name__ == '__main__':
    # YamlAnalysis('../yamls/djaisj.yaml').wightYaml([{'等会': '等级分iu', 'dajhiuhis': 'dasjuhiu'}, ['fds,gfd', 'dasfds', 'fggfg', 5454]])
    # print(json.dumps(YamlAnalysis('../yamls/stocknewslist.yaml').readYaml(), ensure_ascii=False, indent=2))