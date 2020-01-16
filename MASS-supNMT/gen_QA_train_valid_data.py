# This file is used to preprocess data for generate train and valid data
# train.en train.zh valid.en valid.zh
import os
import csv
import sys
sys.path.append('../lang-conv')

import random
import subprocess
from langconv import *

dst_root = './QA_test_data/'

src_dict = './data/mono/dict.zh.txt'
dst_dict = os.path.join(dst_root, 'dict.zh.txt')
src_csv = '../../sample_v2_10_test.csv'

train_Q = os.path.join(dst_root, 'train.Q')
train_A = os.path.join(dst_root, 'train.A')
val_Q = os.path.join(dst_root, 'valid.Q')
val_A = os.path.join(dst_root, 'valid.A')
total_QA = os.path.join(dst_root, 'total_test_QA.txt')


def lang_conv(word):
    tmp = Converter('zh-hant').convert(word)
    return tmp


"""
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
"""

# convert csv
QA_pair = []

with open(src_csv, 'r') as f3:
    rows = csv.reader(f3)
    
    for row in rows:
        Q = lang_conv(row[0])
        A = lang_conv(row[1])
        QA_pair.append((Q.replace('\xa0', ''), A.replace('\xa0', '')))



# split train and valid set
random.shuffle(QA_pair)
train_idx = int(len(QA_pair) * 0.9)


# dump train data
with open(total_QA, 'w') as f:
    with open(train_Q, 'w') as f1:
        with open(train_A, 'w') as f2:
            for i in QA_pair[:train_idx]:
                f1.writelines(i[0] + '\n')
                f2.writelines(i[1] + '\n')
                f.writelines(i[0] + '\n')
                f.writelines(i[1] + '\n')


# dump valid data
with open(total_QA, 'w') as f:
    with open(val_Q, 'w') as f1:
        with open(val_A, 'w') as f2:
            for i in QA_pair:
            #for i in QA_pair[train_idx:]:
                f1.writelines(i[0] + '\n')
                f2.writelines(i[1] + '\n')
                f.writelines(i[0] + '\n')
                f.writelines(i[1] + '\n')

                      
# copy data to folder
for i in ['mono', 'para']:
    cp_path = os.path.join(dst_root, i)
    subprocess.call(['cp', train_Q, cp_path])
    subprocess.call(['cp', train_A, cp_path])
    subprocess.call(['cp', val_Q, cp_path])
    subprocess.call(['cp', val_A, cp_path])

