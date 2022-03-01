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
    def __init__(self, iurl):
        # 需要爬取 页面动态 的url
        # self.url = "https://space.bilibili.com/672353429/dynamic?spm_id_from=333.999.0.0"
        self.url = iurl
        # 实例化一个配置对象
        self.driver = webdriver.Chrome()

    def parse(self):
        # 发送请求，获取响应
        self.driver.get(self.url)
        lists_con = []
        # 循环滚动 循环几次 滚动几次
        for i in range(1, 10):
            time.sleep(2)
            # 找到所有的 动态
            # com_lists = self.driver.find_elements(By.XPATH, '//*[@id="page-dynamic"]/div[1]/div/div/div')
            com_lists = self.driver.find_elements(By.XPATH, '//*[@id="page-dynamic"]/div[1]/div/div/div/div/div[1]/div[3]/div[1]/div/div/div/div')
            name = self.driver.find_element(By.XPATH, '//*[@id="h-name"]')
            for j in range(len(com_lists)):
                # 判断当前下标com_lists有没有文本
                if com_lists[j].text:
                    # 有则添加进列表
                    lists_con.append(com_lists[j].text)
                    # 写入文件
                    with open(f'lists_con_{name.text}.txt', 'w+', encoding='utf-8') as f:
                        for ls in lists_con:
                            # print(type(ls))
                            print(ls)
                            f.write(name.text + '：' + ls + '\n' + '\n')
                            f.write('*----------------------------分割线----------------------------*\n')
                else:
                    pass
            # 编写页面滚动的js语句
            # js = 'window.scrollTo(0,(i * 400))'
            # js = 'window.scrollTo(0,document.body.scrollHeight)'
            # 执行js方法
            # self.driver.execute_script(js)
            self.driver.execute_script('window.scrollTo(0,{})'.format(i * 2000))

        # 完成后关闭浏览器
        self.driver.close()


        # print(type(lists_con))
        # print(len(lists_con))
        # print(lists_con)

    def run(self):
        self.parse()


if __name__ == '__main__':
    # url = "https://space.bilibili.com/672353429/dynamic"
    url = input('请输入B站的动态网址：')
    bilicom = Bili_com(url)
    bilicom.run()
