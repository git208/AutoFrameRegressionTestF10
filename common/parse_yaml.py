from common.yaml_RW import YamlRW

class ParseYaml():
    def __init__(self, yaml_file):
        self.data = YamlRW(yaml_file).readYaml()

    def data_process(self,key):
        if key in self.data['teststeps']['request'].keys():
            if self.data['teststeps']['request'][key] == "":
                return None
            else:
                return self.data['teststeps']['request'][key]
        else:
            return None

    def get_testName(self):
        if 'name' in self.data['config'].keys():
            if self.data['config']['name'] == "":
                return None
            else:
                return self.data['config']['name']
        else:
            return None

    def get_url(self):
        return self.data_process('url')

    def get_method(self):
        return self.data_process('method')

    def get_type(self):
        return self.data_process('body_type')

    def get_headers(self):
        return self.data_process('headers')

    def get_params(self):
        return self.data_process('params')

    def get_body(self):
        return self.data_process('body')


if __name__ == '__main__':
    sad = ParseYaml('../testCase/yamls/stockbulletinlist.yaml').get_body()
    print(sad)