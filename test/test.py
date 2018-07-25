#! /usr/bin/env python
# -*- coding: utf-8 -*-
from src.common import utils

if __name__ == "__main__":
    print("start")
    # temp_file = open("./temp.txt", encoding='utf-8', errors="ignore")
    temp_file = open("../material/temp.html", encoding='utf-8', errors="ignore")
    file_context = ""
    try:
        file_context = temp_file.read()
        print("a")
    finally:
        temp_file.close()
    # print(file_context)
    print("aaa")
    item = utils.get_one_item(file_context)
    print("a2")
    print(len(item))
    print(item[0])
    print(item)