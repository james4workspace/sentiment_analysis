# sentiment_analysis

## 1.Libraries Importion

There are some general library requirements for the project and some which are specific to individual methods. The general requirements are as follows.

* `numpy`
* `pandas`
* `bs4`
* `urllib`
* `re`
* `tqdm`
* `pickle`
* `gensim`
* `nltk`
* `sklearn`
* `spellchecker`
* `operator`
* `tensorflow`
* `keras`
* `matplotlib`

## 2.Third Party Resources Preparation

According to Preprocessing, word2vec and glove are both not able to convert emoji or emoticon into vector. But in sentiment analysis, emoji and emoticon are strong expression for stating emotion. Thus, I searched for authoriative explaination of emoji and emoticon and got 2 links for explaining the exact meaning of emoji/emoticon:

* `https://en.wikipedia.org/wiki/List_of_emoticons`
* `https://unicode.org/emoji/charts/emoji-list.html`

For the purpose of crawling down all the information provided by these 2 links, I built 2 py files namely `web_crawl_emoji.py` and `web_crawl_emoticon.py`.
`web_crawl_emoji.py` is for link from `https://unicode.org/emoji/charts/emoji-list.html`, while `web_crawl_emoticon.py` is for `https://en.wikipedia.org/wiki/List_of_emoticons`. 

After using `web_crawl_emoji.py`, we can have `emoji_meaning.csv`, which demonstrates the exact meaning of certain emoji within the dataframe.
After using `web_crawl_emoticon.py`, we can have `emo_meaning.csv`, which demonstrates the exact meaning of certain emoji within the dataframe.

And `web_crawl_merge.py` is for emerging the dataframes built by `web_crawl_emoji.py` and `web_crawl_emoticon.py`. And it built `emo_collection.csv` as its production.
