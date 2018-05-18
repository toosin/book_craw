# -*- coding: utf-8 -*-
import scrapy
from books.mysql1 import msyqlHelper
import json
import time
class YunduyunSpider(scrapy.Spider):
    name = 'yunduyun'
    allowed_domains = ['leyuee.com']
    start_urls = ['http://www.leyuee.com/services/zwfx.aspx?method=booklist&token=sefaf23h7face']

    def parse(self, response):
        res = response.text;
        res = self.json_encode(res)
        #detail_format = "http://www.leyuee.com/services/zwfx.aspx?method=bookinfo&bid=580&token=sefaf23h7face"
        i = 0
        mysql = msyqlHelper()
        #yield scrapy.Request("http://www.leyuee.com/services/yueloo.aspx?method=bookinfo&bid=%s&token=sefef2324fawe" % res['data'][0]['book_id'],callback=self.parse2,meta={"ly_bid":res['data'][0]['book_id'],"i":1})
        #return
        for item in res['data']:
        	exist = mysql.selectbylyid(item['book_id'])
        	
        	if exist is not None:
        		self.logger.info(exist)
        		continue
        	yield scrapy.Request("http://www.leyuee.com/services/zwfx.aspx?method=bookinfo&token=sefaf23h7face&bid=%s" % item['book_id'],callback=self.parse2,meta={"ly_bid":item['book_id'],"i":i})
        mysql.close()
    def parse2(self,response):
        mysql = msyqlHelper()
        res = response.text;
        res = self.json_encode(res)
        data = dict()
        data['ly_bid'] = res['data']['book_id']
        data['name'] = res['data']['book_name']
        data['author'] = res['data']['book_author']
        data['intro'] = res['data']['introduction']
        data['cover'] = res['data']['cover_url']
        data['category_name'] = res['data']['book_tags']
        data['category_id'] = res['data']['book_category_id']
        data['status'] = res['data']['book_state']
        data['sequence'] = response.meta['i']
        bid = mysql.insertbook(data)
        mysql.close()

        yield scrapy.Request("http://www.leyuee.com/services/zwfx.aspx?method=chapterlist&bid=%s&token=sefaf23h7face" % res['data']['book_id'],meta={"bid":bid,"book_id":res['data']['book_id']},callback=self.parse3)

    def parse3(self,response):
        res = response.text;
        res = self.json_encode(res)
        if res['code']  == 200:
        	mysql = msyqlHelper()
        	for chapter in res['data'][0]['chapters']:
        		chapter['bid'] = response.meta['bid']
        		yield scrapy.Request('http://www.leyuee.com/services/zwfx.aspx?method=chapter&bid=%s&cid=%s&token=sefaf23h7face' % (response.meta['book_id'],chapter['chapter_id']),meta=chapter,callback=self.parse4)

        mysql.close()
    def parse4(self,response):
        res = response.text;
        res = self.json_encode(res)
        if res['code'] == 200:
        	mysql = msyqlHelper()
        	meta = response.meta
        	data = dict()
        	data['bid'] = meta['bid']
        	data['name'] = meta['chapter_name']
        	data['sequence'] = meta['chapter_order_number']+1
        	data['size'] = len(res['data']['chapter_content'])
        	data['is_vip'] = meta['chapter_need_pay']
        	data['prev_cid'] = 0
        	data['next_cid'] = 0
        	data['recent_update_at'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(meta['chapter_last_update_time']))
        	data['content'] = res['data']['chapter_content']
        	data['ly_chapter_id'] = res['data']['chapter_id']
        	mysql.inseraAll(data)
    def json_encode(self,jsonstr):
    	return json.loads(jsonstr)
