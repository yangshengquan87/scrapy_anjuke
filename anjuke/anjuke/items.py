# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnjukeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    address = scrapy.Field()    #地址
    name = scrapy.Field()   #小区名称
    type_ = scrapy.Field()  #类型，3室/4室
    tags = scrapy.Field()   #近学校，近地铁
    price = scrapy.Field()  #价格
    area = scrapy.Field()   #面积


