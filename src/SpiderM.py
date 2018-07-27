#! /usr/bin/env python
# -*- coding: utf-8 -*-
from src.common.weiBoPhoneLogin import WeiBoPhoneLogin
from src.config import Config
from src.common import utils
import requests
from bs4 import BeautifulSoup


class SpiderM(object):
    #     classs to catch weibo news

    def __init__(self):
        """
        get login cookies
        """

        user_name = Config.getUserName()
        pass_word = Config.getPwd()
        weibo = WeiBoPhoneLogin()
        cookies = weibo.login(user_name,pass_word)
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
    base_url = Config.getUrl(1)
    spider = SpiderM()
    url2 = spider.get_page_url(base_url, 2)
    headers = Config.get_header()
    print("url  -->  ", url2)
    res2 = spider.get_page_content(url2, None, headers)
    print("********************")
    soup = BeautifulSoup(res2, "lxml")
    newsList = soup.find_all(id=True, class_='c')
    item = newsList[1]
    div_one = item.find_all('div')
    contentHtml = div_one[0]
    numHtml = div_one[1]
    print(contentHtml)
    print(numHtml)





