#! /usr/bin/env python
# -*- coding: utf-8 -*-


def get_url(base_url, page_num):
    return base_url.replace("${page_num}", str(page_num))