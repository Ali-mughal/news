from scrapy.spiders import Spider
# import scrapy
import schedule
import time

class KhaleejSpider(Spider):
    #spider name
    name = 'khaleej'
    allowed_domains = ['khaleejtimes.com']
    start_urls = ['http://khaleejtimes.com']

    def parse(self,response):
        all_urls = response.css('a::attr(href)').getall()
        urls_list1 = []
        urls_list2 = []
        for all_url in all_urls:
            if  'javascript' not in all_url:
                absolute_url=response.urljoin(all_url)
                print(absolute_url)
                urls_list1.append(absolute_url)
                urls_list2.append(absolute_url)
                # yield scrapy.Request(url=url, callback=self.parse_details)
        print ("getting the length of list:",len(urls_list1))
        diff=set(urls_list1) & set(urls_list2)
        print('lsdjflsadf;l###################################################',len(diff))
        if urls_list1==urls_list2:
            print('both list are equal')

        # def parse_details(self,response):
        # yield{
        #         'name': response.css('h3.author-title::text').get(),
        #         }
        
        
    
        # yield{
        #     'absolute_allurls': [response.urljoin for all_url in all_urls if 'javascript' not in all_url]
        # }
        ## pagination link
        