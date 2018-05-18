# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from books.mysql import msyqlHelper
class A20171013Spider(scrapy.Spider):
    name = '2017110101'
    allowed_domains = ['gzbpi.com','dongfengye.com']
    start_urls = [
					['129','http://www.gzbpi.com/shu/227860/','//ul[@class="mulu_list"]/li/a','//div[@class="page-content"]/pre/text()'],			
					['130','http://www.gzbpi.com/shu/192282/','//ul[@class="mulu_list"]/li/a','//div[@class="page-content"]/pre/text()'],			
					['131','http://www.gzbpi.com/shu/217123/','//ul[@class="mulu_list"]/li/a','//div[@class="page-content"]/pre/text()'],			
					#['132','http://www.dongfengye.com/d/147457.html','//ul[@class="list-group"]/li/a','//div[@id="content"]/div[@class="content"]/pre/text()'],			
					['133','http://www.gzbpi.com/shu/217113/','//ul[@class="mulu_list"]/li/a','//div[@class="page-content"]/pre/text()'],			
					['134','http://www.gzbpi.com/shu/198898/','//ul[@class="mulu_list"]/li/a','//div[@class="page-content"]/pre/text()'],			
				]

    def start_requests(self):
        for url in self.start_urls:
        	meta ={}
        	meta['linkpath'] = url[2]
        	meta['bid'] = url[0]
        	meta['contentxpath'] = url[3]
        	yield scrapy.Request(url[1],callback=self.parse,meta=meta)
		
    def parse(self,response):
    	mysql = msyqlHelper()
    	names = set(['上架感言！'])
    	links = response.xpath(response.meta['linkpath'])

    	j = 1
    	maxcid = 1
    	for link in links:
		    name = link.xpath('text()').extract_first()
		    if name in names:
		    	continue
		    href = link.xpath('@href').extract_first()
		    next_url = urljoin(response.url,href)
		    names.add(name)
		    meta = dict()
		    meta['name'] = name
		    meta['bid'] = response.meta['bid']
		    meta['size'] = 0
		    meta['is_vip'] = 1
		    if j == 1:
		    	meta['prev_cid'] = 0
		    else:
		    	meta['prev_cid'] = 	maxcid-1
		    meta['next_cid'] = maxcid+1
            
		    maxcid = maxcid+1
		    meta['sequence'] = j
		    j = j+1
		    self.logger.info('Parse url is  %s', next_url)
		    chapter_id = mysql.insert(meta)
		    meta['contentxpath'] = response.meta['contentxpath']
		    meta['id'] = chapter_id
		    self.logger.info('Parse function called on dfsdfsd------------------')
		    yield scrapy.Request(next_url,callback=self.parse_content,meta=meta)
    	mysql.close()
    	
	    

	   
    def parse_content(self,response):
        meta = response.meta

        self.logger.info('parse_content parse_content parse_content on parse_content------------------%s',response.url)
        str = response.xpath(meta['contentxpath']).extract()
        str = filter(lambda s:s != '',str)
        newsttr = list(str)
        content = '\r\n'.join(newsttr)
        meta['content'] = content
        yield meta
