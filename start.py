'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/6/27 19:59
@Software: PyCharm
@File    : start.py
'''
from scrapy import cmdline

# cmdline.execute("scrapy crawl httpbin".split())
cmdline.execute("scrapy crawl ipproxy".split())