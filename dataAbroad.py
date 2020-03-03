import time
import json
import csv #生成.csv所需
# import codecs #中文编码所需
import requests
ExcelName = 'C:/Users/Administrator/Desktop/Epidemic-data-abroad.csv'

#当前日期时间戳
number = format(time.time() * 100, '.0f')

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%s' % number
datas = json.loads(requests.get(url=url).json()['data'])

print('更新时间：' + datas['lastUpdateTime'])

#写入表头
with open(ExcelName, 'w', encoding='utf_8_sig', newline='') as csvfile: #utf_8_sig替换utf-8解决中文乱码问题
    writer = csv.writer(csvfile)
    writer.writerow(["记录时间", str(datas['lastUpdateTime'])])
    writer.writerow(["国家","新增确诊","累计确诊","治愈","死亡"])
    
for area in datas['areaTree']:
    if area['name'] != '中国':
        with open(ExcelName, 'a', encoding='utf-8-sig', newline='') as csvfile:#utf_8_sig替换utf-8解决中文乱码问题
            # csvfile.write(codecs.BOM_UTF8)
            writer = csv.writer(csvfile)
            writer.writerow([area['name'], str(area['today']['confirm']), str(area['total']['confirm']), str(area['total']['dead']), str(area['total']['heal'])])