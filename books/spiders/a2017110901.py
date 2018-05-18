# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from books.mysql import msyqlHelper
class A20171013Spider(scrapy.Spider):
    name = '2017110901'
    allowed_domains = ['mywenxue.com','mytxt.cc','shangshu.cc']
    start_urls = [
					['135','http://www.mywenxue.com/xiaoshuo/67/67741/Index.htm','//div[@class="insert_list"]/dl/dd/ul/li/strong/a','//div[@id="chapterContent"]/p/text()'],						
					['136','http://www.mywenxue.com/xiaoshuo/67/67854/Index.htm','//div[@class="insert_list"]/dl/dd/ul/li/strong/a','//div[@id="chapterContent"]/p/text()'],						
					['137','http://www.mytxt.cc/read/9780/','//div[@id="story9780"]/div/ol/li/a','//div[@class="detail_con_m62topxs"]/p/text()'],						
					['138','http://www.shangshu.cc/98/98978/','//div[@id="index"]/div[@class="ListCon"]/ul[@class="ListRow"]/li/a','//div[@id="content"]/text()'],						
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
