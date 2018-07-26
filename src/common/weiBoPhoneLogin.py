#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests

class WeiBoPhoneLogin(object):

    def login(self):
        login_url = "https://passport.weibo.cn/sso/login"
        headers={
            "Content-Type":"application/x-www-form-urlencoded",
            "Origin": "https://passport.weibo.cn",
            "Referer": "https://passport.weibo.cn/signin/login",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }
        data = {
            "username": "1666188122@qq.com",
            "password": "mzg...8535933570",
            "savestate": 1,
            "r": "",
            "ec": 0,
            "pagerefer": "",
            "entry": "mweibo",
            "wentry": "",
            "loginfrom": "",
            "client_id": "",
            "code": "",
            "qq": "",
            "mainpageflag": 1,
            "hff": "",
            "hfp": ""
        }
        res = requests.post(login_url, data, headers=headers)
        print(res.text)
        return res.cookies

if __name__ == "__main__":
    weibop = WeiBoPhoneLogin()
    cookies = weibop.login()

