# -*- coding: utf-8 -*-

"""
糗事百科段子命令行输出管道

"""

from w3lib.html import replace_tags


class ArticleConsolePipeline:
    def process_item(self, item, spider):
        """处理item"""
        user_name = item.get('user_name', '')
        user_gender = item.get('user_gender', '')
        user_age = item.get('user_age', 0)
        vote_count = item.get('vote_count', 0)
        comment_count = item.get('comment_count', 0)
        god_comment = item.get('god_comment', '')
        content = item.get('content', '')
        url = item.get('url', '')

        # 更改性别显示方式
        user_gender = '男' if user_gender == 'M' else '女'
        # 去除html标签
        content = replace_tags(content, token='\n').strip()

        print('#' * 30)
        if user_name != '匿名用户':
            print('{} {} {}:'.format(user_name, user_gender, user_age))
        else:
            print('匿名用户:')
        print('正文: {}'.format(content))
        if god_comment != '':
            print('神评: {}'.format(god_comment))
        print('#' * 30 + '\n')
