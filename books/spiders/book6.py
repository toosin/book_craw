# -*- coding: utf-8 -*-
import scrapy
from books.mysql import msyqlHelper
from urllib.parse import urljoin
import logging
import re


class FenghuangSpider(scrapy.Spider):
	name = 'book6'
	allowed_domains = ['ziyouge.com','126shu.com','sikushu.org','biquge.cc','hkslg.net','800txt.net','wenxuemm.com','qiuxiaoshuo.com','lread.cc','biquzi.com']
	start_urls = [
					['春野小村医','http://www.ziyouge.com/zy/12/12248/index.html','//ul[@class="chapter-list"]/li/a','htmlContent'],
					['农民小神医','http://www.ziyouge.com/zy/11/11848/index.html','//ul[@class="chapter-list"]/li/a','htmlContent'],
					['最强农民','http://www.ziyouge.com/zy/10/10722/index.html','//ul[@class="chapter-list"]/li/a','htmlContent'],
					['辣手村医','http://www.ziyouge.com/zy/11/11538/index.html','//ul[@class="chapter-list"]/li/a','htmlContent'],
					['阴司守灵人','http://www.ziyouge.com/zy/4/4618/index.html','//ul[@class="chapter-list"]/li/a','htmlContent'],
					['乡村小神医','http://www.ziyouge.com/zy/10/10582/index.html','//ul[@class="chapter-list"]/li/a','htmlContent'],
					['特种神医','http://www.800txt.net/book_3413/','//*[@id="list"]/dl/dd/a','content'],
					['透视兵王','http://www.126shu.com/60608/','//*[@id="list"]/dl/dd/a','content'],
					['摸骨神医','http://www.sikushu.org/115/115166/','//*[@id="list"]/ul/li/a','content'],
					['官场风云','http://www.hkslg.net/96/96332/','//*[@id="defaulthtml4"]/table/tr/td/div/a','content'],
					['超级小神农','http://www.hkslg.net/161/161905/','//*[@id="defaulthtml4"]/table/tr/td/div/a','content'],
					['合租医仙','http://www.wenxuemm.com/book/50/50724/','//div[@class="novel_list"]/ul/li/a','clickeye_content'],
					['绝世神医','http://www.qiuxiaoshuo.com/read/91414.html','//ul[@id="chapters-list"]/li/a','txtContent'],
					['都市血色兵王','http://www.lread.cc/read/27695/','//*[@id="list"]/dl/dd/a','booktext'],
					['花都贴身高手','http://www.biquzi.com/4_4668/','//*[@id="list"]/dl/dd/a','content'],
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
			if len(url) == 5:
				meta['other'] = True
			else:
				meta['other'] = False
			meta['id'] = url[3]
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
			j = j+1
			self.logger.info('Parse url is  %s', url)
			chapter_id = mysql.insert(meta);
			meta['chapter_id'] = chapter_id
			if old['other'] == True:
			
				meta['id'] = old['id']+href.replace('.html','')
			else:
				meta['id'] = old['id']
			self.logger.info('chapter_id is ------------------%s',chapter_id)
			yield scrapy.Request(url,callback=self.parse2,meta=meta)
		mysql.close();
	
	def parse2(self,response):
		old = response.meta
		self.logger.info('parse2 parse2 parse2 parse2 parse2------------------')
		self.logger.info(response.status)
		self.logger.info('parse2 function called on dfsdfsd------------------%s',response.url)
		str =  response.xpath('//*[@id="'+old['id']+'"]/text()').extract()
		if not str:
			str =  response.xpath('//*[@id="'+old['id']+'"]/p/text()').extract()
		data = 	response.meta
		data['content'] = "\r\n".join(str)
		yield data
		