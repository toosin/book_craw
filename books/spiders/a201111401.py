# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from books.mysql import msyqlHelper
class A20111401Spider(scrapy.Spider):
    name = '20111401'
    allowed_domains = ['kxs7.com','i7wx.com','qb5200.co','xzwomen.com','jingcaiyuedu.com']
    start_urls = [
					#['151','https://www.kxs7.com/du/104365/','//div[@id="list"]/dl/dd[position()>12]/a','//*[@id="content"]/text()'],			
					#['152','http://www.qb5200.co/shu/78248.html','//div[@class="zjbox"]/dl/dd/a','//*[@id="content"]/text()'],			
					#['153','http://www.i7wx.com/book/22/22405/','//div[@id="readerlist"]/ul/li/a','//*[@id="content"]/text()'],			
					#['154','http://www.i7wx.com/book/29/29529/','//div[@id="readerlist"]/ul/li/a','//*[@id="content"]/text()'],			
					#['155','http://www.i7wx.com/book/24/24480/','//div[@id="readerlist"]/ul/li/a','//*[@id="content"]/text()'],			
					['157','http://www.xzwomen.com/112731.shtml','//ul[@class="nav clearfix"]/span/a','//div[@id="content"]/text()'],			
					['158','http://www.jingcaiyuedu.com/book/105034.html','//dl[@id="list"]/dd/a','//div[@class="panel-body content-body content-ext"]/text()'],			
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
		    #names.add(name)
		    meta = dict()
		    meta['name'] = name
		    meta['bid'] = response.meta['bid']
		    meta['size'] = 0
		    meta['is_vip'] = 1
		    if j == 1:
		    	meta['prev_cid'] = 0
		    else:
		    	meta['prev_cid'] = 	maxcid-1
		    meta['next_cid'] = 0
            
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
