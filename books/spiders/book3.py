# -*- coding: utf-8 -*-
import scrapy
from books.mysql import msyqlHelper
from urllib.parse import urljoin
import logging
import re


class FenghuangSpider(scrapy.Spider):
	name = 'book3'
	allowed_domains = ['pbtxt.com','tmetb.com','tywx.com','biquge.cc']
	start_urls = [
					['超品透视','http://www.pbtxt.com/52065/','//div[@id="novel52065"]/dl/dd/a','content','other'],
					['功夫神医在都市','http://www.tmetb.com/150/150356/','//div[@class="main-wrap"]/div[@class="box"]/div/ul/li/a','text_area'],
					['逍遥兵王','http://www.tywx.com/ty102148/','//*[@id="chapterlist"]/ul[position()>1]/li/a','content'],
					['超级小郎中','http://www.tywx.com/ty94829/','//*[@id="chapterlist"]/ul[position()>1]/li/a','content'],
					['特种服务员','http://www.tywx.com/ty90535/','//*[@id="chapterlist"]/ul[position()>1]/li/a','content'],
					['乡村小医仙','http://www.tywx.com/ty159568/','//*[@id="chapterlist"]/ul[position()>1]/li/a','content'],
					['都市小农民','http://www.tywx.com/ty125090/','//*[@id="chapterlist"]/ul[position()>1]/li/a','content'],
					['都市奇门医圣','http://www.biquge.cc/html/129/129930/','//*[@id="list"]/dl/dd/a','content'],
					['御手狂医','http://www.biquge.cc/html/129/129930/','//*[@id="list"]/dl/dd/a','content'],
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
		