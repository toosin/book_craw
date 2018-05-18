# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from books.mysql import msyqlHelper
from scrapy.http import FormRequest
class PosttestSpider(scrapy.Spider):
    name = 'posttest'
    allowed_domains = ['dongfengye.comm']
    start_urls = ['http://www.dongfengye.com/content.php']

    def start_requests(self):
    	for u in self.start_urls:
	        headers={
				"Referer":"http://www.dongfengye.com/d/147457/41539005.html",
				"Origin":"http://www.dongfengye.com",
				"X-Requested-With":"XMLHttpRequest"
			}
	        formdata = {
				'bid':'147457',
				'rid':'41539005',
				'fid':'e1822db470e60d090affd0956d743cb0e7cdf113'
			}
	        yield FormRequest(u,formdata=formdata,headers=headers,callback=self.parse)

    def parse(self,response):
    	self.logger.info('-----------------------------------');
    	self.logger.info(response.text)
