#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import scrapy

class BlogSpider(scrapy.Spider): #?.Spider
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com'] #开始的网址

    def parse(self, response): #查parse
        for title in response.css('h2.entry-title'): #每一个h2文本里的title extract出来
        # <h2 class="entry-title">...</h2>
            yield {'title': title.css('a ::text').extract_first()}
        for next_page in response.css('div.prev-post > a'): #下一页继续爬, prev-post class里的链接
            yield response.follow(next_page, self.parse)



'''
很多类似的entry

2018-04-04 17:01:59 [scrapy.core.scraper] DEBUG: Scraped from <200 https://blog.scrapinghub.com/page/11/>
{'title': u'Hello, world'}

'''
