# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.exceptions import DropItem

class NewsPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['news_db']
        self.collection = db['urls_tb']
    def process_item(self, item, spider):
        for url in item['url']:
            self.collection.insert(dict({'url_key':url}))
            # self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        return item