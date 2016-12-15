# -*- coding: utf-8 -*-
import scrapy


class TbtestSpider(scrapy.Spider):
    name = "tbtest"
    allowed_domains = ["taobao.com"]
    start_urls = (
        'http://www.taobao.com/',
    )

    def parse(self, response):
        pass
