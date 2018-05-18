# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from books.mysql import msyqlHelper
from scrapy.selector import Selector
class Other2Spider(scrapy.Spider):
    name = 'other2'
    allowed_domains = ['xiashu.cc']
    start_urls = [		
					['144','https://www.xiashu.cc/141233/','//*[@id="at"]/tr/td/a','//div[@id="chaptercontent"]/text()'],				
				]
    temp = '''
	<li><a href="/141233/read_9.html" title="第9章 起程去金钟县" target="_blank" rel="nofollow">第9章 起程去金钟县</a><span class="time">08-11</span></li><li><a href="/141233/read_10.html" title="第10章 张家村" target="_blank" rel="nofollow">第10章 张家村</a><span class="time">08-11</span></li><li><a href="/141233/read_11.html" title="第11章 走进四明山" target="_blank" rel="nofollow">第11章 走进四明山</a><span class="time">08-11</span></li><li><a href="/141233/read_12.html" title="第12章 封月" target="_blank" rel="nofollow">第12章 封月</a><span class="time">08-11</span></li><li><a href="/141233/read_13.html" title="第13章 背上的人" target="_blank" rel="nofollow">第13章 背上的人</a><span class="time">08-11</span></li><li><a href="/141233/read_14.html" title="第14章 封泽，帮忙捉个鬼呗" target="_blank" rel="nofollow">第14章 封泽，帮忙捉个鬼呗</a><span class="time">08-11</span></li><li><a href="/141233/read_15.html" title="第15章 验尸" target="_blank" rel="nofollow">第15章 验尸</a><span class="time">08-11</span></li><li><a href="/141233/read_16.html" title="第16章 疑犯失踪" target="_blank" rel="nofollow">第16章 疑犯失踪</a><span class="time">08-11</span></li><li><a href="/141233/read_17.html" title="第17章 养尸" target="_blank" rel="nofollow">第17章 养尸</a><span class="time">08-11</span></li><li><a href="/141233/read_18.html" title="第18章 生辰八字里的秘密" target="_blank" rel="nofollow">第18章 生辰八字里的秘密</a><span class="time">08-11</span></li><li><a href="/141233/read_19.html" title="第19章 行僵" target="_blank" rel="nofollow">第19章 行僵</a><span class="time">08-11</span></li><li><a href="/141233/read_20.html" title="第20章 与僵尸对战" target="_blank" rel="nofollow">第20章 与僵尸对战</a><span class="time">08-11</span></li><li><a href="/141233/read_21.html" title="【关于耽美的那些事】" target="_blank" rel="nofollow">【关于耽美的那些事】</a><span class="time">08-11</span></li><li><a href="/141233/read_22.html" title="第21章 医院里" target="_blank" rel="nofollow">第21章 医院里</a><span class="time">08-11</span></li><li><a href="/141233/read_23.html" title="第22章 这种事我懂" target="_blank" rel="nofollow">第22章 这种事我懂</a><span class="time">08-11</span></li><li><a href="/141233/read_24.html" title="第23章 还没结束" target="_blank" rel="nofollow">第23章 还没结束</a><span class="time">08-11</span></li><li><a href="/141233/read_25.html" title="第24章 方遇白" target="_blank" rel="nofollow">第24章 方遇白</a><span class="time">08-11</span></li><li><a href="/141233/read_26.html" title="第25章 华亭山上" target="_blank" rel="nofollow">第25章 华亭山上</a><span class="time">08-11</span></li><li><a href="/141233/read_27.html" title="第26章 再遇行僵" target="_blank" rel="nofollow">第26章 再遇行僵</a><span class="time">08-11</span></li><li><a href="/141233/read_28.html" title="第27章 对战" target="_blank" rel="nofollow">第27章 对战</a><span class="time">08-11</span></li><li><a href="/141233/read_29.html" title="第28章 山里一夜" target="_blank" rel="nofollow">第28章 山里一夜</a><span class="time">08-11</span></li><li><a href="/141233/read_30.html" title="第29章 齐振" target="_blank" rel="nofollow">第29章 齐振</a><span class="time">08-11</span></li><li><a href="/141233/read_31.html" title="第30章 汪家的秘密" target="_blank" rel="nofollow">第30章 汪家的秘密</a><span class="time">08-11</span></li><li><a href="/141233/read_32.html" title="第31章 借命" target="_blank" rel="nofollow">第31章 借命</a><span class="time">08-11</span></li><li><a href="/141233/read_33.html" title="第32章 重遇故友" target="_blank" rel="nofollow">第32章 重遇故友</a><span class="time">08-11</span></li><li><a href="/141233/read_34.html" title="第33章 误入山村" target="_blank" rel="nofollow">第33章 误入山村</a><span class="time">08-11</span></li><li><a href="/141233/read_35.html" title="第34章 失去联络" target="_blank" rel="nofollow">第34章 失去联络</a><span class="time">08-11</span></li><li><a href="/141233/read_36.html" title="第35章 争执" target="_blank" rel="nofollow">第35章 争执</a><span class="time">08-11</span></li><li><a href="/141233/read_37.html" title="第36章 都太诡异了" target="_blank" rel="nofollow">第36章 都太诡异了</a><span class="time">08-11</span></li><li><a href="/141233/read_38.html" title="第37章 真正的鬼" target="_blank" rel="nofollow">第37章 真正的鬼</a><span class="time">08-11</span></li><li><a href="/141233/read_39.html" title="第38章 蝴蝶效应" target="_blank" rel="nofollow">第38章 蝴蝶效应</a><span class="time">08-11</span></li><li><a href="/141233/read_40.html" title="第39章 阴阳眼" target="_blank" rel="nofollow">第39章 阴阳眼</a><span class="time">08-11</span></li><li><a href="/141233/read_41.html" title="第40章 尘归尘，土归土" target="_blank" rel="nofollow">第40章 尘归尘，土归土</a><span class="time">08-11</span></li><li><a href="/141233/read_42.html" title="第41章 回家了" target="_blank" rel="nofollow">第41章 回家了</a><span class="time">08-11</span></li><li><a href="/141233/read_43.html" title="第42章 偶遇和重逢" target="_blank" rel="nofollow">第42章 偶遇和重逢</a><span class="time">08-11</span></li><li><a href="/141233/read_44.html" title="第43章 这个人" target="_blank" rel="nofollow">第43章 这个人</a><span class="time">08-11</span></li><li><a href="/141233/read_45.html" title="第44章 这是吃醋吗" target="_blank" rel="nofollow">第44章 这是吃醋吗</a><span class="time">08-11</span></li><li><a href="/141233/read_46.html" title="第45章 小区闹鬼" target="_blank" rel="nofollow">第45章 小区闹鬼</a><span class="time">08-11</span></li><li><a href="/141233/read_47.html" title="第46章 鬼婴" target="_blank" rel="nofollow">第46章 鬼婴</a><span class="time">08-11</span></li><li><a href="/141233/read_48.html" title="第47章 这人情商负数" target="_blank" rel="nofollow">第47章 这人情商负数</a><span class="time">08-11</span></li><li><a href="/141233/read_49.html" title="第48章 吃醋太明显" target="_blank" rel="nofollow">第48章 吃醋太明显</a><span class="time">08-11</span></li><li><a href="/141233/read_50.html" title="第49章 女鬼" target="_blank" rel="nofollow">第49章 女鬼</a><span class="time">08-11</span></li><li><a href="/141233/read_51.html" title="第50章 跟女鬼做交易" target="_blank" rel="nofollow">第50章 跟女鬼做交易</a><span class="time">08-11</span></li><li><a href="/141233/read_52.html" title="第51章 家常" target="_blank" rel="nofollow">第51章 家常</a><span class="time">08-11</span></li><li><a href="/141233/read_53.html" title="第52章 获得召唤“兽”" target="_blank" rel="nofollow">第52章 获得召唤“兽”</a><span class="time">08-11</span></li><li><a href="/141233/read_54.html" title="第53章 这一刻的心动" target="_blank" rel="nofollow">第53章 这一刻的心动</a><span class="time">08-11</span></li><li><a href="/141233/read_55.html" title="第54章 罗珊的目的" target="_blank" rel="nofollow">第54章 罗珊的目的</a><span class="time">08-11</span></li><li><a href="/141233/read_56.html" title="第55章 真正的方遇白" target="_blank" rel="nofollow">第55章 真正的方遇白</a><span class="time">08-11</span></li><li><a href="/141233/read_57.html" title="第56章 谁相亲" target="_blank" rel="nofollow">第56章 谁相亲</a><span class="time">08-11</span></li><li><a href="/141233/read_58.html" title="第57章 就这么霸道" target="_blank" rel="nofollow">第57章 就这么霸道</a><span class="time">08-11</span></li><li><a href="/141233/read_59.html" title="第58章 送行" target="_blank" rel="nofollow">第58章 送行</a><span class="time">08-11</span></li><li><a href="/141233/read_60.html" title="第59章 活人死灵" target="_blank" rel="nofollow">第59章 活人死灵</a><span class="time">08-11</span></li><li><a href="/141233/read_61.html" title="第60章 酒吧意外" target="_blank" rel="nofollow">第60章 酒吧意外</a><span class="time">08-11</span></li><li><a href="/141233/read_62.html" title="第61章 这一年最后一天" target="_blank" rel="nofollow">第61章 这一年最后一天</a><span class="time">08-11</span></li><li><a href="/141233/read_63.html" title="第62章 有我陪着你" target="_blank" rel="nofollow">第62章 有我陪着你</a><span class="time">08-11</span></li><li><a href="/141233/read_64.html" title="第63章 执勤" target="_blank" rel="nofollow">第63章 执勤</a><span class="time">08-11</span></li><li><a href="/141233/read_65.html" title="第64章 废弃的卖场" target="_blank" rel="nofollow">第64章 废弃的卖场</a><span class="time">08-11</span></li><li><a href="/141233/read_66.html" title="第65章 失踪" target="_blank" rel="nofollow">第65章 失踪</a><span class="time">08-11</span></li><li><a href="/141233/read_67.html" title="第66章 天生倒霉啊" target="_blank" rel="nofollow">第66章 天生倒霉啊</a><span class="time">08-11</span></li><li><a href="/141233/read_68.html" title="第67章 是人是鬼" target="_blank" rel="nofollow">第67章 是人是鬼</a><span class="time">08-11</span></li><li><a href="/141233/read_69.html" title="第68章 以吻渡灵" target="_blank" rel="nofollow">第68章 以吻渡灵</a><span class="time">08-11</span></li><li><a href="/141233/read_70.html" title="第69章 我们好像不一样了" target="_blank" rel="nofollow">第69章 我们好像不一样了</a><span class="time">08-11</span></li><li><a href="/141233/read_71.html" title="第70章 出乎意料之举" target="_blank" rel="nofollow">第70章 出乎意料之举</a><span class="time">08-11</span></li><li><a href="/141233/read_72.html" title="第71章 更近一步" target="_blank" rel="nofollow">第71章 更近一步</a><span class="time">08-11</span></li><li><a href="/141233/read_73.html" title="第72章 过来" target="_blank" rel="nofollow">第72章 过来</a><span class="time">08-11</span></li><li><a href="/141233/read_74.html" title="第73章 罗珊之死" target="_blank" rel="nofollow">第73章 罗珊之死</a><span class="time">08-11</span></li><li><a href="/141233/read_75.html" title="第74章 枪击案" target="_blank" rel="nofollow">第74章 枪击案</a><span class="time">08-11</span></li><li><a href="/141233/read_76.html" title="第75章 幕后的人" target="_blank" rel="nofollow">第75章 幕后的人</a><span class="time">08-11</span></li><li><a href="/141233/read_77.html" title="第76章 霸道的吻" target="_blank" rel="nofollow">第76章 霸道的吻</a><span class="time">08-11</span></li><li><a href="/141233/read_78.html" title="第77章 杨东是谁" target="_blank" rel="nofollow">第77章 杨东是谁</a><span class="time">08-11</span></li><li><a href="/141233/read_79.html" title="第78章 起疑" target="_blank" rel="nofollow">第78章 起疑</a><span class="time">08-11</span></li><li><a href="/141233/read_80.html" title="第79章 警告" target="_blank" rel="nofollow">第79章 警告</a><span class="time">08-11</span></li><li><a href="/141233/read_81.html" title="第80章 百鬼夜游" target="_blank" rel="nofollow">第80章 百鬼夜游</a><span class="time">08-11</span></li><li><a href="/141233/read_82.html" title="第81章 女战神江若" target="_blank" rel="nofollow">第81章 女战神江若</a><span class="time">08-11</span></li><li><a href="/141233/read_83.html" title="第82章 因为我在这里" target="_blank" rel="nofollow">第82章 因为我在这里</a><span class="time">08-11</span></li><li><a href="/141233/read_84.html" title="第83章 出发龙泉岭" target="_blank" rel="nofollow">第83章 出发龙泉岭</a><span class="time">08-11</span></li><li><a href="/141233/read_85.html" title="第84章 传言" target="_blank" rel="nofollow">第84章 传言</a><span class="time">08-11</span></li><li><a href="/141233/read_86.html" title="第85章 保持距离" target="_blank" rel="nofollow">第85章 保持距离</a><span class="time">08-11</span></li><li><a href="/141233/read_87.html" title="第86章 出发去景区" target="_blank" rel="nofollow">第86章 出发去景区</a><span class="time">08-11</span></li><li><a href="/141233/read_88.html" title="第87章 追查案件" target="_blank" rel="nofollow">第87章 追查案件</a><span class="time">08-11</span></li><li><a href="/141233/read_89.html" title="第88章 古战场遗迹" target="_blank" rel="nofollow">第88章 古战场遗迹</a><span class="time">08-11</span></li><li><a href="/141233/read_90.html" title="第89章 诡异坟地" target="_blank" rel="nofollow">第89章 诡异坟地</a><span class="time">08-11</span></li><li><a href="/141233/read_91.html" title="第90章 失踪真相" target="_blank" rel="nofollow">第90章 失踪真相</a><span class="time">08-11</span></li><li><a href="/141233/read_92.html" title="第91章 有鬼" target="_blank" rel="nofollow">第91章 有鬼</a><span class="time">08-11</span></li><li><a href="/141233/read_93.html" title="第92章 再次出现" target="_blank" rel="nofollow">第92章 再次出现</a><span class="time">08-11</span></li><li><a href="/141233/read_94.html" title="第93章 追踪" target="_blank" rel="nofollow">第93章 追踪</a><span class="time">08-11</span></li><li><a href="/141233/read_95.html" title="第94章 陷阱" target="_blank" rel="nofollow">第94章 陷阱</a><span class="time">08-11</span></li><li><a href="/141233/read_96.html" title="第95章 危急时刻" target="_blank" rel="nofollow">第95章 危急时刻</a><span class="time">08-11</span></li><li><a href="/141233/read_97.html" title="第96章 迷心之术" target="_blank" rel="nofollow">第96章 迷心之术</a><span class="time">08-11</span></li><li><a href="/141233/read_98.html" title="第97章 奇怪的洞穴" target="_blank" rel="nofollow">第97章 奇怪的洞穴</a><span class="time">08-11</span></li><li><a href="/141233/read_99.html" title="第98章 活死人" target="_blank" rel="nofollow">第98章 活死人</a><span class="time">08-11</span></li><li><a href="/141233/read_100.html" title="第99章 命悬一刻的时候" target="_blank" rel="nofollow">第99章 命悬一刻的时候</a><span class="time">08-11</span></li><li><a href="/141233/read_101.html" title="第100章 下山" target="_blank" rel="nofollow">第100章 下山</a><span class="time">08-11</span></li><li><a href="/141233/read_102.html" title="第101章 夜合的心结" target="_blank" rel="nofollow">第101章 夜合的心结</a><span class="time">08-11</span></li><li><a href="/141233/read_103.html" title="第102章 怀疑" target="_blank" rel="nofollow">第102章 怀疑</a><span class="time">08-11</span></li><li><a href="/141233/read_104.html" title="第103章 江若的异常" target="_blank" rel="nofollow">第103章 江若的异常</a><span class="time">08-11</span></li><li><a href="/141233/read_105.html" title="第104章 古玩店" target="_blank" rel="nofollow">第104章 古玩店</a><span class="time">08-11</span></li><li><a href="/141233/read_106.html" title="第105章 线索" target="_blank" rel="nofollow">第105章 线索</a><span class="time">08-11</span></li><li><a href="/141233/read_107.html" title="第106章 恶灵肆虐" target="_blank" rel="nofollow">第106章 恶灵肆虐</a><span class="time">08-11</span></li><li><a href="/141233/read_108.html" title="第107章 一波又一波的危险" target="_blank" rel="nofollow">第107章 一波又一波的危险</a><span class="time">08-11</span></li><li><a href="/141233/read_109.html" title="第108章 超渡罗珊" target="_blank" rel="nofollow">第108章 超渡罗珊</a><span class="time">08-11</span></li><li><a href="/141233/read_110.html" title="第109章 方旭晨失常" target="_blank" rel="nofollow">第109章 方旭晨失常</a><span class="time">08-11</span></li><li><a href="/141233/read_111.html" title="第110章 跟踪陈鸿" target="_blank" rel="nofollow">第110章 跟踪陈鸿</a><span class="time">08-11</span></li><li><a href="/141233/read_112.html" title="第111章 江若的过去" target="_blank" rel="nofollow">第111章 江若的过去</a><span class="time">08-11</span></li><li><a href="/141233/read_113.html" title="第112章 你当小偷了？" target="_blank" rel="nofollow">第112章 你当小偷了？</a><span class="time">08-11</span></li><li><a href="/141233/read_114.html" title="第113章 古董店失窃" target="_blank" rel="nofollow">第113章 古董店失窃</a><span class="time">08-11</span></li><li><a href="/141233/read_115.html" title="第114章 这一切的根源" target="_blank" rel="nofollow">第114章 这一切的根源</a><span class="time">08-11</span></li><li><a href="/141233/read_116.html" title="第115章 顺路" target="_blank" rel="nofollow">第115章 顺路</a><span class="time">08-11</span></li><li><a href="/141233/read_117.html" title="第116章 回到宜城" target="_blank" rel="nofollow">第116章 回到宜城</a><span class="time">08-11</span></li><li><a href="/141233/read_118.html" title="第117章 恶梦从未结束" target="_blank" rel="nofollow">第117章 恶梦从未结束</a><span class="time">08-11</span></li><li><a href="/141233/read_119.html" title="第118章 一百年的思念" target="_blank" rel="nofollow">第118章 一百年的思念</a><span class="time">08-11</span></li><li><a href="/141233/read_120.html" title="第119章 我们就是关系不正常" target="_blank" rel="nofollow">第119章 我们就是关系不正常</a><span class="time">08-11</span></li><li><a href="/141233/read_121.html" title="第120章 没有节制的禽兽" target="_blank" rel="nofollow">第120章 没有节制的禽兽</a><span class="time">08-11</span></li><li><a href="/141233/read_122.html" title="第121章 悠闲的日子" target="_blank" rel="nofollow">第121章 悠闲的日子</a><span class="time">08-11</span></li><li><a href="/141233/read_123.html" title="第122章 无尽黑暗" target="_blank" rel="nofollow">第122章 无尽黑暗</a><span class="time">08-11</span></li><li><a href="/141233/read_124.html" title="第123章 心魔" target="_blank" rel="nofollow">第123章 心魔</a><span class="time">08-11</span></li><li><a href="/141233/read_125.html" title="第124章 御鬼令" target="_blank" rel="nofollow">第124章 御鬼令</a><span class="time">08-11</span></li><li><a href="/141233/read_126.html" title="第125章 你要的加倍" target="_blank" rel="nofollow">第125章 你要的加倍</a><span class="time">08-11</span></li><li><a href="/141233/read_127.html" title="第126章 意外相遇" target="_blank" rel="nofollow">第126章 意外相遇</a><span class="time">08-11</span></li><li><a href="/141233/read_128.html" title="第127章 再上龙泉山" target="_blank" rel="nofollow">第127章 再上龙泉山</a><span class="time">08-11</span></li><li><a href="/141233/read_129.html" title="第128章 寻找尸骨" target="_blank" rel="nofollow">第128章 寻找尸骨</a><span class="time">08-11</span></li><li><a href="/141233/read_130.html" title="第129章 引开" target="_blank" rel="nofollow">第129章 引开</a><span class="time">08-11</span></li><li><a href="/141233/read_131.html" title="第130章 封印解开" target="_blank" rel="nofollow">第130章 封印解开</a><span class="time">08-11</span></li><li><a href="/141233/read_132.html" title="第131章 危急关头" target="_blank" rel="nofollow">第131章 危急关头</a><span class="time">08-11</span></li><li><a href="/141233/read_133.html" title="第132章 代价" target="_blank" rel="nofollow">第132章 代价</a><span class="time">08-11</span></li><li><a href="/141233/read_134.html" title="第133章 信念" target="_blank" rel="nofollow">第133章 信念</a><span class="time">08-11</span></li><li><a href="/141233/read_135.html" title="第134章 雪上加霜" target="_blank" rel="nofollow">第134章 雪上加霜</a><span class="time">08-11</span></li><li><a href="/141233/read_136.html" title="第135章 落井下石的人" target="_blank" rel="nofollow">第135章 落井下石的人</a><span class="time">08-11</span></li><li><a href="/141233/read_137.html" title="第136章 封云岚" target="_blank" rel="nofollow">第136章 封云岚</a><span class="time">08-11</span></li><li><a href="/141233/read_138.html" title="第137章 这不是结束" target="_blank" rel="nofollow">第137章 这不是结束</a><span class="time">08-11</span></li><li><a href="/141233/read_139.html" title="第138章 质问" target="_blank" rel="nofollow">第138章 质问</a><span class="time">08-11</span></li><li><a href="/141233/read_140.html" title="第139章 决心" target="_blank" rel="nofollow">第139章 决心</a><span class="time">08-11</span></li><li><a href="/141233/read_141.html" title="第140章 想要的东西" target="_blank" rel="nofollow">第140章 想要的东西</a><span class="time">08-11</span></li><li><a href="/141233/read_142.html" title="第141章 我有喜欢的人了" target="_blank" rel="nofollow">第141章 我有喜欢的人了</a><span class="time">08-11</span></li><li><a href="/141233/read_143.html" title="第142章 过去" target="_blank" rel="nofollow">第142章 过去</a><span class="time">08-11</span></li><li><a href="/141233/read_144.html" title="第143章 接受和不接受" target="_blank" rel="nofollow">第143章 接受和不接受</a><span class="time">08-11</span></li><li><a href="/141233/read_145.html" title="第144章 这是办法吗" target="_blank" rel="nofollow">第144章 这是办法吗</a><span class="time">08-11</span></li><li><a href="/141233/read_146.html" title="第145章 抽丝剥茧" target="_blank" rel="nofollow">第145章 抽丝剥茧</a><span class="time">08-11</span></li><li><a href="/141233/read_147.html" title="第146章 不是办法的办法" target="_blank" rel="nofollow">第146章 不是办法的办法</a><span class="time">08-11</span></li><li><a href="/141233/read_148.html" title="第147章 一份安慰" target="_blank" rel="nofollow">第147章 一份安慰</a><span class="time">08-11</span></li><li><a href="/141233/read_149.html" title="第148章 附灵之术" target="_blank" rel="nofollow">第148章 附灵之术</a><span class="time">08-11</span></li><li><a href="/141233/read_150.html" title="第149章 希望" target="_blank" rel="nofollow">第149章 希望</a><span class="time">08-11</span></li><li><a href="/141233/read_151.html" title="第150章 绑架" target="_blank" rel="nofollow">第150章 绑架</a><span class="time">08-11</span></li><li><a href="/141233/read_152.html" title="第151章 绝望与折磨" target="_blank" rel="nofollow">第151章 绝望与折磨</a><span class="time">08-11</span></li><li><a href="/141233/read_153.html" title="第152章 唯利是图" target="_blank" rel="nofollow">第152章 唯利是图</a><span class="time">08-11</span></li><li><a href="/141233/read_154.html" title="第153章 堕进更深的地狱" target="_blank" rel="nofollow">第153章 堕进更深的地狱</a><span class="time">08-11</span></li><li><a href="/141233/read_155.html" title="第154章 毁灭最后的尊严" target="_blank" rel="nofollow">第154章 毁灭最后的尊严</a><span class="time">08-11</span></li><li><a href="/141233/read_156.html" title="第155章 旧厂房" target="_blank" rel="nofollow">第155章 旧厂房</a><span class="time">08-11</span></li><li><a href="/141233/read_157.html" title="第156章 一步之遥" target="_blank" rel="nofollow">第156章 一步之遥</a><span class="time">08-11</span></li><li><a href="/141233/read_158.html" title="第157章 只有黑暗" target="_blank" rel="nofollow">第157章 只有黑暗</a><span class="time">08-11</span></li><li><a href="/141233/read_159.html" title="第158章 四个支派的人" target="_blank" rel="nofollow">第158章 四个支派的人</a><span class="time">08-11</span></li><li><a href="/141233/read_160.html" title="第159章 风波未平" target="_blank" rel="nofollow">第159章 风波未平</a><span class="time">08-11</span></li><li><a href="/141233/read_161.html" title="第160章 转机" target="_blank" rel="nofollow">第160章 转机</a><span class="time">08-11</span></li><li><a href="/141233/read_162.html" title="第161章 枪战" target="_blank" rel="nofollow">第161章 枪战</a><span class="time">08-11</span></li><li><a href="/141233/read_163.html" title="第162章 惊险的时刻" target="_blank" rel="nofollow">第162章 惊险的时刻</a><span class="time">08-11</span></li><li><a href="/141233/read_164.html" title="第163章 错过与结束" target="_blank" rel="nofollow">第163章 错过与结束</a><span class="time">08-11</span></li><li><a href="/141233/read_165.html" title="第164章 地狱之内" target="_blank" rel="nofollow">第164章 地狱之内</a><span class="time">08-11</span></li><li><a href="/141233/read_166.html" title="第165章 终于找到了你" target="_blank" rel="nofollow">第165章 终于找到了你</a><span class="time">08-11</span></li><li><a href="/141233/read_167.html" title="第166章 失败了吗" target="_blank" rel="nofollow">第166章 失败了吗</a><span class="time">08-11</span></li><li><a href="/141233/read_168.html" title="第167章 最深的咒语" target="_blank" rel="nofollow">第167章 最深的咒语</a><span class="time">08-11</span></li><li><a href="/141233/read_169.html" title="第168章 只为这一刻的相见" target="_blank" rel="nofollow">第168章 只为这一刻的相见</a><span class="time">08-11</span></li><li><a href="/141233/read_170.html" title="第169章 逃出生天" target="_blank" rel="nofollow">第169章 逃出生天</a><span class="time">08-11</span></li><li><a href="/141233/read_171.html" title="第170章 你的命是我的" target="_blank" rel="nofollow">第170章 你的命是我的</a><span class="time">08-11</span></li><li><a href="/141233/read_172.html" title="第171章 一场交易" target="_blank" rel="nofollow">第171章 一场交易</a><span class="time">08-11</span></li><li><a href="/141233/read_173.html" title="第172章 该做的事" target="_blank" rel="nofollow">第172章 该做的事</a><span class="time">08-11</span></li><li><a href="/141233/read_174.html" title="第173章 最后的歇斯底里" target="_blank" rel="nofollow">第173章 最后的歇斯底里</a><span class="time">08-11</span></li><li><a href="/141233/read_175.html" title="第174章 下场" target="_blank" rel="nofollow">第174章 下场</a><span class="time">08-11</span></li><li><a href="/141233/read_176.html" title="第175章 这就是死亡" target="_blank" rel="nofollow">第175章 这就是死亡</a><span class="time">08-11</span></li><li><a href="/141233/read_177.html" title="第176章 结束和开始" target="_blank" rel="nofollow">第176章 结束和开始</a><span class="time">08-11</span></li><li><a href="/141233/read_178.html" title="第177章 再次出现的人" target="_blank" rel="nofollow">第177章 再次出现的人</a><span class="time">08-11</span></li><li><a href="/141233/read_179.html" title="第178章 诡异的女孩" target="_blank" rel="nofollow">第178章 诡异的女孩</a><span class="time">08-11</span></li><li><a href="/141233/read_180.html" title="第179章 鬼遮人" target="_blank" rel="nofollow">第179章 鬼遮人</a><span class="time">08-11</span></li><li><a href="/141233/read_181.html" title="第180章 寻找线索" target="_blank" rel="nofollow">第180章 寻找线索</a><span class="time">08-11</span></li><li><a href="/141233/read_182.html" title="第181章 二名受害者" target="_blank" rel="nofollow">第181章 二名受害者</a><span class="time">08-11</span></li><li><a href="/141233/read_183.html" title="第182章 最可怕的对手" target="_blank" rel="nofollow">第182章 最可怕的对手</a><span class="time">08-11</span></li><li><a href="/141233/read_184.html" title="第183章 是人是鬼" target="_blank" rel="nofollow">第183章 是人是鬼</a><span class="time">08-11</span></li><li><a href="/141233/read_185.html" title="第184章 一物降一物" target="_blank" rel="nofollow">第184章 一物降一物</a><span class="time">08-11</span></li>
	'''			
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
    	#links = response.xpath(response.meta['linkpath'])
    	links1 = response.xpath('//ul[@id="toplist"]/li/a');
    	links2 = Selector(text=self.temp).xpath('//li/a');
    	links3 = response.xpath('//ul[@id="lastchapter"]/li/a');
    	links = links1+links2+links3

    	j = 1
    	maxcid = 1
    	for link in links:
		    name = link.xpath('text()').extract_first()
		    if name in names:
		    	continue
		    href = link.xpath('@href').extract_first()
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
		    	meta['prev_cid'] = 	maxcid-1
		    meta['next_cid'] = maxcid+1
            
		    maxcid = maxcid+1
		    meta['sequence'] = j
		    j = j+1
		    self.logger.info('Parse url is  %s', next_url)
		    chapter_id = mysql.insert(meta)
		    meta['contentxpath'] = response.meta['contentxpath']
		    meta['id'] = chapter_id
		    self.logger.info('Parse function called on dfsdfsd------------------')
		    yield scrapy.Request(next_url,callback=self.parse_content,meta=meta)
    	mysql.close()
    	
	    

	   
    def parse_content(self,response):
        meta = response.meta

        self.logger.info('parse_content parse_content parse_content on parse_content------------------%s',response.url)
        str = response.xpath(meta['contentxpath']).extract()
        str = filter(lambda s:s != '',str)
        newsttr = list(str)
        content = '\r\n'.join(newsttr)
        meta['content'] = content
        yield meta