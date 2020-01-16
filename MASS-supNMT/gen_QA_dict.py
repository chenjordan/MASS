# This file is used to translate dictionary from zh to hant

import os
import sys
sys.path.append('../lang-conv')

import random
import subprocess
from langconv import *

dst_root = './QA_test_data/'

src_dict = './data/mono/dict.zh.txt'
dst_dict = os.path.join(dst_root, 'dict.zh.txt')


def lang_conv(word):
    # convert language from zh to hant
    tmp = Converter('zh-hant').convert(word)
    return tmp


# convert dict
def convert_dict():
    with open(src_dict) as f:
        src_data = f.readlines()
    
    with open(dst_dict, 'w') as f:
        for i in src_data:
            print('-----------------')
            tmp = i.split('\n')
            word, idx = tmp[0].split(' ')
            print(tmp)
    
            trans_word = lang_conv(word)
            print(trans_word)
            dump_word = trans_word + ' ' + idx + '\n'
            f.writelines(dump_word)

