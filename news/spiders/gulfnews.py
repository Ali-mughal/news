from scrapy.spiders import Spider
import scrapy
import schedule
import time

class GulfnewsSpider(Spider):
    #spider name
    name = 'gulfnews'
    allowed_domains = ['gulfnews.com']
    start_urls = ['https://gulfnews.com']

    def parse(self,response):
        urls = response.css('a::attr(href)').getall()
        for url in urls:
            if 'javascript' not in url:
                absolute_url=response.urljoin(url)
                print(url)

