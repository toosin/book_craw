# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from books.mysql import msyqlHelper
class vodtwSpider(scrapy.Spider):
    name = 'vodtw'
    allowed_domains = ['vodtw.com','kanshuge.la']
    start_urls = [
                    #['165','http://www.vodtw.com/html/book/37/37412/','//div[@class="insert_list"]/dl/dd/ul/li/a','//*[@id="BookText"]/p/text()'],              
                    #['24','https://www.vodtw.com/Html/Book/29/29494/Index.html','//div[@class="insert_list"]/dl/dd/ul/li/a','//*[@id="BookText"]/p/text()'],                   
                    ['30','https://www.vodtw.com/html/book/45/45906/Index.html','//div[@class="insert_list"]/dl/dd/ul/li[position()>663]/a','//*[@id="BookText"]/p/text()'],                   
                ]

    def start_requests(self):
        for url in self.start_urls:
            meta ={}
            meta['linkpath'] = url[2]
            meta['bid'] = url[0]
            meta['contentxpath'] = url[3]
            yield scrapy.Request(url[1],callback=self.parse,meta=meta)
        
    def parse(self,response):

        mysql = msyqlHelper()
        names = set(['上架感言！'])
        links = response.xpath(response.meta['linkpath'])
        #self.logger.info('dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd')
        #self.logger.info(links)
        j = 1
        maxcid = 1
        for link in links:
            name = link.xpath('text()').extract_first()
            if name in names:
                continue
            href = link.xpath('@href').extract_first()
            next_url = urljoin(response.url,href)
            #names.add(name)
            meta = dict()
            meta['name'] = name
            meta['bid'] = response.meta['bid']
            meta['size'] = 0
            meta['is_vip'] = 1
            if j == 1:
                meta['prev_cid'] = 0
            else:
                meta['prev_cid'] =     0
            meta['next_cid'] = 0
            
            maxcid = maxcid+1
            meta['sequence'] = j
            j = j+1
            self.logger.info('Parse url is  %s', next_url)
            chapter_id = mysql.insert(meta)
            meta['contentxpath'] = response.meta['contentxpath']
            meta['id'] = chapter_id
            self.logger.info('next url is %s------------------' % next_url)
            headers = {
                "Referer":response.url,
                "Host":"www.vodtw.com",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
            }
            yield scrapy.Request(next_url,callback=self.parse_content,meta=meta,headers=headers)
        mysql.close()
        
        

       
    def parse_content(self,response):
        #mysql = msyqlHelper()
        meta = response.meta

        self.logger.info('parse_content parse_content parse_content on parse_content------------------%s',response.url)
        str = response.xpath(meta['contentxpath']).extract()
        str = filter(lambda s:s != '',str)
        newsttr = list(str)
        content = '\r\n'.join(newsttr)
        meta['content'] = content
        #mysql.updateChapter(meta)
        #mysql.close()
        yield meta   
