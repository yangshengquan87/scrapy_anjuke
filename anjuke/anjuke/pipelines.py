# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class AnjukePipeline(object):
#     def process_item(self, item, spider):
#         return item

import pymysql

class AnjukePipeline(object):
    def __init__(self):
        # 连接MySQL数据库
        self.connect=pymysql.connect(host='47.101.54.26',user='root',password='2018xysm',db='scrapy',port=3306)
        self.cursor=self.connect.cursor()
    def process_item(self, item, spider):
        # 往数据库里面写入数据
        self.cursor.execute('insert into anjuke(address,name,type_,area,price)VALUES ("{}","{}","{}","{}","{}")'.format(item['address'],item['name'],item['type_'],item['area'],item['price']))
        self.connect.commit()
        return item
    # 关闭数据库
    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()
