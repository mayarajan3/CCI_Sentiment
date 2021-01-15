#!/usr/bin/env python
# coding: utf-8

#The data type is JSON type.
import pandas as pd
import json
import collections

df = pd.read_csv('twitterdata.csv', encoding = 'latin_1')
df1 = pd.read_csv('myhashtags.csv', header=None).rename(columns = {0:'npu'})

hashtag = df['lowe case'].dropna().apply(lambda x: x.split(' | '))
mapping = df1['npu'].str.lower().tolist()


def func(x, mapping):
    for i in x:
        if i in mapping:
            res = i
        else:
            res = None
    return res


hashtag_cleaned = hashtag.apply(lambda x: func(x, mapping)).dropna().reset_index()

df_cleaned = pd.merge(hashtag_cleaned, df[['tweet_text']], left_on = 'index', right_index = True)\
    .drop('index', axis = 1).rename(columns = {'lowe case':'npu'})


dic = collections.defaultdict(list)
for i in range(len(df_cleaned['npu'])):
    dic[df_cleaned['npu'][i]].append(df_cleaned['tweet_text'][i])
output = dict(dic)

dp = json.dumps(output)
f = open('hashtag cleaned.json', 'w')
f.write(dp)
