# -*- coding: utf-8 -*-
import scrapy
import json
from books.mysql import msyqlHelper
class UrlsjoinSpider(scrapy.Spider):
    name = 'urlsjoin'
    allowed_domains = ['m.iyunyue.com','hgread.com']
    #start_urls = ['http://m.iyunyue.com/inter/ChapterListService.aspx?cmd=GETCHAPTERLIST&bookid=413088&pi=2&ps=305']
    start_urls = ['http://www.hgread.com/chapter/203228.html']
     


    def start_requests(self):
        cookies = {
            "cloud_qiangqian":"1",
            "ASP.NET_SessionId":"mlvxncjrp2tj4bck1hhngkxj",
            "UM_distinctid":"162b3a4eac32cb-056cf6396bf4f2-b34356b-1fa400-162b3a4eac4d8"
        }
        headers = {
                "Referer":self.start_urls[0],
                "Host":"www.hgread.com",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
        }

        yield scrapy.Request(self.start_urls[0],callback=self.parse,headers=headers)

    def parse(self, response):
        mysql = msyqlHelper()
        #txt = json.loads(response.body)
        #self.logger.info(txt)
        #return;
        chapters = response.xpath('//ul[@class="t-list"]/li[position()>86]/a')
        i = 300;
        cookies = {
            "Hm_lvt_b7a5349c0dc4d90da89e89cc58ee99da":1523950381,
            "UserItem_HGREAD_7040":"%7b%22UserId%22%3a2699411%2c%22OpenId%22%3a%22951678%22%2c%22AccessToken%22%3a%229E8E5C106BF94A14BE3760E3A5D1483F%22%2c%22RefreshToken%22%3a%2255DB88B286834E26A4DC66776E770537%22%2c%22ExpiresIn%22%3a1200%2c%22NickName%22%3a%22jinmincc%22%2c%22QQNo%22%3a%22%22%2c%22EMail%22%3a%22%22%2c%22Gender%22%3anull%2c%22IntroSelf%22%3a%22%22%2c%22HeadImgUrl%22%3a%22%22%2c%22UDate%22%3a%22%5c%2fDate(-62135596800000)%5c%2f%22%2c%22NewGuid%22%3anull%2c%22SumAmount%22%3a978%2c%22GiveSumAmount%22%3a0%2c%22GiveLoseTime%22%3a%22%5c%2fDate(-62135596800000)%5c%2f%22%2c%22VipScore%22%3a0%2c%22VipLoseScore%22%3a0%2c%22VipGrowth%22%3a0%2c%22VipLoseTime%22%3a%22%5c%2fDate(-62135596800000)%5c%2f%22%2c%22SVipLoseTime%22%3a%22%5c%2fDate(-62135596800000)%5c%2f%22%2c%22IsVip%22%3afalse%2c%22IsSVip%22%3afalse%2c%22VipTag%22%3a%22VIP%22%2c%22ScoreLevel%22%3a0%2c%22GrowthLevel%22%3a0%2c%22VipDiscount%22%3a1.000%2c%22TpOpenId%22%3anull%2c%22TpExpiresTime%22%3a0%7d",
            "USER_INFO_ACCESS_TOKEN":"EcXxcJEdDjsPKbanpdVAApnGhUOfe2RFwP9PRlNa2owtfVn9CvkMDQ==",
            "USER_INFO_EXPIRES_IN":"BSQWOyR09yo=",
            "USER_INFO_REFRESH_TOKEN":"RzYHBqus6gbGAgWeBK9D2LGd0IDtcKpO5/2zUwFRI2daAc3oHqA1ww==",
            "Hm_lpvt_b7a5349c0dc4d90da89e89cc58ee99da":1523950925
        }
        #(`bid`, `name`,`sequence`,`size`,`is_vip`,`prev_cid`,`next_cid`,`recent_update_at`,`created_at`,`updated_at`)
        for chapter in chapters:
            link_info = chapter.xpath('@href').extract_first()
            name = chapter.xpath('text()').extract_first()
            link = link_info.split('/')
            #self.logger.info(link)
            headers = {
                "Referer":response.url,
                "Host":"www.hgread.com",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
            }
            meta = {}
            meta['bid'] = 45
            meta['name'] = name
            meta['sequence'] = i
            meta['size'] = 0
            meta['is_vip'] = 0
            meta['prev_cid'] = 0
            meta['next_cid'] = 0
            chapter_id = mysql.insert(meta)
            meta['id'] = chapter_id
            i = i+1;
            if i >= 500:
                break;
            url_t = 'http://www.hgread.com/home/OBookApiAgent?action=Chapter&bookId=%s&chapterId=%s' % (link[2],link[3][0:-5])
            #self.logger.info(meta)   
            #url_format = 'http://m.iyunyue.com/inter/ChapterService.aspx?cmd=getchaptercontent&from=&iswx=0&bookid=413088&chapterid=%s' % (chapter['chapterId'],)
            yield scrapy.Request(url_t,callback=self.parse_content,meta=meta,cookies=cookies,headers=headers)
        mysql.close()


    def  parse_content(self,response):
        meta = response.meta
        txt = json.loads(response.body) 
        meta['content'] = txt['data']['textContent']
        self.logger.info(meta)
        yield meta
