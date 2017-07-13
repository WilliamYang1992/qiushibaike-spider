# -*- coding: utf-8 -*-

"""
糗事百科爬虫
根据PC网页端的热门栏目爬取段子
以供后续数据分析

"""

__author__ = 'William Yang <505741310@qq.com>'

import time

import scrapy
from scrapy import Request

from ..items import ArticleItem
from ..item_loaders import ArticleLoader


class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['qiushibaike.com']
    start_url = 'https://qiushibaike.com/'

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

    def start_requests(self):
        yield Request(url=self.start_url, headers=self.headers, dont_filter=True, meta={'page': 1})

    def parse(self, response):
        # 文章块xpath
        article_block_xpath = '//div[@class="article block untagged mb15"]'
        article_blocks = response.xpath(article_block_xpath)
        if article_blocks:
            # 预定义各种field的相对xpath, 前面增加了'.'代表了相对路径
            article_id_xpath = './/a[@class="contentHerf"]/@href'
            user_id_xpath = './/a[@rel]/@href'
            user_name_xpath = './/h2/text()'
            user_gender_css = '.articleGender::attr(class)'
            user_age_css = '.articleGender::text'
            user_img_xpath = './/a[@rel]/img/@src'
            vote_count_xpath = './/span[@class="stats-vote"]/i/text()'
            comment_count_xpath = './/span[@class="stats-comments"]//i/text()'
            god_comment_xpath = './/div[@class="main-text"]/text()'
            content_xpath = './/div[@class="content"]/span'
            image_xpath = './/div[@class="thumb"]//img/@src'
            # 循环遍历各个文章块, 从而导出item
            for block in article_blocks:
                # 实例ArticleLoader, 这里一定要用'selector=block', 因为是相对于block选择
                l = ArticleLoader(item=ArticleItem(), selector=block)
                l.add_xpath('article_id', article_id_xpath)
                l.add_xpath('user_id', user_id_xpath)
                l.add_xpath('user_name', user_name_xpath)
                l.add_css('user_gender', user_gender_css)
                l.add_css('user_age', user_age_css)
                l.add_xpath('user_img', user_img_xpath)
                l.add_xpath('vote_count', vote_count_xpath)
                l.add_xpath('comment_count', comment_count_xpath)
                l.add_xpath('god_comment', god_comment_xpath)
                l.add_xpath('content', content_xpath)
                l.add_xpath('image', image_xpath)
                l.add_value('article_type', block.extract())  # 传入整个文章区域来判断文章类型
                l.add_value('url', 'https://www.qiushibaike.com/article/{}'.format(l.get_output_value('article_id')))
                yield l.load_item()

        # 获得页数
        page = response.meta.get('page', 1)
        # 因为糗事百科默认最多只能看35页的内容, 因此只需要循环遍历到35页即可
        if page < 35:
            page += 1
            url = 'https://www.qiushibaike.com/8hr/page/{}'.format(page)
            yield Request(url=url, headers=self.headers, dont_filter=True, meta={'page': page})
