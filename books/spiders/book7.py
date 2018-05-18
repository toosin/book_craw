# -*- coding: utf-8 -*-
import scrapy
from books.mysql import msyqlHelper
from urllib.parse import urljoin
import logging
import re

class FenghuangSpider(scrapy.Spider):
	name = 'book7'
	allowed_domains = ['ybdu.com','biqudao.com','abxsw.com','bookxuan.com','tadu.com','800txt.net','800xs.net','ziyouge.com']
	start_urls = [
					['近身兵王','http://www.biqudao.com/bqge1036/','//*[@id="list"]/dl/dd[position()>14]/a','content'],
					['黑道特种兵','http://www.ybdu.com/xiaoshuo/7/7021/','//ul[@class="mulu_list"]/li/a','htmlContent'],
					['盛世狂医','http://www.tadu.com/book/catalogue/422284','//div[@class="detail-chapters"]/ul/li/h5/a','partContent'],
					['绝色女神','http://www.bookxuan.com/36_36429/','//*[@id="list"]/dl/dd/a','content'],
					['我在殡仪馆工作的那些事儿','http://www.abxsw.com/book/257124/','/html/body/div[1]/div[5]/ul[2]/li/a','contents'],
					['美女总裁爱上小保安：绝世高手','http://www.800txt.net/book_13248/','//*[@id="list"]/dl/dd/a','content'],
					['极品桃花运','http://www.800txt.net/book_17891/','//*[@id="list"]/dl/dd/a','content'],
					['重生之全能巨星','http://www.800xs.net/book_59893/','/html/body/div[4]/div/ul/li/a','htmlContent'],
					['绝品神医','http://www.ziyouge.com/zy/10/10465/index.html','//ul[@class="chapter-list"]/li/a','htmlContent']
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
		