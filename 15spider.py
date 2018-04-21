#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# 3.30 作业 爬月光博客

import scrapy

class BlogSpider(scrapy.Spider): 
    name = 'blogspider'
    start_urls = ['http://www.williamlong.info/'] 

    def start_requests(self):
        urls = []
        for i in range(1,3): # total page = 177
        	urls.append('http://www.williamlong.info/cat/?page=' + str(i))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response): 
    	# title

    	response.css(divMain > div:nth-child(2))
    	#divMain > div:nth-child(30)

        for title in response.css('h2.post-title'): 
        	content = 'title: '+ title.css('a ::text').extract_first()
        	print content.encode('utf-8') #Chinese unicode 
            # yield {'title': title.css('a ::text').extract_first()} 
    	
    	# body + image or category
    	for body in response.css('post-body'):
    		bodycontent = 'body: '+ title.css('a ::text').extract_first()
    		print bodycontent.encode('utf-8')
    		image = 'image' + response.css('a[href*=image]::attr(href)').extract()
    		print image
    	

 