# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

import pymysql
import pymysql.cursors
import time
import re
class BooksPipeline(object):
    def process_item(self, item, spider):
        return item

		
		
		
		
		
class TutorialMysqlPipeline(object):
	
	def __init__(self,
				host='192.168.10.140',
				user='zhaoyang',
				password='123456',
				db=''):
		self.host = host
		self.user = user
		self.password = password
		self.db = db
		self.cursorclass = pymysql.cursors.DictCursor
		
		
	@classmethod	
	def from_crawler(cls, crawler):	
		
		return cls(
			host = crawler.settings.get('MYSQL_HOST'),
			user = crawler.settings.get('MYSQL_USER'),
			password = crawler.settings.get('MYSQL_PASS'),
			db = crawler.settings.get('MYSQL_DB'),
		)
		
	def open_spider(self, spider):
		self.connection = pymysql.connect(host = self.host,user=self.user,password=self.password,db=self.db,charset='utf8mb4',cursorclass=self.cursorclass)
		#self.cursor = self.connection.cursor()replace
	
	def process_item(self, item, spider):
		self.insertChapter(item)
		#self.updateChapter(item)
		return item	
	
	def insertChapter(self,data):
		try:
			#sql = "update bs_chapters set content=%s,size=%s where bid=%s and name=%s";
			sql = "update bs_chapters set content=%s,size=%s where id=%s";
			with self.connection.cursor() as cursor:
				res = cursor.execute(sql,(self.content(data['content']),len(self.content(data['content'])),int(data['id'])))
			self.connection.commit()
		finally:
			#self.connection.close()
			pass
	def updateChapter(self,data):
		if data['content'] == '':
			return None
		if data['content'] is None:
			return None;	
		try:

			#sql = "update bs_chapters set content=%s,size=%s where bid=%s and name=%s";
			sql = "update bs_chapters set content=%s,size=%s where bid=%s and name=%s";

			with self.connection.cursor() as cursor:
				res = cursor.execute(sql,(self.content(data['content']),len(self.content(data['content'])),int(data['bid']),data['name']))
			self.connection.commit()
		finally:
			#self.connection.close()
			pass		
	
	def close_spider(self,spider):		
		self.connection.close()	
	


	def content(self,content):
		return content.strip()