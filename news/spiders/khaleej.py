from scrapy.spiders import Spider
# import scrapy
import schedule
import time
from news.items import NewsItem

class KhaleejSpider(Spider):
    #spider name
    name = 'khaleej'
    allowed_domains = ['khaleejtimes.com']
    start_urls = ['http://khaleejtimes.com']

    def parse(self,response):
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