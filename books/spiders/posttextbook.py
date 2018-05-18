# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from books.mysql import msyqlHelper
import hashlib
from scrapy.http import FormRequest
class PosttextbookSpider(scrapy.Spider):
    name = 'posttextbook'
    allowed_domains = ['dongfengye.com']
    start_urls = [
					['132','http://www.dongfengye.com/d/147457.html','//section[4]/div/div[1]/ul[@class="list-group"]/li/a','//*[@id="content"]/text()'],			
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
    	num = 30
    	for link in links:
		    name = link.xpath('text()').extract_first()
		    if name in names:
		    	continue
		    href = link.xpath('@href').extract_first()
		    next_url = urljoin(response.url,href)
		    names.add(name)
		    meta = dict()
		    meta['href'] = href
		    meta['name'] = name
		    meta['bid'] = response.meta['bid']
		    meta['size'] = 0
		    meta['is_vip'] = 1
		    if(name == '098我还没照顾过谁'):
		    	 num = 1
		    if(name == '198谁也拆散不了我们'):
		    	num = 2
		    if(name == '255当家立威'):
		    	num = 66
		    if(name == '259真命天女'):
		    	num = 7	
		    num = num%100;
		    meta['numnum'] = num
		    num += 10
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
        href = meta['href']
        num = meta['numnum']
        param = self.formParam(href,num)
        self.logger.info('param------------param-----param----------')
        self.logger.info(param);
        headers={
			"Referer":response.url,
			"Origin":"http://www.dongfengye.com",
			"X-Requested-With":"XMLHttpRequest"
		}

        yield FormRequest('http://www.dongfengye.com/content.php',formdata=param,headers=headers,callback=self.parse2,meta=meta)

    def parse2(self,response):
        meta = response.meta
        self.logger.info('--------------res si res is ------------------------');
        self.logger.info(response.text)
        meta['content'] = response.text
        yield meta


    def sha1(self,data):
        if data == 0:
            data = '00'
        if data < 10:
        	data = '0'+str(data)    
        hash = hashlib.sha1()
        hash.update(str(data).encode('utf-8'))
        return hash.hexdigest()

    def formParam(self,href,num):
        if href is  None:
            return None
        href = href[0:-5]
        href_list = href.split('/');
        fid = self.sha1(num)
        bid = href_list[2];
        rid = href_list[3]
        return {'bid':bid,'rid':rid,'fid':fid} 	