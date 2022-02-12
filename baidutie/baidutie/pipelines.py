# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class BaidutiePipeline:
    def __init__(self):
        self.file = open('baidutie.json', 'w')
    # 默认调用process_item方法，该方法定义如何处理数据
    def process_item(self, item, spider):
        # 将item对象强转为字典
        item = dict(item)
        # 将字典数据序列化
        json.data = json.dumps(item, ensure_ascii=False) + ', \n'
        # 将数据写入文件
        self.file.write(json.data)
        return item

    def __del__(self):
        self.file.close()
