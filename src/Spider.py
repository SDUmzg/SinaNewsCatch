#! /usr/bin/env python
# -*- coding: utf-8 -*-
from src.common.weiboLogin import WeiBoLogin
from src.config import Config
from src.common import utils
import requests
import time

class Spider(object):
    #     classs to catch weibo news

    def __init__(self):
        """
        get login cookies
        """

        user_name = Config.getUserName()
        pass_word = Config.getPwd()
        weibo = WeiBoLogin()
        cookies = weibo.login(user_name, pass_word)
        self.cookies = cookies

    @staticmethod
    def get_page_url(base_url, page_num):
        return utils.get_url(base_url, page_num)

    def get_page_content(self, url, data, headers):
        response = requests.request('GET', url, data=data, headers=headers, cookies=self.cookies)
        self.cookies.update(response.cookies)
        return response.text


if __name__ == "__main__":
    print("Test Start")
    # user_name = Config.getUserName()
    # pass_word = Config.getPwd()
    base_url = Config.getUrl(0)
    spider = Spider()
    url1 = spider.get_page_url(base_url, 1)
    url2 = spider.get_page_url(base_url, 2)
    headers = Config.get_header()
    time.sleep(utils.get_random_second(1, 3))
    print("url  -->  ", url1)
    res1 = spider.get_page_content(url1, None, headers)
    time.sleep(utils.get_random_second(1, 3))
    print("url  -->  ", url2)
    res2 = spider.get_page_content(url2, None, headers)
    print(res1)
    print("********************")
    print(res2)

