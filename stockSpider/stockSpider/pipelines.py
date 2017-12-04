# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os
import time

class StockspiderPipeline(object):
    path = 'D:/work_documents/vikky_projects/python_project/stock_project/stockSpider/stock_data/'
        
    def process_item(self, item, spider):
        file_list = os.listdir(self.path)
        print("*******************文件夹**********************",file_list)
        if (len(file_list)>0):
            if (os.path.getsize(self.path+file_list[-1])//(1024*1024))< 10:
                """
                    继续写入
                """
                self.file = open(self.path+file_list[-1],'a', newline='')
            else:
                """
                    新建文件
                """
                file_date = time.strftime("%Y%m%d", time.localtime())
                new_file = 'stock_flow_'+file_date+'.csv'
                self.file = open(self.path+new_file,'a', newline='')
                writer = csv.writer(self.file)
                writer.writerow(['时间','行业','行业指数','涨跌幅','流入资金(亿)',
                                 '流出资金(亿)','净额(亿)','公司家数','领涨股',
                                 '领涨股涨跌幅','领涨股当前价(元)'])
        else:
            """
                新建文件
            """
            file_date = time.strftime("%Y%m%d", time.localtime())
            new_file = 'stock_flow_'+file_date+'.csv'
            self.file = open(self.path+new_file,'a', newline='')
            writer = csv.writer(self.file)
            writer.writerow(['时间','行业','行业指数','涨跌幅','流入资金(亿)',
                                '流出资金(亿)','净额(亿)','公司家数','领涨股',
                                '领涨股涨跌幅','领涨股当前价(元)'])
        writer = csv.writer(self.file)
        writer.writerow([item['time'],item['industry'].decode('utf-8'),item['industry_idx'],item['chg'],
                        item['money_in'],item['money_out'],item['net'],item['company_count'],
                        item['lead_stock'].decode('utf-8'),item['lead_chg'],item['cur_price']])
        self.file.close() #一定要关闭csv，不然写入的文件不会保存
        return item

