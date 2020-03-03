import time
import json
import csv
import requests
ExcelName = 'C:/Users/Administrator/Desktop/Epidemic-data-china.csv'

#当前日期时间戳
number = format(time.time() * 100, '.0f')

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%s' % number
datas = json.loads(requests.get(url=url).json()['data'])

print('更新时间：' + datas['lastUpdateTime'])

#写入表头
with open(ExcelName, 'w', encoding='utf_8_sig', newline='') as csvfile:#utf_8_sig替换utf-8解决中文乱码问题
    writer = csv.writer(csvfile)
    writer.writerow(["记录时间", str(datas['lastUpdateTime'])])
    writer.writerow(["省份","新增确诊","累计确诊","治愈","死亡"])
    
for contry in datas['areaTree']:
    if contry['name'] == '中国':
        for province in contry['children']:
            with open(ExcelName, 'a', encoding='utf_8_sig', newline='') as csvfile:#utf_8_sig替换utf-8解决中文乱码问题
                writer = csv.writer(csvfile)
                writer.writerow([province['name'], str(province['today']['confirm']), str(province['total']['confirm']), str(province['total']['heal']), str(province['total']['dead'])])