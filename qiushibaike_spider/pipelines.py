# -*- coding: utf-8 -*-

"""
糗事百科段子输出管道
基于Pony ORM框架, Pony支持MySQL, postgresql, Oracle 和 SQLite
本项目采用MySQL保存数据
如果数据库已存在相同段子, 则更新相关数据

"""

from .table_entities import db, db_session, DatabaseError, Article


class ArticlePipeline:
    def __init__(self):
        self.db = db
        self.Article = Article
        self.items = []

    def close_spider(self, spider):
        if self.items:
            self.process_items(self.items)
        self.db.commit()

    def process_item(self, item, spider):
        """收集item"""
        self.items.append(item)
        # 达到一定量时一并输出, 减少数据库事务的发生
        if len(self.items) >= 10:
            result = self.process_items(self.items)
            if result:
                self.items.clear()
        return item

    @db_session
    def process_items(self, items):
        """输出已收集的item到数据库"""
        result = True
        for item in items:
            article_id = item['article_id']
            try:
                article = self.Article.get(article_id=article_id)
                if article is None:
                    article = self.Article(**item)  # 完成插入一个段子到数据库
                    print('成功插入{}'.format(article))
                else:
                    print('已存在{}'.format(article))
                    article.vote_count = item.get('vote_count', 0)
                    article.comment_count = item.get('comment_count', 0)
                    article.god_comment = item.get('god_comment', '')
                    article.content = item.get('content', '')
                    article.image = item.get('image', '')
            except DatabaseError as e:
                print(e)
                print('数据库发生错误, 插入或更新数据失败: {}: {}'.format(item['article_id'], item['content'][0:50]))
                result = False
        return result
