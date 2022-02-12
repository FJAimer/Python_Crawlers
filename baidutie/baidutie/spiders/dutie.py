import scrapy
from baidutie.items import BaidutieItem

class DutieSpider(scrapy.Spider):
    name = 'dutie'
    # 2、检查修改允许的域
    allowed_domains = ['baidu.com']
    # 1、修改起始url
    start_urls = ['https://tieba.baidu.com/f?kw=%E6%96%B9%E8%88%9F%E7%94%9F%E5%AD%98%E8%BF%9B%E5%8C%96']

    def parse(self, response):
        # 3、编写解析方法
        # 获取所有节点
        node_list = response.xpath('//*[@id="thread_list"]/li')
        # 遍历节点列表，提取数据name、link
        for node in node_list:
            # item = {}
            # 实例化
            item = BaidutieItem()

            item['name'] = node.xpath('./div/div[2]/div[1]/div[1]/a/text()').extract_first()
            item['link'] = response.urljoin(node.xpath('./div/div[2]/div[1]/div[1]/a/@href').extract_first())
            yield item
        # 模拟翻页
        # 获取下一页url
        part_url = response.xpath('//*[@id="frs_list_pager"]/a[@class="next pagination-item "]/@href | //*[@id="frs_list_pager"]/a[@class="next pagination-item"]/@href').extract_first()
        print(part_url)
        # 判断终止条件
        if part_url != None:
            next_url = response.urljoin(part_url)
            # 构建请求对象，并返回yield给引擎
            yield scrapy.Request(
                url=next_url,
                callback=self.parse
            )