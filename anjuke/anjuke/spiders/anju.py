# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from anjuke.items import AnjukeItem  # 使用item


class AnjuSpider(scrapy.Spider):
    name = 'anju'
    allowed_domains = ['shanghai.anjuke.com']
    start_urls = ['https://shanghai.anjuke.com/sale/baoshan/m2401/']

    def parse(self, response):
        divs = response.xpath('''//li[@class="list-item"]''')  # 使用xpath从response中获取需要的html块
        for div in divs:
            item = AnjukeItem()  # 实例化item对象
            address = div.xpath('.//span[@class="comm-address"]/@title').extract_first()  # 楼盘地址和小区名称，由于地址和小区名称在一起，所以下面是拆分
            address1 = address[address.index("\xa0\xa0") + 2 :]  #地址，以“\xa0\xa0”区分,结果：宝山-大华-真北路4333弄
            address2 = address1[address1.index("-") + 1 :]  #第一次以“-”分隔，结果：大华-真北路4333弄
            address3 = address2[address2.index("-") + 1 :]  #第二次以“-”分隔，结果：真北路4333弄

            name1 = address[:address.index("\xa0\xa0")]  #小区名称
            try:
                type_1 = div.xpath('.//div[@class="details-item"]/span/text()').extract_first()  # 房子类型比如两房一厅这样子~
            except:
                pass

            # item['tags'] = div.xpath('.//span[@class="item-tags tag-metro"]/text()').extract()  # 网站给楼盘定的标签~

            price = div.xpath('.//span[@class="price-det"]/strong/text()').extract_first()  # 价格
            price1 = price + '万'
            try:
                area = div.xpath('.//div[@class="details-item"]/span/text()').extract()[1:2]
                area1 = ''.join(area)   #将list转化为string
            except:
                pass

            item['address'] = address3
            item['name'] = name1
            item['type_'] = type_1
            item['price'] = price1
            item['area'] = area1

            yield item
            
        next_ = response.xpath('//div[@class="multi-page"]/a[@class="aNxt"]/@href').extract_first()  # 获取下一页的链接
        print('-------next----------')
        print(next_)
        yield response.follow(url=next_, callback=self.parse)  # 将下一页的链接加入爬取队列~~


    