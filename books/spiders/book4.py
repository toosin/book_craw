# -*- coding: utf-8 -*-
import scrapy
from books.mysql import msyqlHelper
from urllib.parse import urljoin
import logging
import re


class FenghuangSpider(scrapy.Spider):
	name = 'book4'
	allowed_domains = ['tywx.com','feizw.com','qu.la','jsusj.com']
	start_urls = [
					['最强透视','http://www.feizw.com/Html/9788/Index.html','//*[@id="main"]/div[@class="chapterlist"]/ul/li/a','content'],
					['神棍小村医','http://www.feizw.com/Html/13897/index.html','//*[@id="main"]/div[@class="chapterlist"]/ul/li/a','content'],
					['绝品村医','http://www.feizw.com/Html/12924/index.html','//*[@id="main"]/div[@class="chapterlist"]/ul/li/a','content'],
					['全能小村医','http://www.feizw.com/Html/12167/index.html','//*[@id="main"]/div[@class="chapterlist"]/ul/li/a','content'],
					['都市最强兵王','http://www.qu.la/book/4830/','//*[@id="list"]/dl/dd/a','content'],
					['富家女的超级高手','http://www.tywx.com/ty148173/','//*[@id="chapterlist"]/ul[position()>1]/li/a','content'],
					['极品都市高手','http://www.jsusj.com/52/52586/','//*[@id="chapter"]/dl/dd/a','text_area'],
					['女总裁的贴身保镖','http://www.qu.la/book/5295/','//*[@id="list"]/dl/dd/a','content'],
					['桃运神戒','http://www.qu.la/book/20419/','//*[@id="list"]/dl/dd/a','content'],
					['无双宝鉴','http://www.qu.la/book/9868/','//*[@id="list"]/dl/dd/a','content'],
					['御宝天师','http://www.qu.la/book/636/','//*[@id="list"]/dl/dd/a','content']
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
		