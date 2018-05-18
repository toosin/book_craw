# -*- coding: utf-8 -*-
import scrapy
from books.mysql import msyqlHelper
from urllib.parse import urljoin
import logging
import re


class FenghuangSpider(scrapy.Spider):
	name = 'book2'
	allowed_domains = ['263zw.com','luoqiu.com','258zw.com','8jzw.cc','zbzw.com']
	start_urls = [
					['极品神医','http://www.luoqiu.com/read/47002/','//*[@id="defaulthtml4"]/table/tr/td/div/a','content'],
					['特种房客俏千金','http://www.luoqiu.com/read/105845/','//*[@id="defaulthtml4"]/table/tr/td/div/a','content'],
					['特种奶爸俏老婆','http://www.luoqiu.com/read/37371/','//*[@id="defaulthtml4"]/table/tr/td/div/a','content'],
					['贴身兵王','http://www.luoqiu.com/read/221707/','//*[@id="defaulthtml4"]/table/tr/td/div/a','content'],
					['我的极品女老师','http://www.263zw.com/119138/list/','//*[@id="main"]/div[2]/div[2]/div/ul/li/a','chapterContent'],
					['极品小农民','http://www.258zw.com/html/1330/','//div[@class="article"]/div[@class="article_texttitleb"]/ul/li/a','chapterContent'],
					['锁骨娘子','http://www.8jzw.cc/Html/Book/152/152453/','//*[@id="list"]/dl/dd/a','content'],
					['我的美女总裁老婆','http://www.zbzw.com/wodemeinvzongcailaopo/','//div[@class="listmain"]/dl/dd[position()>9]/a','content'],
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
			self.logger.info('Parse function called on dfsdfsd------------------')
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
		