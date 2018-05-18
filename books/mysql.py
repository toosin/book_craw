# -*- coding: utf-8 -*-
import time
import pymysql.cursors
class msyqlHelper(object):
	def __init__(self):
		self.conn = pymysql.connect(host='192.168.18.144',user='zhaoyang',password='123456',db='bsread',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		self.encoding = 'utf-8'
	def setTable(self,table):
		self.table = table
	
	def insert(self,data):
		now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		sql = "INSERT INTO `bs_chapters` (`bid`, `name`,`sequence`,`size`,`is_vip`,`prev_cid`,`next_cid`,`recent_update_at`,`created_at`,`updated_at`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		with self.conn.cursor() as cursor:
			cursor.execute(sql,(data['bid'],data['name'],data['sequence'],data['size'],data['is_vip'],data['prev_cid'],data['next_cid'],now,now,now))
			id = int(cursor.lastrowid)
		self.conn.commit()
		return id
	def insertcontent(self,data):
		sql = "update bs_chapters set content=%s where name=%s and bid=%s";
		with self.conn.cursor() as cursor:
			cursor.execute(sql,(data['contetn'],data['name'],data['bid']))
		self.conn.commit()
	
	def insertbook(self,book_name):
		now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		sql = "insert into bs_books (name,author,intro,cover,category,status,chapter_count,first_cid,last_cid,size,last_chapter,is_recommended,`created_at`,`updated_at`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		id = 0
		with self.conn.cursor() as cursor:
			res = cursor.execute(sql,(book_name,'0','0','0','0','0','0','0','0','0','0','0',now,now))
			id = int(cursor.lastrowid)
		self.conn.commit()
		return id
	def inseraAll(self,data):
		now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		sql = "INSERT INTO `bs_chapters` (`bid`, `name`,`sequence`,`size`,`is_vip`,`prev_cid`,`next_cid`,`recent_update_at`,`created_at`,`updated_at`,`content`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		with self.conn.cursor() as cursor:
			cursor.execute(sql,(data['bid'],data['name'],data['sequence'],data['size'],data['is_vip'],data['prev_cid'],data['next_cid'],now,now,now,data['content']))
			id = int(cursor.lastrowid)
		self.conn.commit()
		return id
	def getByBidAndName(self,name,bid):
		res=None;
		with self.conn.cursor() as cursor:
			sql="select id,content from bs_chapters where bid=%s and name=%s"
			cursor.execute(sql, (bid,name))
			res = cursor.fetchone()
		self.conn.commit()
		return res		
	def updateChapter(self,data):
		if data['content'] == '':
			return None
		if data['content'] is None:
			return None;	
		try:

			#sql = "update bs_chapters set content=%s,size=%s where bid=%s and name=%s";
			sql = "update bs_chapters set content=%s,size=%s where bid=%s and name=%s";

			with self.connection.cursor() as cursor:
				res = cursor.execute(sql,(self.content(data['content']),len(self.content(data['content'])),int(data['bid']),int(data['name'])))
			self.connection.commit()
		finally:
			#self.connection.close()
			password		
	def close(self):
		self.conn.close()