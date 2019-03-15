# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CaipiaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    num = scrapy.Field()
    qiuH1 = scrapy.Field()
    qiuH2 = scrapy.Field()
    qiuH3 = scrapy.Field()
    qiuH4 = scrapy.Field()
    qiuH5 = scrapy.Field()
    qiuH6 = scrapy.Field()
    qiuH7 = scrapy.Field()
    qiuL = scrapy.Field()
    pass
