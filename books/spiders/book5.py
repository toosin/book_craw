# -*- coding: utf-8 -*-
import scrapy
from books.mysql import msyqlHelper
from urllib.parse import urljoin
import logging
import re


class FenghuangSpider(scrapy.Spider):
	name = 'book5'
	allowed_domains = ['263zw.com','dhzw.org','qiuwu.net','mht.la','kanshu58.com','800xs.net','shangshu.cc','00ksw.org']
	start_urls = [
					['我和26岁美女村长','http://www.263zw.com/408493/list/','//*[@id="main"]/div[2]/div[2]/div/ul/li/a','chapterContent'],
					['贴身透视高手','http://www.dhzw.org/book/185/185022/','//*[@id="list"]/dl/dd/a','BookText'],
					['贴身保安','http://www.00ksw.org/html/5/5120/','//*[@id="list"]/dl/dd/a','content'],
					['小村那些事','http://www.qiuwu.net/html/223/223040/','//*[@id="defaulthtml4"]/table/tr/td/div/a','content'],
					['超级佣兵','http://www.qiuwu.net/html/169/169757/index.html','//*[@id="defaulthtml4"]/table/tr/td/div/a','content'],
					['极品小野医','http://www.mht.la/72/72610/','//*[@id="novel72610"]/dl/dd/a','con','other'],
					['我和美女上司','http://www.mht.la/71/71712/','//*[@id="novel71712"]/dl/dd/a','con','other'],
					['神级保安','http://www.mht.la/67/67049/','//*[@id="novel67049"]/dl/dd/a','con','other'],
					['超级狂医','http://www.mht.la/72/72165/','//*[@id="novel72165"]/dl/dd/a','con','other'],
					['山村名医','http://www.kanshu58.com/book/204/204357/index.html','/html/body/div[8]/ul/li/a','content'],
					['捡个杀手做老婆','http://www.kanshu58.com/book/1/1528/index.html','/html/body/div[8]/ul/li/a','content'],
					['女总裁的近身特工','http://www.shangshu.cc/60/60174/','//*[@id="index"]/div[2]/ul[@class="ListRow"]/li/a','content'],
					['都市之全能至尊','http://www.800xs.net/book_59832/','/html/body/div[4]/div/ul/li/a','htmlContent'],
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
		