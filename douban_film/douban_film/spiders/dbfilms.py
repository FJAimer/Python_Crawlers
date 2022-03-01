import scrapy
from douban_film.items import DoubanFilmItem   # 导入建模模型


class DbfilmsSpider(scrapy.Spider):
    name = 'dbfilms'
    # 2、检查域名
    allowed_domains = ['douban.com']
    # 1、修改起始url
    start_urls = ['https://movie.douban.com/top250']

    # 实现爬取逻辑
    def parse(self, response):
        # 获取所有电影分类列表
        node_lists = response.xpath('//*[@id="content"]/div/div[1]/ol/li/div')
        # print(len(node_lists))  # 每页25
        # 遍历列表拿到需要的数据
        for node in node_lists:
            # 模型实例化
            item = DoubanFilmItem()

            # 添加模型数据
            item['name'] = node.xpath('./div[2]/div[1]/a/span[1]/text()').extract_first()
            item['link'] = node.xpath('./div[2]/div[1]/a/@href').extract_first()
            item['counts'] = node.xpath('./div[2]/div[2]/div/span[4]/text()').extract_first()
            item['description'] = node.xpath('./div[2]/div[2]/p[2]/span/text()').extract_first()

            yield item

        # 翻页操作
        next_url = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract_first()
        # 判断终止条件,如果next_url不等于None，则执行翻页操作
        if next_url != None:
            # 使用urljoin()自动补全连接
            next_url = response.urljoin(next_url)
            yield scrapy.Request(url=next_url)