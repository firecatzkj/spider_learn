# -*- coding: utf-8 -*-

# Scrapy settings for spider_learn project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spider_learn'

SPIDER_MODULES = ['spider_learn.spiders']
NEWSPIDER_MODULE = 'spider_learn.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spider_learn (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#     'scrapy.spidermiddlewares.offsite.OffsiteMiddleware':None,
#     'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware':None,
# 'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware':None,
#  'scrapy.spidermiddlewares.referer.RefererMiddleware':None,
#  'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware':None,
#  'scrapy.spidermiddlewares.depth.DepthMiddleware':None
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
JS_DOWNLOADER=['tbspider']

DOWNLOADER_MIDDLEWARES = {
    'spider_learn.dealjs.Jsmiddleware':543,
    #'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
    # 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware':None,
    # 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware':None
    #'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware':None,
    #'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware':None,
    #'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
    #'scrapy.downloadermiddlewares.retry.RetryMiddleware':None,
    #"scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware":None,
     #'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware':None,
     #'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware':None,
     #'scrapy.downloadermiddlewares.redirect.RedirectMiddleware':None,
     #'scrapy.downloadermiddlewares.cookies.CookiesMiddleware':None,
     #'scrapy.downloadermiddlewares.chunked.ChunkedTransferMiddleware':None,
     #'scrapy.downloadermiddlewares.stats.DownloaderStats':None
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'spider_learn.pipelines.SpiderLearnPipeline': 300,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
