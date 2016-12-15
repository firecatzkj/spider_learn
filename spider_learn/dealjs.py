# -*- encoding:utf8 -*-
import datetime
from selenium import webdriver
import time
from scrapy.http.response.html import HtmlResponse
from scrapy.spidermiddlewares.offsite import OffsiteMiddleware
from spider_learn.settings import JS_DOWNLOADER





"""
针对某些网页必须用浏览器渲染js才能得到完整的页面(比如京东商品的价格)
在这里开始download middleware,使用phantomjs,来获取渲染之后的html页面
"""
class Jsmiddleware(object):
    def process_request(self, request, spider):
        if spider.name == 'tbspider':
            print("正在使用js引擎爬取页面: PhantomJS is starting...")
            driver = webdriver.PhantomJS(executable_path="D:\\phantomjs-1.9.7-windows\\phantomjs.exe")  # 指定使用的浏览器
            try:
                driver.get(request.url)
                #driver.get(request.url)
                time.sleep(5)
                body = driver.page_source
                print(body)
                print("访问了:" + request.url)
                ###########################################################################
                ###########################################################################
                resp = HtmlResponse(driver.current_url, body=body,encoding="utf8")
                return resp
                ###########################################################################
                ###########################################################################
            except Exception as e:
                print("连接错误或者超时:{}".format(e[0]))
                return None
            finally:
                driver.quit()
        else:
            return None



# if __name__ == '__main__':
#     test = Jsmiddleware()
#     test.start_request("https://item.jd.com/3372867.html",1)