import scrapy


class DbfilmsSpider(scrapy.Spider):
    name = 'dbfilms'
    # 2、检查域名
    allowed_domains = ['douban.com']
    # 1、修改起始url
    start_urls = ['https://movie.douban.com/top250']

    # 实现爬取逻辑
    def parse(self, response):
        pass
