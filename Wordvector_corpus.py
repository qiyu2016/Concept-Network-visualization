#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: Qiyu
@date : 2020/5/1 14:10
"""

import linecache

TotalNum = 1448   # 设置文本文件总数
count = 1
file_wordvecCorpus = open('D:/5_PatentData/Data/Training_corpus/01wordvecCorpus.txt', 'a', encoding='utf8')

while True:
    linepath = "D:/5_PatentData/Data/Training_corpus/" + str(count) + ".txt"
    linecontent = linecache.getline(linepath, 1)
    if "论文页>" not in linecontent:
        for line in open(linepath, encoding='utf8'):
            file_wordvecCorpus.write(line)

    linecache.clearcache()  # 清除现有的文件缓存
    count = count + 1
    if count > TotalNum:
        break

file_wordvecCorpus.close()





