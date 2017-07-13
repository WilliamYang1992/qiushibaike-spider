# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    # 文章ID
    article_id = scrapy.Field()
    # 用户ID
    user_id = scrapy.Field()
    # 用户名
    user_name = scrapy.Field()
    # 用户性别
    user_gender = scrapy.Field()
    # 用户年龄
    user_age = scrapy.Field()
    # 用户头像
    user_img = scrapy.Field()
    # 好笑数
    vote_count = scrapy.Field()
    # 评论数
    comment_count = scrapy.Field()
    # 神评
    god_comment = scrapy.Field()
    # 文章类型
    article_type = scrapy.Field()
    # 文章文字内容
    content = scrapy.Field()
    # 文章图片内容
    image = scrapy.Field()
    # 文章url
    url = scrapy.Field()
