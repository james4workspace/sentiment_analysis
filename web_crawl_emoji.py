# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:43:49 2020

Explanation:
in order to manipulate emoji and emoticons from text data,
I found 2 web pages with the explanation of emoji and emoticons.
Here is the web crawl code with Beautiful Soup for downloading the explanation.
And save them as dataframe for further extraction.

Website Link: https://unicode.org/emoji/charts/emoji-list.html

@author: Shenghan ZHANG
"""

from bs4 import BeautifulSoup
import urllib
import re
import pandas as pd
from tqdm import tqdm

url = "https://unicode.org/emoji/charts/emoji-list.html"

# fake header for mimicing human reading page
header = dict()
header['User-Agent'] = "Mozilla/10.0 (Windows NT 10.0; Win64; x64)"
req = urllib.request.Request(url,headers = header)

# import the body of html
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')


# dump html into Beautiful Soup object
soup = BeautifulSoup(html,"lxml")


# emoji meaning extraction
meaning_list=list()
for line in soup.find_all("td",class_ = "name"):
    meaning = line.get_text()
    meaning_list.append(meaning)
    
# emoji extraction
emoji_list = list()
for each_1 in soup.find_all("td",class_ = "andr"):
    for each_2 in each_1.find_all("img"):
        emoji_list.append(each_2["alt"])
   
# seperate the meaning into emoji dictionary
emoji_dict = dict()
length = len(meaning_list)
emoji_dict["short name"]=list()
emoji_dict["other keywords"]=list()
emoji_dict["emoji"] = emoji_list
for i in range(0,length,2):
    emoji_dict["short name"].append(meaning_list[i])
    emoji_dict["other keywords"].append(meaning_list[i+1])

# join the two meaning list together
emoji_dict["key words"]=list()
for i in range(len(emoji_list)):
    if emoji_dict["short name"][i] in emoji_dict["other keywords"][i]:
        sentence = re.sub(r'\|',' ',emoji_dict["other keywords"][i])
        words_list = sentence.split()
        sentence = " ".join(words_list)
        emoji_dict["key words"].append(sentence)
    else:
        sentence = re.sub(r'\|',' ',emoji_dict["short name"][i])
        words_list = sentence.split()
        sentence = " ".join(words_list)
        emoji_dict["key words"].append(sentence)
        
# create dataframe for storing the emoji and its meaning(key words)
df_emoji = pd.DataFrame.from_dict(emoji_dict)
df_emoji = df_emoji.drop(columns=["short name","other keywords"])

path = "DataSet\\emoji_meaning.csv"
df_emoji.to_csv(path,sep='|',index=False)

