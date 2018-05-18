# -*- coding: utf-8 -*-
import time
import pymysql.cursors
class msyqlHelper(object):
	def __init__(self):
		self.conn = pymysql.connect(host='rm-bp1z1dto3n2rdb02f.mysql.rds.aliyuncs.com',user='yueduyun',password='yueduyun2017#Ydy',db='yueduyun',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		self.encoding = 'utf-8'
	def setTable(self,table):
		self.table = table
	
	def insert(self,data):
		now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		sql = "INSERT INTO `chapters` (`bid`, `name`,`sequence`,`size`,`is_vip`,`prev_cid`,`next_cid`,`recent_update_at`,`created_at`,`updated_at`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		with self.conn.cursor() as cursor:
			cursor.execute(sql,(data['bid'],data['name'],data['sequence'],data['size'],data['is_vip'],data['prev_cid'],data['next_cid'],now,now,now))
			id = int(cursor.lastrowid)
		self.conn.commit()
		return id
	def insertcontentbyname(self,data):
		sql = "update bs_chapters set content=%s where name=%s and bid=%s";
		with self.conn.cursor() as cursor:
			cursor.execute(sql,(data['content'],data['name'],data['bid']))
		self.conn.commit()
	def insertcontentbyid(self,data):
		sql = "update bs_chapters set content=%s,size=%s where bid=%s";
		with self.conn.cursor() as cursor:
			cursor.execute(sql,(data['content'],len(data['content']),data['id']))
		self.conn.commit()

	def insertbook(self,data):
		now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		sql = "insert into books (ly_bid,name,author,intro,cover,category_name,category_id,status,sequence,chapter_count,first_cid,last_cid,size,last_chapter,`created_at`,`updated_at`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		id = 0
		with self.conn.cursor() as cursor:
			res = cursor.execute(sql,(data['ly_bid'],data['name'],data['author'],data['intro'],data['cover'],data['category_name'],data['category_id'],data['status'],data['sequence'],'0','0','0','0','0',now,now))
			id = int(cursor.lastrowid)
		self.conn.commit()
		return id
	def inseraAll(self,data):
		now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		sql = "INSERT INTO `chapters` (`bid`, `name`,`sequence`,`size`,`is_vip`,`prev_cid`,`next_cid`,`recent_update_at`,`created_at`,`updated_at`,`content`,`ly_chapter_id`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		with self.conn.cursor() as cursor:
			cursor.execute(sql,(data['bid'],data['name'],data['sequence'],data['size'],data['is_vip'],data['prev_cid'],data['next_cid'],now,now,now,data['content'],data['ly_chapter_id']))
			id = int(cursor.lastrowid)
		self.conn.commit()
		return id
	def selectbylyid(self,id):
		result = None
		with self.conn.cursor() as cursor:
			sql = "select ly_bid from books where ly_bid=%s"
			cursor.execute(sql,(id))
			result = cursor.fetchone()
		self.conn.commit()
		return 	result;		
	def close(self):
		self.conn.close()