# coding: utf-8

"""
Item Processor
处理ItemLoader输入和输出的数据

"""

import re


def strip(value):
    """移除字符串的空白"""
    if isinstance(value, str):
        return value.strip()
    else:
        return value


class ArticleIdInputProcessor:
    """提取文章ID"""

    def __call__(self, values):
        if values:
            value = values[0]
            match = re.findall('/article/(\d+)', value)
            if match:
                article_id = match[0]
                return article_id


class UserIdInputProcessor:
    """提取用户ID"""

    def __call__(self, values):
        if values:
            value = values[0]
            match = re.findall('/(\d+)/', value)
            if match:
                user_id = match[0]
                return user_id


class UserGenderInputProcessor:
    """根据class名称, 判断用户性别"""

    def __call__(self, values):
        if values:
            value = values[0]
            if 'man' in value:
                return 'M'
            elif 'women' in value:
                return 'F'


class ArticleTypeInputProcessor:
    """根据内容, 判断为纯文字还是文字图片混合"""

    def __call__(self, values):
        if values:
            value = values[0]
            if 'class="thumb"' in value and 'class="content"' in value:
                return 'mix'
            else:
                return 'text'
