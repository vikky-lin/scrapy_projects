# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 时间点
    time = scrapy.Field()
    # 行业
    industry = scrapy.Field()
    # 行业指数
    industry_idx = scrapy.Field()
    #涨跌幅
    chg = scrapy.Field()
    # 资金流入
    money_in = scrapy.Field()
    #资金流出
    money_out = scrapy.Field()
    #净额
    net = scrapy.Field()
    #公司数
    company_count = scrapy.Field()
    #领涨股
    lead_stock = scrapy.Field()
    #领涨股涨跌幅
    lead_chg = scrapy.Field()
    #当前价
    cur_price = scrapy.Field()
