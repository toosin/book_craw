# -*- coding: utf-8 -*-
import scrapy
from books.mysql import msyqlHelper
from urllib.parse import urljoin
import logging
import re


class FenghuangSpider(scrapy.Spider):
	name = 'other'
	allowed_domains = ['biqugex.com','kanshula.org','feizw.com','hkslg.net','shengyan.org','shengyan.org','xiaoshuo2016.com']
	start_urls = [
					#['1','http://www.feizw.com/Html/7355/Index.html','//div[@id="main"]/div[@class="chapterlist"]/ul/li/a','content'],
					#['25','http://www.23us.cc/html/133/133677/','//div[@id="main"]/div/dl[@class="chapterlist"]/dd/a','content'],
					#['25','http://www.shengyan.org/book/8707.html','//div[@class="listmain"]/dl/dd[position()>12]/a','content'],
					#['26','http://www.23us.cc/html/88/88465/','//div[@id="main"]/div/dl[@class="chapterlist"]/dd/a','content'],
					#['107','http://www.kanshula.org/3_3489/0.html','//*[@id="list"]/dl/dd/a','content'],
					#['69','http://www.qiuwu.net/html/223/223040/','//*[@id="defaulthtml4"]/table/tr/td/div/a','content'],
					#['55','http://www.feizw.com/Html/9788/Index.html','//*[@id="main"]/div[@class="chapterlist"]/ul/li/a','content'],
					#['56','http://www.feizw.com/Html/13897/index.html','//*[@id="main"]/div[@class="chapterlist"]/ul/li/a','content'],
					#['57','http://www.feizw.com/Html/12924/index.html','//*[@id="main"]/div[@class="chapterlist"]/ul/li/a','content'],
					#['58','http://www.feizw.com/Html/12167/index.html','//*[@id="main"]/div[@class="chapterlist"]/ul/li/a','content']
					#['108','http://www.xxbiquge.com/22_22895/','//*[@id="list"]/dl/dd[position()>17]/a','content'],
					#['23','http://www.fhxiaoshuo.com/read/96/96746/','//*[@id="list"]/dl/dd/a','TXT']
					#['29','http://www.biqugex.com/book_7075/','//div[@class="listmain"]/dl/dd[position()>619]/a','content']
					#['39','http://www.pbtxt.com/51964/','//div[@id="novel51964"]/dl/dd[position()>761]/a','content']
					#['54','http://www.xiaoshuo2016.com/129469/','/html/body/div[2]/div[1]/div[4]/div[2]/ul/li/a','content']
					['50','http://www.hkslg.net/119/119193/','//*[@id="defaulthtml4"]/table/tbody/tr[position()>143]/td/div/a','content']
					
				]
	
	def start_requests(self):
		msyql = msyqlHelper()
		for url in self.start_urls:

			link =  url[1]
			bid = url[0]
			meta = {}
			meta['bid'] = bid
			meta['xpath'] = url[2]
			meta['id'] = url[3]
			#self.logger.info(' 111111111111111111111111111111111111111 ------------------')
			yield scrapy.Request(link,callback=self.parse,meta=meta)
		msyql.close();
	def parse(self,response):
		mysql = msyqlHelper()
		old = response.meta
		names = set(['上架感言！'])
		links = response.xpath(old['xpath'])
		self.logger.info(response.status)
		#self.logger.info('111 111 11 11 111 url------------------%s',response.url)
		j = 1
		for link in links:
			name = link.xpath('text()').extract_first();
			if name in names:
				continue;
			href = link.xpath('@href').extract_first();
			url = urljoin(response.url,href)
			#name = name.strip()
			if name == '第四百三十五章 自作孽不可活 4':
				break;
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
			#chapter_id = mysql.insert(meta);
			#meta['chapter_id'] = chapter_id
			#meta['id'] = old['id']+href.replace('.html','')
			meta['id'] = old['id']
			self.logger.info('bid is ------------------%s',meta['bid'])
			self.logger.info('name is -----name-------------%s',name)
			yield scrapy.Request(url,callback=self.parse2,meta=meta)
		mysql.close();
	
	def parse2(self,response):
		old = response.meta
		self.logger.info('parse2 parse2 parse2 parse2 parse2------------------')
		self.logger.info(response.status)
		self.logger.info('parse2 function called on dfsdfsd------------------%s',response.url)
		#str =  response.xpath('//*[@id="'+old['id']+'"]/text()').extract()
		#str =  response.xpath('//*[@id="yellow"]/div[1]/div[2]/div[2]/p/text()').extract()
		str =  response.xpath('//div[@id="content"]/p/text()').extract()
		#if not str:
		#	str =  response.xpath('//*[@id="'+old['id']+'"]/p/text()').extract()
		data = 	response.meta
		data['content'] = "\r\n".join(str)
		if data['content']:
			yield data
		