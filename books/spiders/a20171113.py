# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from books.mysql import msyqlHelper
from scrapy.http import FormRequest
import json
class A20171113Spider(scrapy.Spider):
    name = '20171113'
    allowed_domains = ['gzdushu.com','feizw.com','xiaoshuokong.com','m.bsread.com','yanqing520.com']
    start_urls = [
                    #['3','http://www.dreamersall.com/Book/Chapter/List.aspx?NovelId=5108','//dl[@class="index"]/dd/a','//div[@id="acontent"]/text()'],              
                    #['3','http://www.dreamersall.com/Book/Chapter/List.aspx?NovelId=5108','//div[@class="user-catalog-ul clearfix js-ul-pop"]/div/a','//div[@class="container user-reading-online pos-rel"]/p/text()'],                
                    #['16','https://www.luochen.com/book/9768/chapter.html','//ul[@class="clearfix chapter-list"]/li/span/a','//div[@class="article-con"]/p/text()'],                                
                    #['22','http://www.feizw.com/Html/14467/index.html','//div[@class="chapterlist"]/ul/li/a','//div[@id="content"]//text()'],                                
                    #['42','https://m.bsread.com/mulu/533.html','//ul[@class="ls bg"]/li/a','//div[@class="bookdetail"]/div[@class="bookmain"]/p/text()'],                                
                    #['18','http://www.gzdushu.com/modules/article/reader.php?aid=21','//dl[@class="index"]/dd/a','//div[@id="acontent"]/text()'], 
                     ['29','https://m.bsread.com/mulu/224.html?u=30025','//ul[@class="ls bg"]/li/a','//div[@class="bookdetail"]/div[@class="bookmain"]/p/text()'],                                
                        
                ]

    def start_requests(self):
        cookies = {
             "UM_distinctid":"162a3e6a64e89-0843b576687bb1-2e06372c-51000-162a3e6a6511a9",
            "uvip":"faaf79da50e39d893598fd8fce28cc04",
            "wgid":"1",
            "tlid":"223",
            "qdi":"1395",
            "qp":"30025",
            "id":"495059",
            "name":"user495059",
            "names":"%22user495059%22",
            "contact":"%22%5Cu91d1%5Cu5999%5Cu5999%22",
            "pic":"495059.jpg",
            "v":"1",
            "code":"9c960aa1d4b92cfa9569f26edc2cf2aa",
            "phone_unbind":"1",
            "tuid":"30025",
            "PHPSESSID":"gaa04b81clg2qj6n3qoeavmp52",
            "pindao":"b",
            "bi":"204",
            "CNZZDATA1267452641":"772678074-1523166968-%7C1524820323",
            "Hm_lvt_589e8b9ebda178159870e84dcda2b999":"1524801203",
            "Hm_lpvt_589e8b9ebda178159870e84dcda2b999":"1524821433"
        }
        headers = {
                "Referer":"https://m.bsread.com/mulu/224.html?u=30025",
                "Host":"m.bsread.com",
                "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 wechatdevtools/0.7.0 MicroMessenger/6.3.9 Language/zh_CN webview/0"
        }
        for url in self.start_urls:
            meta ={}
            meta['linkpath'] = url[2]
            meta['bid'] = url[0]
            meta['contentxpath'] = url[3]
            yield scrapy.Request(url[1],callback=self.parse,meta=meta,headers=headers,cookies=cookies)
            #yield scrapy.Request("http://www.gzdushu.com/modules/article/reader.php?aid=21",callback=self.parse,meta=meta)
        
    def parse(self,response):
        mysql = msyqlHelper()
        names = set(['上架感言！'])
        links = response.xpath(response.meta['linkpath'])

        self.logger.info(links)
        #3cookies = response.headers.getlist('Set-Cookie')
        cookies = {
             "UM_distinctid":"162a3e6a64e89-0843b576687bb1-2e06372c-51000-162a3e6a6511a9",
            "uvip":"faaf79da50e39d893598fd8fce28cc04",
            "wgid":"1",
            "tlid":"223",
            "qdi":"1395",
            "qp":"30025",
            "id":"495059",
            "name":"user495059",
            "names":"%22user495059%22",
            "contact":"%22%5Cu91d1%5Cu5999%5Cu5999%22",
            "pic":"495059.jpg",
            "v":"1",
            "code":"9c960aa1d4b92cfa9569f26edc2cf2aa",
            "phone_unbind":"1",
            "tuid":"30025",
            "PHPSESSID":"gaa04b81clg2qj6n3qoeavmp52",
            "pindao":"b",
            "bi":"204",
            "CNZZDATA1267452641":"772678074-1523166968-%7C1524820323",
            "Hm_lvt_589e8b9ebda178159870e84dcda2b999":"1524801203",
            "Hm_lpvt_589e8b9ebda178159870e84dcda2b999":"1524821433"
        }
        #headers = {
                #"Referer":"http://www.sxyj.net/Book_Read/bookId_4dc9650165c6405f9219947466176978/chapterId_465531889b8648c0a26ec775eeda2056.html"
        #}    
        j = 1
        #meta = dict()
        #meta['contentxpath'] = response.meta['contentxpath']
        #yield scrapy.Request("http://www.sxyj.net/WebApi/Book/GetChapter?bookId=4dc9650165c6405f9219947466176978&chapterId=465531889b8648c0a26ec775eeda2056",callback=self.parse_content,meta=meta,cookies=cookies,headers=headers)
        #return;
        maxcid = 1
        for link in links:
            name = link.xpath('text()').extract_first()
            if name in names:
                continue

            href = link.xpath('@href').extract_first()
            hrefArr = href.split('/')
            #BookId = hrefArr[2][7:]
            #ChapterIds = hrefArr[3][10:-5]
            next_url = urljoin(response.url,href)
            self.logger.info(name)
            meta = dict()
            meta['name'] = name
            #chapter = mysql.getByBidAndName(name,18)
            #content = chapter.get('content')
            #self.logger.info(chapter);
            #if content != '':
            #   continue

            #self.logger.info("--------name is %s" % name)
            meta['bid'] = response.meta['bid']
            meta['size'] = 0
            meta['is_vip'] = 1
            if j == 1:
                meta['prev_cid'] = 0
            else:
                meta['prev_cid'] =  0
            meta['next_cid'] = 0
            
            
            self.logger.info("-------enter-222-------------enter---2222-----------enter---222----")    
            maxcid = maxcid+1
            meta['sequence'] = j
            
            j = j+1
            self.logger.info('----name-is:%s---url-is:%s'% (name,next_url))    
           
            headers = {
                "Referer":response.url,
                "Host":"m.bsread.com",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
            }    
            self.logger.info('Parse url is  %s', next_url)
            if j<=11:
                continue
            chapter_id = mysql.insert(meta)
            #chapter_id = chapter.get('id')
            meta['contentxpath'] = response.meta['contentxpath']
            meta['id'] = chapter_id
            self.logger.info('Parse function called on dfsdfsd------------------')
            #temp = "http://www.sxyj.net/WebApi/Book/GetChapter?bookId=%s&chapterId=%s" % (BookId,ChapterIds)
            #yield scrapy.Request(next_url,callback=self.parse_content,meta=meta,cookies=cookies,headers=headers)
            aid = href.split('/')[2][0:-5]
            
            formdata={"act":"gView","bid":'224',"aid":aid}
            self.logger.info(formdata)
            yield scrapy.FormRequest(url='https://m.bsread.com/wx/s.php',formdata=formdata,headers=headers,callback=self.parse_content2,cookies=cookies,meta=meta)
        mysql.close()
        
        

       
    def parse_content(self,response):
        #self.logger.info(response.body)

        meta = response.meta
        #self.logger.info(response.text)
        #res = json.loads(response.text)
        self.logger.info('parse_content parse_content parse_content on parse_content------------------%s',response.url)
        str = response.xpath(meta['contentxpath']).extract()
        str = filter(lambda s:s != '',str)
        newsttr = list(str)
        content = '\r\n'.join(newsttr)
        meta['content'] = content
        yield meta  

    def parse_content2(self,response):
        #self.logger.info(response.body)

        meta = response.meta
        #self.logger.info(response.text)
        res = json.loads(response.text)
        self.logger.info(res)
        content = res[2]
        content = self.a(content)
        meta['content'] = content
        yield meta
    def a(self,text):
        b = text.strip('\\').split('\\')
        t = ''
        for i in b:
            t = t+chr(int(i,22))
        return t          
