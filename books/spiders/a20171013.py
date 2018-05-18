# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from books.mysql import msyqlHelper
class A20171013Spider(scrapy.Spider):
    name = '20171013'
    allowed_domains = ['bookbao8.com','263zw.com']
    start_urls = [
					#['124','https://www.bookbao8.com/book/201612/18/id_XNTUzNTg3.html','/html/body/div[7]/ul/li/a','//*[@id="contents"]/p/text()'],
					#['125','http://www.263zw.com/503/list/','//*[@id="main"]/div[2]/div[2]/div/ul/li/a','//*[@id="chapterContent"]/text()'],					
					['897','https://www.bookbao8.com/book/201610/25/id_XNTQ1OTgx.html','//*[@class="wp b2 info_chapterlist"]/ul/li[position()>570]/a','//*[@id="contents"]/text()'],					
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
		    	meta['prev_cid'] = 	0
		    meta['next_cid'] = 0
            
		    maxcid = maxcid+1
		    meta['sequence'] = j
		    j = j+1
		    self.logger.info('Parse url is  %s', next_url)
		    chapter_id = mysql.insert(meta)
		    meta['contentxpath'] = response.meta['contentxpath']
		    meta['id'] = chapter_id
		    self.logger.info('Parse function called on dfsdfsd------------------')
		    if name == '第621章621威胁，直到你满意为止':
		    	break;
		    if j >51:
		    	break;	
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
