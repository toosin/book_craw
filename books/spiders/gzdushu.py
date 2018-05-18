# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from books.mysql import msyqlHelper
from scrapy.http import FormRequest
import json
class A20171113Spider(scrapy.Spider):
    name = 'gzdushu'
    allowed_domains = ['gzdushu.com','yunshuge.com']
    start_urls = [
                    #['3','http://www.dreamersall.com/Book/Chapter/List.aspx?NovelId=5108','//dl[@class="index"]/dd/a','//div[@id="acontent"]/text()'],              
                    #['3','http://www.dreamersall.com/Book/Chapter/List.aspx?NovelId=5108','//div[@class="user-catalog-ul clearfix js-ul-pop"]/div/a','//div[@class="container user-reading-online pos-rel"]/p/text()'],                
                    #['16','https://www.luochen.com/book/9768/chapter.html','//ul[@class="clearfix chapter-list"]/li/span/a','//div[@class="article-con"]/p/text()'],                                
                    #['22','http://www.feizw.com/Html/14467/index.html','//div[@class="chapterlist"]/ul/li/a','//div[@id="content"]//text()'],                                
                    #['42','https://m.bsread.com/mulu/533.html','//ul[@class="ls bg"]/li/a','//div[@class="bookdetail"]/div[@class="bookmain"]/p/text()'],                                
                    #['18','http://www.gzdushu.com/modules/article/reader.php?aid=21','//dl[@class="index"]/dd/a','//div[@id="acontent"]/text()'],                                       
                    #['31','http://m.gzdushu.com/modules/article/reader.php?aid=287','//dl[@class="index"]/dd/a','//div[@id="acontent"]/text()'],                                       
                    #['31','http://m.gzdushu.com/modules/article/reader.php?aid=287','//dl[@class="index"]/dd/a','//div[@id="acontent"]/text()'],                                       
                    #['31','http://m.gzdushu.com/modules/article/reader.php?aid=287','//dl[@class="index"]/dd/a','//div[@id="acontent"]/text()'],                                       
                    ['34','https://yomeng.yunshuge.com/chapter/13540/?page=12','//ul[@class="clearfix"]/li/a','//div[@class="reader_page_content  reader_page_font_size1"]/p/text()'],                                       
                ]

    def start_requests(self):
        cookies = {
             "jieqiVisitInfo":"jieqiUserLogin%3D1525764839%2CjieqiUserId%3D123189",
             "read_pagenum":"1",
             "jieqiWapPsize":"-11",
             "shuhai_history_":"%5B%7B%22aid%22%3A%2211817%22%2C%22cid%22%3A1230652%2C%22aname%22%3A%22%25CE%25D2%25C4%25C3%25CA%25B1%25B9%25E2%25BB%25BB%25C4%25E3%25D2%25BB%25CA%25C0%25B3%25D5%25C3%25D4%22%2C%22autname%22%3A%22%25CA%25A2%25C9%25D9%22%2C%22asort%22%3A%22%25CF%25D6%25B4%25FA%25D1%25D4%25C7%25E9%22%2C%22cname%22%3A%22%2B%25B5%25DA5%25D5%25C2%2B%25D7%25ED%25BE%25C6%25B6%25D4%25BF%25B9%22%2C%22siteid%22%3Anull%2C%22sortid%22%3A%22111%22%7D%2C%7B%22aid%22%3A%2213540%22%2C%22cid%22%3A2053135%2C%22aname%22%3A%22%25CE%25AA%25C4%25E3%25C4%25A8%25C8%25A5%25D2%25BB%25CA%25C0%25B3%25BE%25B0%25A3%22%2C%22autname%22%3A%22%25BE%25FD%25D6%25B9%25B9%25E9%22%2C%22asort%22%3A%22%25C7%25E0%25B4%25BA%25D0%25A3%25D4%25B0%22%2C%22cname%22%3A%22%2B%25B5%25DA050%25D5%25C2%2526nbsp%253B%2526nbsp%253B%25CB%25AF%25BE%25F5%25CA%25C7%25B8%25F6%25CE%25CA%25CC%25E2%22%2C%22siteid%22%3Anull%2C%22sortid%22%3A%22101%22%7D%5D",
             "PHPSESSID":"1ff197c95d71a9d38021cdf0ccff1508"
        }
        headers = {
                "Referer":"https://yomeng.yunshuge.com/chapter/13540/?page=12",
                "Host":"yomeng.yunshuge.com",
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
        names = set()
        links = response.xpath(response.meta['linkpath'])

        self.logger.info(links)
        #3cookies = response.headers.getlist('Set-Cookie')
        cookies = {
             "jieqiVisitInfo":"jieqiUserLogin%3D1525764839%2CjieqiUserId%3D123189",
             "read_pagenum":"1",
             "jieqiWapPsize":"-11",
             "shuhai_history_":"%5B%7B%22aid%22%3A%2211817%22%2C%22cid%22%3A1230652%2C%22aname%22%3A%22%25CE%25D2%25C4%25C3%25CA%25B1%25B9%25E2%25BB%25BB%25C4%25E3%25D2%25BB%25CA%25C0%25B3%25D5%25C3%25D4%22%2C%22autname%22%3A%22%25CA%25A2%25C9%25D9%22%2C%22asort%22%3A%22%25CF%25D6%25B4%25FA%25D1%25D4%25C7%25E9%22%2C%22cname%22%3A%22%2B%25B5%25DA5%25D5%25C2%2B%25D7%25ED%25BE%25C6%25B6%25D4%25BF%25B9%22%2C%22siteid%22%3Anull%2C%22sortid%22%3A%22111%22%7D%2C%7B%22aid%22%3A%2213540%22%2C%22cid%22%3A2053135%2C%22aname%22%3A%22%25CE%25AA%25C4%25E3%25C4%25A8%25C8%25A5%25D2%25BB%25CA%25C0%25B3%25BE%25B0%25A3%22%2C%22autname%22%3A%22%25BE%25FD%25D6%25B9%25B9%25E9%22%2C%22asort%22%3A%22%25C7%25E0%25B4%25BA%25D0%25A3%25D4%25B0%22%2C%22cname%22%3A%22%2B%25B5%25DA050%25D5%25C2%2526nbsp%253B%2526nbsp%253B%25CB%25AF%25BE%25F5%25CA%25C7%25B8%25F6%25CE%25CA%25CC%25E2%22%2C%22siteid%22%3Anull%2C%22sortid%22%3A%22101%22%7D%5D",
             "PHPSESSID":"1ff197c95d71a9d38021cdf0ccff1508"
        }
        #headers = {
                #"Referer":"http://www.sxyj.net/Book_Read/bookId_4dc9650165c6405f9219947466176978/chapterId_465531889b8648c0a26ec775eeda2056.html"
        #}    
        j = 317
        #meta = dict()
        #meta['contentxpath'] = response.meta['contentxpath']
        #yield scrapy.Request("http://www.sxyj.net/WebApi/Book/GetChapter?bookId=4dc9650165c6405f9219947466176978&chapterId=465531889b8648c0a26ec775eeda2056",callback=self.parse_content,meta=meta,cookies=cookies,headers=headers)
        #return;
        maxcid = 1
        for link in links:
            name = link.xpath('text()').extract_first()

            href = link.xpath('@href').extract_first()
            hrefArr = href.split('/')
            #BookId = hrefArr[2][7:]
            #ChapterIds = hrefArr[3][10:-5]
            next_url = urljoin(response.url,href)
            self.logger.info(name)
            meta = dict()
            meta['name'] = name

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
                "Host":"yomeng.yunshuge.com",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
            }    
            self.logger.info('Parse url is  %s', next_url)

            chapter_id = mysql.insert(meta)
            #chapter_id = chapter.get('id')
            meta['contentxpath'] = response.meta['contentxpath']
            meta['id'] = chapter_id
            self.logger.info('Parse function called on dfsdfsd------------------')
            #temp = "http://www.sxyj.net/WebApi/Book/GetChapter?bookId=%s&chapterId=%s" % (BookId,ChapterIds)
            yield scrapy.Request(next_url,callback=self.parse_content,meta=meta,cookies=cookies,headers=headers)
            #aid = href.split('/')[2][0:-5]
            break;
            #formdata={"act":"gView","bid":'224',"aid":aid}
            #self.logger.info(formdata)
            #yield scrapy.FormRequest(url='https://m.bsread.com/wx/s.php',formdata=formdata,headers=headers,callback=self.parse_content2,cookies=cookies,meta=meta)
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
