# -*- encoding:utf8 -*-
from scrapy import Spider        # 导入spider基类
from scrapy.selector import Selector             # 导入选择器
from spider_learn.items import SpiderLearnItem   # 导入item

# 创建一个自定义的spider,继承scrapy里面的spider基类
class tbspider(Spider):
    name = "tbspider"       # 爬虫的名称
    start_urls = [          # 开始爬取的url
        #"http://book.douban.com/top250"
        #"https://www.douban.com/"
        "https://item.jd.com/3372867.html"
    ]

    def parse(self, response):   # 解析html的方法
        print(response.body)
        item = SpiderLearnItem()
        #print(response.body)
        print("start")
        sel = Selector(response)
        #book_names = sel.css("#parameter2>li").xpath("./@title").extract()
        #book_names = sel.xpath(".//*[@id='J_Itemlist_TLink_35226125815']/text()").extract()
        book_names= sel.xpath(".//*[@id='jd-price']/text()").extract()
        print("-----------------")
        print(book_names)
        print("-----------------")
        """
        item_name = scrapy.Field()
        item_id = scrapy.Field()
        item_weight = scrapy.Field()
        item_area = scrapy.Field()
        """
        item['item_name'] = book_names[0]
        item['item_id'] = book_names[1]
        item['item_weight'] = book_names[2]
        item['item_area'] = book_names[3]
        yield item                              # 返回item接着会传输到pipeline进行后续的存储操作
