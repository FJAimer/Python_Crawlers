#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
import re
import random
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 隐式等待

# 防止被识别， 设置随机等待秒数
rand_seconds = random.choice([1, 3]) + random.random()

listname = []


def spider(url, xpath_name):
    driver.get(url=url)

    # 循环几次  滚动几次
    for i in range(1, 8):
        # 爬取电影名称
        name = driver.find_elements(By.XPATH, xpath_name)

        for j in range(len(name)):
            # 判断当前下标name有没有文本
            if name[j].text:
                # 有则添加进列表
                listname.append(name[j].text)
            else:
                pass
        # 下拉滚动
        driver.execute_script('window.scrollTo(0,{})'.format(i * 400))

    # 完成后关闭浏览器
    driver.close()

    print(listname)
    print(len(listname))


# 调用函数
# 并传参url和xpath
spider(url='https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90',
       xpath_name='//*[@id="content"]/div/div[1]/div/div/div/div/div//a')