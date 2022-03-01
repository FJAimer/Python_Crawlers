#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 利用selenium爬取bilibili动态发布消息
# 实现思路，利用selenium控制浏览器执行我们规定的js代码
# 执行js的方法：driver.execute_script(js)
# 导包
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Bili_com(object):
    def __init__(self):
        # 需要爬取 页面动态 的url
        self.url = "https://space.bilibili.com/672353429/dynamic?spm_id_from=333.999.0.0"

        # 实例化一个配置对象
        self.driver = webdriver.Chrome()

    def parse(self):
        # 发送请求，获取响应
        self.driver.get(self.url)
        lists_con = []
        # 循环滚动 循环几次 滚动几次
        for i in range(1, 5):
            time.sleep(2)
            # 找到所有的 动态
            # com_lists = self.driver.find_elements(By.XPATH, '//*[@id="page-dynamic"]/div[1]/div/div/div')
            com_lists = self.driver.find_elements(By.XPATH, '//*[@id="page-dynamic"]/div[1]/div/div/div/div/div[1]/div[3]/div[1]/div/div/div/div')
            # for com in com_lists:
            #     print(com)
            #     lists_con.append(com)
            print(com_lists)
            # 编写页面滚动的js语句
            js = 'window.scrollTo(0,(i * 400))'
            # js = 'window.scrollTo(0,document.body.scrollHeight)'
            # 执行js方法
            self.driver.execute_script(js)

        # 完成后关闭浏览器
        self.driver.close()
        # print(lists_con)
        # print(len(lists_con))

    def run(self):
        self.parse()


if __name__ == '__main__':
    bilicom = Bili_com()
    bilicom.run()
