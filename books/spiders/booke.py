# -*- coding: utf-8 -*-
import scrapy
from books.mysql import msyqlHelper
from urllib.parse import urljoin
import logging
import re


class FenghuangSpider(scrapy.Spider):
	name = 'booke'
	allowed_domains = ['biqugex.com','baoliny.com','630book.la','9cwx.com','kanshula.org','xxbiquge.com','wangshuge.com','lewenxiaoshuo.com','22ff.com','23us.cc','wenxuemm.com','yqzww.com']
	start_urls = [
					['无敌医神','http://www.biqugex.com/book_21372/','//div[@class="listmain"]/dl/dd[position()>12]/a','content'],
					['超品兵王','http://www.baoliny.com/119720/index.html','/html/body/div[2]/div[4]/table/tr/td/a','content'],
					['美女保镖','http://www.630book.la/shu/13556.html','//dl[@class="zjlist"]/dd/a','content'],
					['修仙归来在都市','http://www.9cwx.com/6_6130/','//*[@id="list"]/dl/dd[position()>9]/a','content'],
					['混迹花都','http://www.kanshula.org/3_3489/0.html','//*[@id="list"]/dl/dd/a','content'],
					['农民医生','http://www.xxbiquge.com/22_22895/','//*[@id="list"]/dl/dd[position()>17]/a','content'],
					['纨绔兵王','http://www.wangshuge.com/books/97/97200/','//*[@id="at"]/tr/td/a','contents'],
					['家有表姐太傲娇','http://www.lewenxiaoshuo.com/books/jiayoubiaojietaiaojiao/','//*[@id="list"]/dl/dd/a','content'],
					['美女大小姐的贴身兵王','http://www.22ff.com/xs/205845/','//div[@class="neirong"]/div/a','chapter_content'],
					['情路官道','http://www.23us.cc/html/88/88465/','//div[@id="main"]/div/dl[@class="chapterlist"]/dd/a','content'],
					['最强废少','http://www.wenxuemm.com/book/46/46492/','//div[@class="novel_list"]/ul/li/a','clickeye_content'],
					['妙手狂医','http://www.yqzww.com/files/article/html/2/2566/index.html','//div[@class="zjlist4"]/ol/li/a','htmlContent']
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
		