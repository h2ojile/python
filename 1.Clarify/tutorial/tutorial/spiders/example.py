# -*- coding: utf-8 -*-
import scrapy
import json
from tutorial.items import TutorialItem

class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["lagou.com"]
    start_urls = json.load(file('../allUrl.json'))
    # start_urls = json.load(file('../Url.json'))

    def parse(self, response):
        # filename = response.url.split("/").pop().split('?')[0]
        # print filename
        # f=open(filename, 'wb')
        # f.write(response.body)
        # f.close()
        
        item= TutorialItem()
        item['url']=response.url
        
        item['title']=''.join(response.css('.job_detail dt h1').xpath('text()').extract()).strip()    
        item['salary']=''.join(response.css('.job_request .red').xpath('text()').extract()).strip()    
        item['city']=''.join(response.css('.job_request span:nth-child(2)').xpath('text()').extract()).strip()    
        item['experience']=''.join(response.css('.job_request span:nth-child(3)').xpath('text()').extract()).strip()    
        item['education']=''.join(response.css('.job_request span:nth-child(4)').xpath('text()').extract()).strip()    
        item['employment']=''.join(response.css('.job_request span:nth-child(5)').xpath('text()').extract()).strip()    
        item['points']=''.join(response.css('.job_request').xpath('text()').extract()).strip()    
        item['description']=''.join(response.css('.job_bt *').xpath('text()').extract()).strip()    
        item['logo']=''.join(response.css('.job_company   > dt > a > img').xpath('@src').extract()).strip()    
        item['domain']=''.join(response.css('.job_company .c_feature:nth-child(1) li:nth-child(1)').xpath('text()').extract()).strip()    
        item['scale']=''.join(response.css('.job_company .c_feature:nth-child(1) li:nth-child(2)').xpath('text()').extract()).strip()    
        item['web']=''.join(response.css('.job_company  ul:nth-child(1) > li:nth-child(3) > a').xpath('text()').extract()).strip()    
        item['stage']=''.join(response.css('.job_company > dd > ul:nth-child(3) > li ').xpath('text()').extract()).strip()    
        item['address']=''.join(response.css('.job_company  div').xpath('text()').extract()).strip()    
        item['company']=''.join(response.css('.job_company   > dt > a > img').xpath('@alt').extract()).strip()    
 
		
        return item
        #''.join(response.css('.job_bt')
        #''.join(response.css('.job_company')
        
