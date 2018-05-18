# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from books.mysql import msyqlHelper
class A2017111302Spider(scrapy.Spider):
    name = '20171111302'
    allowed_domains = ['kanshuge.la','wanben.me','wuruo.com','aszw.org','wuruo.com','vodtw.com','txtjia.com','xiangcunxiaoshuo.la','paoshuba.cc','zuok.cn','iyunyue.com','773buy.com','qu.la','prwx.com','dhzw.org']
    start_urls = [
					#['146','http://www.bqg8.cc/0_696/','//div[@id="list"]/dl/dd/a','//div[@id="content"]/text()'],
					#['897','http://www.xsbashi.com/274792_0/','//div[@id="list"]/dl/dd/a','//div[@id="content"]/text()'],
					#['898','https://www.258zw.com/html/143719/','//div[@class="article_texttitleb"]/ul/li/a','//div[@id="chapterContent"]/text()'],
					#['1','http://wodeshucheng.com/book_16215/','//div[@class="book_list boxm"]/ul/li/a','//div[@id="htmlContent"]/text()'],
					#['1','http://www.xiangcunxiaoshuo.la/html/467005/','//section[@class="ml_main"]/dl/dd/a','//div[@class="yd_text2"]/text()'],
					#['4','https://www.aszw.org/book/251/251326/','//dd/table/tr/td/a','//div[@id="contents"]/text()'],
					#['6','http://www.qianqianxs.com/25/25617/','//ul[@class="list-group list-charts"]/li/a','//div[@class="panel-body content-body content-ext"]/text()'],
					#['7','http://www.83zw.com/book/44/44120/','//dl[@class="chapterlist"]/dd/a','//div[@id="chapter_content"]/text()'],
					#['8','http://www.3qzone.com/27_27023/','//div[@id="list"]/dl/dd/a','//div[@id="content"]/text()'],
					#['9','https://www.xiaoshuo.kr/30364/','//div[@class="chapterCon"]/ul/li/a','//div[@class="articleCon "]/p/text()'],
					#['10','http://www.wanxianshan.net/72347.shtml','//ul[@class="nav clearfix"]/span/a','//div[@id="content"]/text()'],
					#['11','http://www.7kzw.com/0/203/','//div[@id="list"]/dl/dd[position()>9]/a','//div[@id="content"]/text()'],
					#['12','https://www.7kshu.com/44/44507/','//ul[@id="chapterlist"]/li/a','//div[@id="content"]/text()'],
					#['13','http://www.mytxt.cc/read/17226/','//*[@class="cp_list_m62topxs"]/ol/li/a','//div[@class="detail_con_m62topxs"]/p/text()'],
					#['14','http://www.bookyyy.com/y/2955.html','//ul[@class="list-group"]/li[@class="list-group-item col-lg-3 col-md-3 col-sm-4 col-xs-6 book"]/a','//div[@class="content"]/text()'],
					#['18','http://www.3qzone.com/23_23582/','//div[@id="list"]/dl/dd/a','//div[@id="content"]/text()'],
					#['18','http://www.3qzone.com/23_23582/','//div[@id="list"]/dl/dd/a','//div[@id="content"]/text()'],
					#['19','http://www.3qzone.com/11_11948/','//div[@id="list"]/dl/dd/a','//div[@id="content"]/text()'],
					#['21','http://www.feizw.com/Html/14467/index.html','//div[@class="chapterlist"]/ul/li/a','//div[@id="content"]//text()'],
					#['23','http://www.wenxuem.com/book/60/60075/index.html','//div[@class="novel_list"]/ul/li/a','//div[@id="clickeye_content"]/text()'],
					#['24','https://www.xs74.com/novel/badaozongcaiyishenshiai/','//div[@id="list"]/dl/dd/a','//div[@id="content"]/text()'],
					#['25','http://www.xiangcunxiaoshuo.la/html/271162/','//section[@class="ml_main"]/dl/dd/a','//div[@class="yd_text2"]/text()'],
					#['26','https://www.aszw.org/book/186/186655/','//dd/table/tr/td/a','//div[@id="contents"]/text()'],
					#['27','https://www.txtjia.com/shu/5983/','//div[@class="list"]/ul/li/a','//div[@id="booktext"]/text()'],
					#['28','https://www.lewen8.com/lw130714/','//ul[@class="chapterlist"]/li/a','//div[@id="content"]/text()'],
					#['29','http://www.loxow.com/81623.shtml','//ul[@class="nav clearfix"]/span/a','//div[@id="content"]/text()'],
					#['147','http://www.99shumeng.net/shu/36/36156/index.html','//table[@class="acss"]/tr/td/a','//*[@id="content"]/text()'],							
					#['32','https://www.txtjia.com/shu/37625/','//div[@class="list"]/ul/li/a','//*[@id="booktext"]/text()'],							
					#['33','https://www.zuok.cn/chapte/14212175509153/list.htm','//div[@class="Catalog_list"]/ul/li/a','//*[@class="context"]/div[@class="text"]/p/text()'],							
					#['35','https://www.dhzw.org/book/198/198391/','//div[@id="list"]/dl/dd[position()>873]/a','//*[@id="BookText"]/text()'],							
					#['36','https://www.aszw.org/book/266/266468/','//dd/table/tr/td/a','//div[@id="contents"]/text()'],
					#['37','http://www.iyunyue.com/NovelDetail.aspx?bookid=413088','//div[@class="con_sub"]/ul/li/a','//div[@id="chapterContent"]/text()'],
					#['43','http://www.773buy.com/209_209689/','//div[@id="defaulthtml4"]/table/tr/td/div/a','//div[@id="content"]/text()'],
					#['7','http://www.lzkan.com/k/37270.html','//ul[@class="list-group"]/li/a','//div[@class="content"]/text()'],
					#['8','http://www.lzkan.com/k/5261.html','//ul[@class="list-group"]/li/a','//div[@class="content"]/text()'],
					#['9','http://www.bxwx.io/book/100129/','//dl[@class="zjlist"]/dd/a','//div[@id="content"]/text()'],
					#['19','https://www.qu.la/book/66701/','//*[@id="list"]/dl/dd[position()>12]/a','//div[@id="content"]/text()'],
					#['21','http://www.yanqing520.com/shu/187/','//div[@id="list"]/dl/dd[position()>639]/a','//div[@id="content"]/text()'],    
                    #['22','http://www.yanqing520.com/shu/3463/','//div[@id="list"]/dl/dd[position()>12]/a','//div[@id="content"]/text()'],    
                    #['23','http://www.yanqing520.com/shu/3/','//div[@id="list"]/dl/dd[position()>12]/a','//div[@id="content"]/text()'],
                    #['24','https://www.vodtw.com/Html/Book/29/29494/Index.html','//div[@id="list"]/dl/dd[position()>12]/a','//div[@id="content"]/text()'],
                    #['25','http://www.kanshuge.la/files/article/html/161/161185/index.html','//dl[@class="chapterlist"]/dd/a','//*[@id="BookText"]/text()'],
                    #['26','https://www.lewen8.com/lw64323/','//ul[@class="chapterlist"]/li/a','//div[@id="content"]/text()'], 
                    #['30','https://www.vodtw.com/html/book/45/45906/Index.html','//div[@id="list"]/dl/dd[position()>663]/a','//div[@id="content"]/text()'],
                    #['32','http://www.prwx.com/book/219361/','//div[@class="centent"]/ul[position()>1]/li/a','//div[@id="content"]/text()'],
                    #['33','https://www.aszw.org/book/253/253131/','//dd/table/tr/td/a','//div[@id="contents"]/text()'],
                    #['35','https://www.dhzw.org/book/222/222005/','//div[@id="list"]/dl/dd[position()>794]/a','//*[@id="BookText"]/text()'],
                    #['36','https://www.qu.la/book/41344/','//*[@id="list"]/dl/dd[position()>1686]/a','//div[@id="content"]/text()'],
                    #['37','http://www.paoshuba.cc/Partlist/72976/Index.shtml','//*[@id="list"]/dl/dd[position()>1314]/a','//div[@id="TXT"]/text()'],
                    #['38','https://www.wuruo.com/36/36644/','//*[@id="readerlist"]/ul/li/a','//div[@id="content"]/text()'],
                    #['39','http://www.wanben.me/xiaoshuo/44447/','//div[@class="chapterCon"]/ul/li/a','//div[@class="articleCon"]/p/text()'],
                    ['40','https://www.wuruo.com/4/4787/','//div[@id="readerlist"]/ul/li/a','//div[@id="content"]/text()'],
				]

    def start_requests(self):
        for url in self.start_urls:
        	meta ={}
        	meta['linkpath'] = url[2]
        	meta['bid'] = url[0]
        	meta['contentxpath'] = url[3]
        	headers = {
                "Referer":"https://www.wuruo.com/4/4787/",
                "Host":"www.wuruo.com",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
                #"Cookie":"__cfduid=d5c0ee4a147bf585b1e16feb3a7eabc321523510448; scrollspeed=5; yjs_id=df1854453bfd7f764b9b1db994ebd4ac; ctrl_time=1; Hm_lvt_0085604b98e8c6f9678da7a3a3354f6d=1523510449; Hm_lpvt_0085604b98e8c6f9678da7a3a3354f6d=1523510607"
        	}
        	yield scrapy.Request(url[1],callback=self.parse,meta=meta,headers=headers)
		
    def parse(self,response):
    	mysql = msyqlHelper()
    	names = set(['上架感言！'])
    	links = response.xpath(response.meta['linkpath'])
    	j = 1
    	maxcid = 1
    	for link in links:
		    name = link.xpath('text()').extract_first()
		    if name in names:
		    	continue
		    href = link.xpath('@href').extract_first()
		    #href ='/'+href;
		    next_url = urljoin(response.url,href)
		    names.add(name)
		    meta = dict()
		    meta['name'] = name
		    meta['bid'] = response.meta['bid']
		    meta['size'] = 0
		    meta['is_vip'] = 1
		    if j == 1:
		    	meta['prev_cid'] = 0
		    else:
		    	meta['prev_cid'] = 	0
		    meta['next_cid'] = 0
            
		    maxcid = maxcid+1
		    meta['sequence'] = j
		    j = j+1
		    self.logger.info('Parse url is  %s', next_url)
		    chapter_id = mysql.insert(meta)
		    meta['contentxpath'] = response.meta['contentxpath']
		    meta['id'] = chapter_id
		    headers = {
                "Referer":response.url,
                "Host":"www.wuruo.com",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
        	}
		    self.logger.info('Parse function called on dfsdfsd------------------')
		    yield scrapy.Request(next_url,callback=self.parse_content,meta=meta,headers=headers)
    	mysql.close()
    	
	    

	   
    def parse_content(self,response):
        meta = response.meta

        self.logger.info('11111111111111111111111111parse_content------------------%s',response.url)
        str = response.xpath(meta['contentxpath']).extract()
        str = filter(lambda s:s != '',str)
        newsttr = list(str)
        content = '\r\n'.join(newsttr)
        meta['content'] = content
        #with open('/mnt/hgfs/projects/newtest/python/books/b.txt','a+') as file:
        #	file.write('    '+meta['name']+"\r\n")
        #	file.write('    '+content+"\r\n")
        yield meta   
