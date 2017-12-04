import scrapy
import time
import csv
from scrapy.http import Request 
from stockSpider.items import StockspiderItem 

class StockSpider(scrapy.Spider):
    name = "stockSpider"
    allow_domain = "http://data.10jqka.com.cn/funds/hyzjl/"
    start_urls = ["http://data.10jqka.com.cn/funds/hyzjl/#refCountId=data_55f13c2c_254"]
    next_page = None
    def parse(self,response):
        localtime = time.localtime()
        cur_time = time.strftime("%Y-%m-%d %H:%M", localtime)
        tr_list = response.xpath('//*[@class="m-table J-ajax-table"]/tbody/tr')
        for sel in tr_list:
            item = StockspiderItem()
            item['time'] = cur_time
            item['industry'] = sel.xpath("./td[2]/a/text()").extract()[0].encode('utf-8')
            item['industry_idx'] = sel.xpath("./td[3]/text()").extract()[0]
            item['chg'] = sel.xpath("./td[4]/text()").extract()[0]
            item['money_in'] = sel.xpath("./td[5]/text()").extract()[0]
            item['money_out'] = sel.xpath("./td[6]/text()").extract()[0]
            item['net'] = sel.xpath("./td[7]/text()").extract()[0]
            item['company_count'] = sel.xpath("./td[8]/text()").extract()[0]
            item['lead_stock'] = sel.xpath("./td[9]/a/text()").extract()[0].encode('utf-8')
            item['lead_chg'] = sel.xpath("./td[10]/text()").extract()[0]
            item['cur_price'] = sel.xpath("./td[11]/text()").extract()[0]
            yield item
        if self.next_page == None:
            self.next_page = "http://data.10jqka.com.cn/funds/hyzjl/field/tradezdf/order/desc/page/2/ajax/1/"
            yield Request(self.next_page, callback=self.parse)




            