# coding: utf-8

"""
定义文章ItemLoader

"""

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst

from .item_processors import strip, ArticleIdInputProcessor, UserIdInputProcessor, UserGenderInputProcessor, \
    ArticleTypeInputProcessor


class ArticleLoader(ItemLoader):
    default_input_processor = MapCompose(strip)
    default_output_processor = TakeFirst()

    article_id_in = ArticleIdInputProcessor()
    user_id_in = UserIdInputProcessor()
    user_gender_in = UserGenderInputProcessor()
    god_comment_in = MapCompose(lambda x: x[2:-1])  # 去除神评前面的冒号和最后面的换行符
    user_img_in = MapCompose(lambda x: 'https:' + x)  # 补充协议头
    picture_in = MapCompose(lambda x: 'https:' + x)  # 补充协议头
    article_type_in = ArticleTypeInputProcessor()  # 根据内容判断文章类型
