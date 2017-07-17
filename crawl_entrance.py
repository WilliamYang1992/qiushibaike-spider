# -*- coding: utf-8 -*-

"""
Scrapy 运行入口
参数为要运行的Spider的name

"""

import os
import sys
import time
import datetime

from qiushibaike_spider.settings import CRAWL_INTERVAL, CRAWL_CYCLES

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        # 获取spider_name
        spider_name = sys.argv[1]
    else:
        spider_name = 'article'
    count = 0  # 记录爬取次数
    while True:
        try:
            os.system('scrapy crawl {}'.format(spider_name))
        except KeyboardInterrupt:
            print('用户已停止')
            sys.exit()
        else:
            count += 1  # 爬取次数增加
            if CRAWL_CYCLES != 0 and count == CRAWL_CYCLES:
                print('{}  爬取指定次数({}次)已完成'.format(datetime.datetime.now(), CRAWL_CYCLES))
                sys.exit()
            print('{}  已完成第{}次爬取, 正在等待下一次爬取'.format(datetime.datetime.now(), count))
            time.sleep(CRAWL_INTERVAL)
