from scrapy.spiders import Spider
# import scrapy

class KhaleejSpider(Spider):
    #spider name
    name = 'khaleej'
    allowed_domains = ['khaleejtimes.com']
    start_urls = ['http://khaleejtimes.com']

    def parse(self,response):
        all_urls = response.css('a::attr(href)').getall()
        for all_url in all_urls:
            if  'javascript' not in all_url:
                absolute_url=response.urljoin(all_url)
                print(absolute_url)