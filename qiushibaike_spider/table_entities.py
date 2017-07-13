# coding: utf-8

"""
数据库连接, 数据表定义和创建

"""

# 加载pony orm
from pony.orm import *
# 加载预定义的mysql配置
from .settings import MYSQL_CONFIG

# 定义pony db实例
db = Database()
# 连接数据库
db.bind('mysql', **MYSQL_CONFIG)


class Article(db.Entity):
    """糗事百科文章table对象"""
    _table_ = 't_qiushibaike_article'
    article_id = PrimaryKey(int)
    user_id = Optional(int, index=True)
    user_name = Optional(str, 30, index=True)
    user_gender = Optional(str, 1)
    user_age = Optional(int, size=8)
    user_img = Optional(str, 200)
    vote_count = Optional(int)
    comment_count = Optional(int)
    god_comment = Optional(str, 420)
    article_type = Required(str, 4)
    content = Optional(str, 780)
    image = Optional(str, 120)
    url = Required(str, 60)

    def __str__(self):
        if len(self.content) > 50:
            content = self.content[0:50] + '...'
        else:
            content = self.content
        return 'ID: {} Content: {}'.format(self.article_id, content)


# 创建table
db.generate_mapping(create_tables=True)
