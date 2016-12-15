# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class SpiderLearnPipeline(object):

    def process_item(self, item, spider):
        client = pymongo.MongoClient('localhost', 27017)
        walden = client['jingdong']
        sheet_table = walden['info']
        data = {
            'item_name' : item['item_name'],
            'item_id': item['item_id'],
            'item_weight' : item['item_weight'],
            'item_area' : item['item_area']
        }
        sheet_table.insert_one(data)
        print("==========save success!===========")
        return item



