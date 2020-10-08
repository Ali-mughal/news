from scrapy.spiders import Spider
# import scrapy
import schedule
import time
import json

class KhaleejSpider(Spider):
    #spider name
    name = 'khaleej'
    allowed_domains = ['khaleejtimes.com']
    start_urls = ['http://khaleejtimes.com']
    
    def parse(self,response):
        list1=[]
        all_urls = response.css('a::attr(href)').getall()
        list1 = response.urljoin(url) for url in all_urls if 'javascript' not in url
        with open('/home/ali-mughal/projects/news/news/list1.json') as f:
        data = json.load(f)

        # yield{
        #         'list':[response.urljoin(url) for url in all_urls if 'javascript' not in url]
                
        #         }
       
        