import time
from datetime import datetime
import os

timeline = [
    '9:30',
    '9:35',
    '9:40',
    '9:45',
    '9:50',
    '9:55',
    '10:00',
    '10:05',
    '10:10',
    '10:15',
    '10:20',
    '10:25',
    '10:30',
    '10:35',
    '10:40',
    '10:45',
    '10:50',
    '10:55',
    '11:00',
    '11:05',
    '11:10',
    '11:15',
    '11:20',
    '11:25',
    '11:30',
    '11:35',
    '11:40',
    '11:45',
    '11:50',
    '11:55',
    '12:00',
    '13:00',
    '13:05',
    '13:10',
    '13:15',
    '13:20',
    '13:25',
    '13:30',
    '13:35',
    '13:40',
    '13:45',
    '13:50',
    '13:55',
    '14:00',
    '14:05',
    '14:10',
    '14:15',
    '14:20',
    '14:25',
    '14:30',
    '14:35',
    '14:40',
    '14:45',
    '14:50',
    '14:55',
    '15:00'
]
while 1:
    cur_time = datetime.now().strftime('%H:%M')
    week_day = datetime.now().isoweekday()
    print("当前时间为",cur_time)
    if week_day >=1 & week_day <=5:
        if cur_time in timeline:
            os.system('d:&cd d://work_documents/vikky_projects/python_project/stock_project/stockSpider&scrapy crawl stockSpider')
            time.sleep(60*4)
        elif ((cur_time<='08:10') | (cur_time>'15:10')):
            print("不在时间点范围,间息1hour")
            time.sleep(60*60)
        else:
            print("不在时间点范围,间息30second")
            time.sleep(30)
