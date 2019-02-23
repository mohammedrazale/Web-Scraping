# -*- coding: utf-8 -*-
import scrapy
import time
import numpy as np



class Realestate1(scrapy.Spider):
    name = 'realestate1'
    mylist=[]
    allowed_domains = ["www.99acres.com"]
    start_urls = ['https://www.99acres.com/property-in-bangalore-ffid-1'] #you can just replace the locations in this url for different places or put a list of places and just iterate through it
    
    def parse(self,response):
        time.sleep(np.random.randint(1,10))#sleep the code to avoid block user by server.you can set it also in settings.py
        location=response.xpath("//th[contains(@class,'_srpttl')]//span/b/text()").extract()
        name=response.xpath("//td/a[contains(@class,'sName')]//b/text()").extract() 
        status=response.xpath("//tr//td[contains(@class,'_auto_possesionLabel')]/text()").extract()
        description=response.xpath('//th[contains(@class,"_srpttl")]/a/span/text()').extract()
        BHK=response.xpath("//td[contains(@class,'_auto_bedroom')]/b/text()").extract() 
        posted_date=response.xpath("//span[contains(@class,'srpNw_dlrNme')]/text()").extract()  
        prize= response.xpath('//span[contains(@class,"srpNw_price ")]/text()').extract()
        prizepersqft=response.xpath("//td[contains(@class,'_auto_ppu_area')]/text()").extract()
        area=response.xpath('//td[contains(@class,"_auto_areaValue")]/b/text()').extract()
        areatype=response.xpath("//td[contains(@class,'_auto_areaType')]/text()").extract() 
        developer=response.xpath('//span[contains(@class,"srpNw_dlrNme")]/a/text()').extract()
        bath_and_balcony=response.xpath("//tr//td[contains(@class,'_auto_bath_balc_roadText')]/text()").extract()
        image_url=response.xpath("//div[contains(@class,'srpNw_img')]/a/img/@src").extract()
        about=response.xpath("//div[contains(@class,'__srpNw_desc')]/text()").extract()
      
  
        
        for i in  zip(location,name,status,description,BHK,posted_date,prize,prizepersqft,area,areatype,developer,bath_and_balcony,image_url,about):
            info={'location':i[0],'name':i[1],'status':i[2],'description':i[3],'BHK':i[4],'posted_date':i[5],'prize':i[6],'prizepersqft':i[7],'area':i[8],'areatype':i[9],'developer':i[10],'bath_and_balcony':i[11],'image_url':i[12],'about':i[13]}
            yield info
                  
                  
                  
                  
                  
        #To iterate through next pages.       
        next_pageCheck = response.xpath('//div[contains(@class,"pgdiv")]/a[contains(@class,"pgselActive")]').extract()
        if next_pageCheck is not None:
            next_page = response.xpath('//div[contains(@class,"pgdiv")]/a[contains(@class,"pgselActive")]/@href').extract()[-1]
            yield response.follow(next_page, callback=self.parse)
    
