import json
import requests


def stockReturn(market,page):
    li = []
    header = {
        'Symbol':f'{market}',
        'Param':f'{page},100,7,1,1',
        'token':'MitakeWeb'
    }
    response = requests.request('get','http://114.80.155.134:22016/v4/catesorting',headers=header)


    for _ in response.text.split(''):
        if len(_.split('')) >=2:
            li.append(_.split('')[1])
        # print(json.dumps(_.split('')[1],ensure_ascii=False,indent=2))

    print(li)


if __name__ == '__main__':
    stockReturn('SH1001',0)
# for _ in li:
#     header1 = {
#         'Symbol':f'{_}',
#         'src':'d',
#         'token':'MitakeWeb'
#     }
#     response = requests.request('get','http://58.63.252.23:22013/v2/fndclassmergesplit',headers=header1)
#     print(response.json(),'aaaa')