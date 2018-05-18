# -*- coding: utf-8 -*-
import scrapy
from books.mysql import msyqlHelper
from urllib.parse import urljoin
import logging
import re


class FenghuangSpider(scrapy.Spider):
	name = 'book1'
	allowed_domains = ['630book.net','xaishang.com','23us.cc','x23us.com','yssm.org','tywx.com']
	start_urls = [
					['超级保安在都市','http://www.630book.net/shu/63158.html','//div[@class="zjbox"]/dl[@class="zjlist"]/dd/a','content'],
					['血色辉煌','http://www.xaishang.com/book/176/176631/','//*[@id="at"]/tbody/tr/a','contents'],
					['我和美女院长','http://www.23us.cc/html/133/133677/','//div[@id="main"]/div/dl[@class="chapterlist"]/dd/a','content'],
					['情路官道','http://www.23us.cc/html/88/88465/','//div[@id="main"]/dl[@class="chapterlist"]/dd/a','content'],
					['美女总裁俏佳人','http://www.x23us.com/html/41/41500/','//*[@id="at"]/tr/td/a','contents'],
					['女总裁的贴身高手','http://www.tywx.com/ty115792/','//*[@id="chapterlist"]/ul[2]/li/a','content'],
					['极品透视','http://www.yssm.org/uctxt/49/49532/','//*[@id="main"]/div/dl/dd/a','content'],
					['神医小农民','http://www.yssm.org/uctxt/73/73031/','//*[@id="main"]/div/dl/dd/a','content'],
					['逍遥小村医','http://www.yssm.org/uctxt/84/84195/','//*[@id="main"]/div/dl/dd/a','content'],
					['女村长的贴身神医','http://www.yssm.org/uctxt/86/86745/','//*[@id="main"]/div/dl/dd/a','content'],
					['最强狂兵','http://www.yssm.org/uctxt/51/51502/','//*[@id="main"]/div/dl/dd/a','content'],
					['乡村小神医','http://www.yssm.org/uctxt/104/104785/','//*[@id="main"]/div/dl/dd/a','content'],
					['最强农民混都市','http://www.yssm.org/uctxt/54/54132/','//*[@id="main"]/div/dl/dd/a','content'],
					['超级保镖','http://www.yssm.org/uctxt/15/15024/','//*[@id="main"]/div/dl/dd/a','content'],
					['修真强少在校园','http://www.yssm.org/uctxt/50/50324/','//*[@id="main"]/div/dl/dd/a','content']
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
			meta['id'] = old['id']
			meta['chapter_id'] = chapter_id
			self.logger.info('Parse function called on dfsdfsd------------------')
			yield scrapy.Request(url,callback=self.parse2,meta=meta)
		mysql.close();
	
	def parse2(self,response):
		old = response.meta
		self.logger.info(response.status)
		self.logger.info('parse2 function called on dfsdfsd------------------%s',response.url)
		str =  response.xpath('//*[@id="'+old['id']+'"]/text()').extract()
		data = 	response.meta
		data['content'] = "\r\n".join(str)
		yield data
		