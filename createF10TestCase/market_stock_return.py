import json
import requests
from config.logConfig import LogCustom,logging
from config.testCaseConfig import ENVIRONMENT3,MAX_BOUNDS,STOCK_NUMBER

# environments = [
#     'http://114.80.155.57:22013',
#     'http://114.80.155.134:22016'
# ]
haveNumPathList = [
    'finmrgninfomarket',
    'finmrgninfodiff',
    'finmrgninfoshare',
    'newsinteractive',
    'exptperformance',
    'proindicdata',
    'stocknewslist',
    'stockbulletinlist',
    'stockreportlist'
]

def stockReturn(market,page,site):
    li = []
    header = {
        'Symbol':f'{market}',
        'Param':f'{page},100,7,1,1',
        'token':'MitakeWeb'
    }

    if site == 'pb':
        response = requests.request('get','http://114.80.155.134:22016/v3/catesorting',headers=header)
    elif site == 'hk':
        response = requests.request('get','http://114.80.155.133:22016/v3/catesorting',headers=header)
    else:
        response = requests.request('get','http://114.80.155.134:22016/v3/catesorting',headers=header)

    for _ in response.text.split(''):
        if len(_.split('')) >=2:
            li.append(_.split('')[1])
        # print(json.dumps(_.split('')[1],ensure_ascii=False,indent=2))
    return li
    # print(li)

def availableStock(path,headers,key,maket,site):
    available_stock_list = []
    i = 0
    while(1):
        stock_list = stockReturn(maket,i,site)
        # print(len(stock_list),stock_list)
        for stock in stock_list:
            print(f'正在查找{path.split("/")[-1]}下可用股票，当前测试对象：maket：{maket}，stock：{stock}')
            he = json.loads(headers)
            he.update({key:stock})
            try:
                response = requests.request('get','http://'+ENVIRONMENT3+path,headers=he)
            except:
                LogCustom().logger().error('生成用例时验证数据出错')
            else:
                if path.split('/')[-1] in haveNumPathList:
                    try:
                        if response.json()['List'] != []:
                            available_stock_list.append({key:stock})
                    except:
                        pass
                else:
                    try:
                        if response.json() != {} and response.json() != []:
                            available_stock_list.append({key: stock})
                    except:
                        pass
                if len(available_stock_list) >= STOCK_NUMBER:
                    return available_stock_list
        if i>=MAX_BOUNDS/100-1:
            return available_stock_list
        i+=1
        if len(stock_list)<100:
            return available_stock_list

if __name__ == '__main__':
    # print(stockReturn('SH1110',0,'pb'))
    availableStock('/v2/fndnavinde','{"Token":"MitakeWeb","src":"d","type":"12"}','key','SZ1110',site=None)
    # print([][-30:])
# for _ in li:
#     header1 = {
#         'Symbol':f'{_}',
#         'src':'d',
#         'token':'MitakeWeb'
#     }
#     response = requests.request('get','http://58.63.252.23:22013/v2/fndclassmergesplit',headers=header1)
#     print(response.json(),'aaaa')