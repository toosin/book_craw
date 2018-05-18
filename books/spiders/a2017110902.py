# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from books.mysql import msyqlHelper
class A20171013Spider(scrapy.Spider):
    name = '2017110902'
    allowed_domains = ['mywenxue.com']
    start_urls = [
					#['135','http://www.mywenxue.com/xiaoshuo/67/67741/23290533.htm','第820章 小情侣','//div[@id="chapterContent"]/p/text()'],						
					#['136','http://www.mywenxue.com/xiaoshuo/67/67854/27093629.htm','第666章身陷流沙','//div[@id="chapterContent"]/p/text()'],												
                    #['141','http://www.mywenxue.com/xiaoshuo/72/72221/25112515.htm','第555章妈妈的温暖','//div[@id="chapterContent"]/p/text()'],                                       
                    #['149','http://www.mywenxue.com/xiaoshuo/65/65466/22319969.htm','第638章 共同之处','//div[@id="chapterContent"]/p/text()'],                                       
					['862','http://www.mywenxue.com/xiaoshuo/64/64225/21846186.htm','第一千零九十章少年的奇怪行为','//div[@id="chapterContent"]/p/text()'],										
				]

    def start_requests(self):
        for url in self.start_urls:
        	meta ={}
        	meta['last_name'] = url[2]
        	meta['bid'] = url[0]
        	meta['contentxpath'] = url[3]
        	meta['sequence'] = 1;
        	meta['j'] = 1;
        	yield scrapy.Request(url[1],callback=self.parse,meta=meta)
		
    def parse(self,response):
        mysql = msyqlHelper()
        data = dict()
        meta = dict()
        data['bid'] = response.meta['bid'];
        data['size'] = 0
        data['is_vip'] = 0
        data['name'] = response.xpath('//div[@id="htmltimu"]/h2/span/text()').extract_first()

        str = response.xpath('//div[@id="chapterContent"]/p/text()').extract()
        str = filter(lambda s:s != '',str)
        newsttr = list(str)
        content = '\r\n'.join(newsttr)
        data['content'] = content
        data['size'] = len(content)
        data['sequence'] = response.meta['sequence']
        data['prev_cid'] = 0
        data['next_cid'] = 0
        chapter_id = mysql.inseraAll(data)
        self.logger.info(data);
        mysql.close()
        if data['name'] == '第一千零九十章少年的奇怪行为':
            return 
        href = response.xpath('//a[contains(.//text(), "下一页")]/@href').extract_first()
        if href is None:
            return
        meta['bid'] = 	response.meta['bid'];
        meta['sequence'] = response.meta['sequence']+1
        meta['last_name'] = response.meta['last_name']
        next_url = urljoin(response.url,href) 
        yield scrapy.Request(next_url,callback=self.parse,meta=meta)
    	