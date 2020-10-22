# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:43:49 2020

Explanation:
After crawling 2 web pages for storing the emoji and emoticon explanation as dataframe,
I need to merge these 2 dataframes together as the reference for checking the meaning of certain emoji or emoticon.

These 2 files are:
emoji_meaning.csv
emo_meaning.csv


@author: Shenghan ZHANG
"""

import pandas as pd
import numpy as np
from tqdm import tqdm

parent_path="DataSet\\"
df_emoji=pd.read_csv(parent_path+"emoji_meaning.csv",sep="|")
df_emo=pd.read_csv(parent_path+"emo_meaning.csv",sep="|")

emoji_values=list(df_emoji["emoji"])
emoji_meaning = list(df_emoji["key words"])
emo_values =list(df_emo["emo"])
emo_meaning = list(df_emo["key words"])

# because emoji_meaning.csv crawled from certain research website, so here I take this as standard
# and add new emoji or emoticon from emo_meaning.csv to df_emoji
len_emo = len(emo_values)
for i in range(len_emo):
    if emo_values[i] not in emoji_values:
        emoji_values.append(emo_values[i])
        emoji_meaning.append(emo_meaning[i])

emo_all=dict()
emo_all["emoji/emoticon"]=emoji_values
emo_all["key words"]=emoji_meaning

# create dataframe for storing the emojis and emoticons and their meanings(key words)
df_emo_all = pd.DataFrame.from_dict(emo_all)


# save final dataframe of emoji and emoticons
path = "DataSet\\emo_collection.csv"
df_emo_all.to_csv(path,sep='|',index=False)

def fit_transform(input_dict,method):
    output_dict=dict()
    for key in input_dict.keys():
        processed_texts = list()
        for text in tqdm(input_dict[key]):
            processed_single_text = eval(method)(text)
            processed_texts.append(processed_single_text)
        
        output_dict[key]=processed_texts
    
    return output_dict
