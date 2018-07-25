#! /usr/bin/env python
# -*- coding: utf-8 -*-
import random
import re


def get_url(base_url, page_num):
    return base_url.replace("${page_num}", str(page_num))


def get_random_second(start, end):
    return random.randint(start, end)


def get_one_item(context):
    pattern = re.compile(r'tbinfo(.*?)feed_list_repeat', re.S)
    return pattern.findall(context)






def filter_tags(htmlstr):
   re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I)
   re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)
   re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)
   re_p = re.compile('<P\s*?/?>')
   re_h = re.compile('</?\w+[^>]*>')
   re_comment = re.compile('<!--[^>]*-->')
   s = re_cdata.sub('',htmlstr)
   s = re_script.sub('',s)
   s = re_style.sub('',s)
   s = re_p.sub('\r\n',s)
   s = re_h.sub('',s)
   s = re_comment.sub('',s)
   blank_line = re.compile('\n+')
   s = blank_line.sub('\n',s)
   return s