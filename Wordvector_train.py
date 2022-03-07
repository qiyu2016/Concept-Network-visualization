#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: Qiyu
@date : 2020/5/1 14:40

解决warning问题
UserWarning: detected Windows; aliasing chunkize to chunkize_serial
warnings.warn("detected Windows; aliasing chunkize to chunkize_serial")
"""

import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

#import gensim
#from gensim.models.keyedvectors import KeyedVectors
from gensim.models import word2vec
import logging
#import nltk
#import re
#import string
#from nltk.stem import WordNetLemmatizer

import time
start = time.clock()

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.LineSentence('D:/5_PatentData/Data/Training_corpus/01wordvecCorpus.txt')   # 加载语料
model = word2vec.Word2Vec(sentences, size=100, window=10, min_count=1, sg=1, hs=0)

model.save('./WordVector.model')


# 获取程序运行时间
end = time.clock()
seconds = end-start
#seconds = 323278.464909
#seconds = 0.6
print('Running time: %s Seconds' %seconds)
# 将运行时间秒转换为时分秒
if seconds >=1:
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    print('Running time(hours:mins:seconds): %02d:%02d:%02d' %(h, m, s))
