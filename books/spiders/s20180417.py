# -*- coding: utf-8 -*-
import scrapy
from books.mysql import msyqlHelper
from urllib.parse import urljoin
import logging
import re


class FenghuangSpider(scrapy.Spider):
	name = 's20180417'
	allowed_domains = ['dingdianzw.com','23wxw.cc','23us.cc','x23us.com','fhxsw.org','biqugecom.com','yznn.com','biquwu.cc','lzkan.com','bxwx.io','booktxt.net','biqule.com']
	start_urls = [
					#['修仙高手混花都','http://www.dingdianzw.com/book/57907.html','//table[@id="bgdiv"]/tbody/tr/td/div/a','//div[@id="content"]/text()'],
					['都市奇门医圣','http://www.dingdianzw.com/book/5240.html','//table[@id="bgdiv"]/tbody/tr/td/div/a','//div[@id="content"]/text()'],
					['都市极品医王','http://www.dingdianzw.com/book/59246.html','//table[@id="bgdiv"]/tbody/tr/td/div/a','//div[@id="content"]/text()'],
					['绝品透视','http://www.yznn.com/files/article/html/29/29742/index.html','//div[@class="zjlist4"]/ol/li/a','//div[@id="htmlContent"]/text()'],
					['我的绝色明星老婆','https://www.biquwu.cc/biquge/27_27864/','//div[@id="list"]/dl/dd/a','//div[@id="content"]/text()'],
					['医武兵王','https://www.biquwu.cc/biquge/40_40394/','//div[@id="list"]/dl/dd/a','//div[@id="content"]/text()'],
					['贴身狂医俏总裁','http://www.lzkan.com/k/37270.html','//ul[@class="list-group"]/li[@class="list-group-item col-lg-3 col-md-3 col-sm-4 col-xs-6 book"]/a','//div[@class="content"]/text()'],
					['王牌保镖','http://www.lzkan.com/k/5261.html','//ul[@class="list-group"]/li[@class="list-group-item col-lg-3 col-md-3 col-sm-4 col-xs-6 book"]/a','//div[@class="content"]/text()'],
					['透视神眼','http://www.bxwx.io/book/100129/','//dl[@class="zjlist"]/dd/a','//div[@id="content"]/text()'],
					['超品战兵','http://www.booktxt.net/1_1192/','//div[@id="list"]/dl/dd[position()>9]/a','//div[@id="content"]/text()'],
					['天才纨绔','https://www.biquwu.cc/biquge/2_2575/','//div[@id="list"]/dl/dd/a','//div[@id="content"]/text()'],
					['女村长的贴身兵王','http://www.biqule.com/book_72711/','//div[@class="article-list"]/dl/dd/a','//div[@id="content"]/text()'],
					['儿媳妇','https://www.23wxw.cc/html/607/','//div[@id="list"]/dl/dd[position()>9]/a','//div[@id="content"]/text()'],
					['妇科男神医','http://www.biqugecom.com/35/35932/','//div[@id="list"]/dl/dd[position()>9]/a','//div[@id="content"]/text()'],
					['出轨的女人','http://www.biqugecom.com/39/39559/','//div[@id="list"]/dl/dd[position()>9]/a','//div[@id="content"]/text()'],
					['乡野诱惑','http://www.fhxsw.org/read/15849/','//div[@id="list"]/dl/dd/a','//div[@id="content"]/text()'],
					#['超级保镖','http://www.yssm.org/uctxt/15/15024/','//*[@id="main"]/div/dl/dd/a','content'],
					#['修真强少在校园','http://www.yssm.org/uctxt/50/50324/','//*[@id="main"]/div/dl/dd/a','content']
				]
	
	def start_requests(self):
		msyql = msyqlHelper()
		for url in self.start_urls:
			book_name = url[0]
			link =  url[1]
			bid = msyql.insertbook(book_name)
			meta = {}
			meta['bid'] = bid
			meta['xpath'] = url[2]
			meta['id'] = url[3]
			meta['contentxpath'] = url[3]
			yield scrapy.Request(link,callback=self.parse,meta=meta)
		msyql.close();
	def parse(self,response):
		mysql = msyqlHelper()
		old = response.meta
		names = set(['上架感言！'])
		links = response.xpath(old['xpath'])
		
		j = 1
		for link in links:
			name = link.xpath('text()').extract_first();
			if name in names:
				continue;
			href = link.xpath('@href').extract_first();
			url = urljoin(response.url,href)
			names.add(name)
			meta = {}
			meta['name'] = name
			meta['bid'] = old['bid']
			meta['size'] = 0
			meta['is_vip'] = 1
			meta['prev_cid'] = 0
			meta['next_cid'] = 0
			meta['sequence'] = j
			meta['contentxpath'] = old['contentxpath']
			j = j+1
			self.logger.info('Parse url is  %s', url)
			chapter_id = mysql.insert(meta);
			#meta['id'] = old['id']
			meta['id'] = chapter_id
			self.logger.info('Parse function called on dfsdfsd------------------')
			yield scrapy.Request(url,callback=self.parse2,meta=meta)
		mysql.close();
	
	def parse2(self,response):
		meta = response.meta

		self.logger.info('11111111111111111111111111parse_content------------------%s',response.url)
		str = response.xpath(meta['contentxpath']).extract()
		str = filter(lambda s:s != '',str)
		newsttr = list(str)
		content = '\r\n'.join(newsttr)
		meta['content'] = content
		yield meta  
		