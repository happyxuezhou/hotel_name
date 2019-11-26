#!/usr/bin/python
# -*- coding:utf-8 -*-

from gensim.models import word2vec,KeyedVectors
wv_from_text = KeyedVectors.load_word2vec_format('Tencent_AILab_ChineseEmbedding.txt',binary = False)


def get_hotel_name(names):
    with open('./hotel_name.txt','w+') as file:
        for name in names:
            for key in wv_from_text.wv.similar_by_word(name, topn = 100):
                print(key[0], key[1])
                file.write(key[0]+'\n')


names = ['华住酒店','携程','同程','七天酒店','汉庭酒店','莫泰酒店','途牛','去哪儿','飞猪','驴妈妈','艺龙','马蜂窝','驴妈妈','格林豪泰','假日酒店','万豪酒店','四季酒店',
	'如家酒店','经济酒店','连锁酒店']

get_hotel_name(names)
