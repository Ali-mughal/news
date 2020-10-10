from scrapy.spiders import Spider
# import scrapy
import schedule
import time
from news.items import NewsItem
import pymongo

class KhaleejSpider(Spider):
    #spider name
    name = 'khaleej'
    allowed_domains = ['khaleejtimes.com']
    start_urls = ['http://khaleejtimes.com']
    def __init__(self):
        self.db = pymongo.MongoClient(
            'localhost',
            27017
        )
        self.urlkey=self.db.news_db.collection.find()
        
    def parse(self,response):
        for url in self.urlkey:
            print('fetching urls',url)
        all_urls = response.css('a::attr(href)').getall()
        urls_list = []
        for all_url in all_urls:
            if  'javascript' not in all_url:
                absolute_url=response.urljoin(all_url)
                urls_list.append(absolute_url)
             

        item=NewsItem()
        item['url']=list(set(urls_list))
        yield item
        # print(absolute_url)
            
        print(len(urls_list))
       