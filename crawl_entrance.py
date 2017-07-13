# -*- coding: utf-8 -*-

"""
Scrapy 运行入口
参数为要运行的Spider的name

"""

import os
import sys
import time

from qiushibaike_spider.settings import CRAWL_INTERVAL

if __name__ == '__main__':
    spider_name = sys.argv[1]
    while True:
        try:
            os.system('scrapy crawl {}'.format(spider_name))
            print()
            time.sleep(CRAWL_INTERVAL)
        except KeyboardInterrupt:
            print('用户已停止')
            sys.exit()
