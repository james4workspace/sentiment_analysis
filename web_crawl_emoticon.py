# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:43:49 2020

Explanation:
in order to manipulate emoji and emoticons from text data,
I found 2 web pages with the explanation of emoji and emoticons.
Here is the web crawl code with Beautiful Soup for downloading the explanation.
And save them as dataframe for further extraction.

Website Link: https://en.wikipedia.org/wiki/List_of_emoticons

@author: Shenghan ZHANG
"""

from bs4 import BeautifulSoup
import urllib
import re
import pandas as pd
from tqdm import tqdm
url = "https://en.wikipedia.org/wiki/List_of_emoticons"

# fake header for mimicing human reading page
header = dict()
header['User-Agent'] = "Mozilla/10.0 (Windows NT 10.0; Win64; x64)"
req = urllib.request.Request(url,headers = header)

# import the body of html
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')


# dump html into Beautiful Soup object
soup = BeautifulSoup(html,"lxml")

data = list()

# extract table into rows
tables = soup.find_all("table",class_="wikitable")
    
# because different table has different format, we extract data from table one by one

# first table
table_body = tables[0].find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    new_cells=list()
    for element in cells:
        #print(element)
        if element.text:
            if "<a href" in str(element):
                ele = element.text
                ele = re.sub(r'\[\d\]','',ele)
                ele = re.sub(r'\n','',ele)
                ele = [ele]
            else:
                ele = re.sub(r'\<\/?td\>','',str(element))
                ele = re.sub(r'\<td colspan\=\"\d+\"\>','',ele)
                ele = re.sub(r'<blockquote><blockquote><blockquote><blockquote><p>','',ele)
                ele = re.sub(r'</p></blockquote></blockquote></blockquote></blockquote>','',ele)
                ele = re.sub(r'\<br\/?\>','AND',ele)
                ele = re.sub(r'\n','',ele)
                ele = re.sub(r'[^ a-zA-Z\d\/\*\:\)\.\,\?\^\;?\-\‑\_\'~!\<\>\=\"#&$%\\\{\}\|\[\]ç\+ω○\@¡éı・…¡\`：）♡ӳ！“”à≧∇≦♂ş≈¬⊄─✔•×ü–₹。ó°ʖ—¶ķñ฿ĺ∑；⏸]','\g<0>AND',ele)
                ele = ele.split(sep="AND")
                try:
                    while True:
                        ele.remove('')
                except:
                    pass
        new_cells = new_cells + ele
    if new_cells !=[]:
        data.append(new_cells)
        
        
# second table
table_body = tables[1].find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    new_cells=list()
    for element in cells:
        #print(element)
        if element.text:
            ele = element.text
        new_cells = new_cells + [ele]
    if new_cells !=[]:
        data.append(new_cells)

# third table
table_body = tables[2].find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    new_cells=list()
    for element in cells:
        #print(element)
        if element.text:
            ele = element.text
        new_cells = new_cells + [ele]
    if new_cells !=[]:
        data.append(new_cells)
    


# ignore 4th table
# 5th table
table_body = tables[4].find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    new_cells=list()
    for element in cells:
        #print(element)
        if element.text:
            if "span" in str(element):
                big=list()
                small=list()
                new_big=list()
                blocks = element.find_all("span",style="white-space:nowrap")
                for block in blocks:
                    big.append(block.text)
                    for small_block in block.find_all("span",style="margin-left:1.5em"):
                        small.append(small_block.text)
                
                for b in range(len(big)):
                    new_big_one = big[b]
                    for s in range(len(small)):
                        if small[s] in big[b]:
                            new_big_one = new_big_one.replace(small[s],'')
                    new_big.append(new_big_one)
                

                new_cells = new_cells + small + new_big
                
                    
            else:
                ele = element.text
                ele = re.sub(r'[^ a-zA-Z\d\/\*\:\)\.\,\?\^\;?\-_\'~!\<\>\=\"#&$%\\\{\}\|\[\]ç\+ω○\@¡éı・…¡\`：）♡ӳ！“”à≧∇≦♂ş≈¬⊄─✔•×ü–₹。ó°ʖ—¶ķñ฿ĺ∑；⏸]','\g<0>AND',ele)
                ele = ele.split(sep="AND")
                try:
                    while True:
                        ele.remove('')
                except:
                    pass
                new_cells = new_cells + ele
    if new_cells !=[]:
        data.append(new_cells)

# 6th table
table_body = tables[5].find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    new_cells=list()
    for element in cells:
        #print(element)
        if element.text:
            if "span" in str(element):
                blocks = element.find_all("span")
                seperated_emo=list()
                for block in blocks:
                   ele = block.text
                   seperated_emo.append(ele)
                   
                single = seperated_emo[0]
                for i in range(len(seperated_emo)-1):
                    if seperated_emo[i+1] in seperated_emo[0]:
                        single = seperated_emo[0].replace(seperated_emo[i+1],'')
                seperated_emo[0]=single
                new_cells = new_cells + seperated_emo
                
                    
            else:
                ele = element.text
                ele = re.sub(r'[^ a-zA-Z\d\/\*\:\)\.\,\?\^\;?\-_\'~!\<\>\=\"#&$%\\\{\}\|\[\]ç\+ω○\@¡éı・…¡\`：）♡ӳ！“”à≧∇≦♂ş≈¬⊄─✔•×ü–₹。ó°ʖ—¶ķñ฿ĺ∑；⏸]','\g<0>AND',ele)
                ele = ele.split(sep="AND")
                try:
                    while True:
                        ele.remove('')
                except:
                    pass
                new_cells = new_cells + ele
    if new_cells !=[]:
        data.append(new_cells)
        
# 7th table
table_body = tables[6].find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    new_cells=list()
    for element in cells:
        #print(element)
        ele = element.text
        new_cells = new_cells + [ele]
    if new_cells !=[]:
        data.append(new_cells)

# 8th table
table_body = tables[7].find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    new_cells=list()
    for element in cells:
        #print(element)
        ele = element.text
        new_cells = new_cells + [ele]
    if new_cells !=[]:
        data.append(new_cells)

# ignore 9th table


# turn the data into dict
emo_dict = dict()
emo_dict["emo"]=list()
emo_dict["key words"]=list()
import numpy as np

for row in data:
    length = len(row)
    key_words=row[length-1]
    key_words=re.sub(r'\[\d+\]','',key_words)
    list_emo = row[:length-1]
    for each in list_emo:
        # get rid of none value
        if each !="" and each != " " and each !="\n" and each !="\"\n\"" and each !="\'\n\'":
            if len(each) == 1:
                # get rid of only one charactor such as "(", which is definitly not emoticon
                str_rep = re.sub(r'[\－\da-zA-Z\/\*\:\)\.\?\^\;?\-_\'~!\<\>\=\"#&$%\\\{\}\|\[\]ç\+ω○\@¡éı・…¡\`]','R',each)
                if str_rep !='R':  
                    emo_dict["emo"].append(each)
                    emo_dict["key words"].append(key_words)
            else:
                emo_dict["emo"].append(each)
                emo_dict["key words"].append(key_words)

new_emo = list()
new_key_word=list()

# get rid of repetitive values
for i in range(len(emo_dict["emo"])):
    if emo_dict["emo"][i] not in new_emo:
        new_emo.append(emo_dict["emo"][i])
        new_key_word.append(emo_dict["key words"][i])

# form final dictionary with emoji, emoticon and key words.
emo_dict["emo"]=new_emo
emo_dict["key words"]=new_key_word

# create dataframe for storing the emo and its meaning(key words)
df_emo = pd.DataFrame.from_dict(emo_dict)

path = "DataSet\\emo_meaning.csv"
df_emo.to_csv(path,sep='|',index=False)


    
            
            
            
            