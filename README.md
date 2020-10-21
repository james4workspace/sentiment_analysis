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
### 2.1.Emoji/Emoticon Explaination Resource

According to Preprocessing, word2vec and glove are both not able to convert emoji or emoticon into vector. But in sentiment analysis, emoji and emoticon are strong expression for stating emotion. Thus, I searched for authoriative explaination of emoji and emoticon and got 2 links for explaining the exact meaning of emoji/emoticon:

* `https://en.wikipedia.org/wiki/List_of_emoticons`
* `https://unicode.org/emoji/charts/emoji-list.html`

For the purpose of crawling down all the information provided by these 2 links, I built 2 py files namely `web_crawl_emoji.py` and `web_crawl_emoticon.py`.
`web_crawl_emoji.py` is for link from `https://unicode.org/emoji/charts/emoji-list.html`, while `web_crawl_emoticon.py` is for `https://en.wikipedia.org/wiki/List_of_emoticons`. 

After using `web_crawl_emoji.py`, we can have `emoji_meaning.csv`, which demonstrates the exact meaning of certain emoji within the dataframe.
After using `web_crawl_emoticon.py`, we can have `emo_meaning.csv`, which demonstrates the exact meaning of certain emoji within the dataframe.

And `web_crawl_merge.py` is for emerging the dataframes built by `web_crawl_emoji.py` and `web_crawl_emoticon.py`. And it built `emo_collection.csv` as its production.

`emo_collection_glove.csv` is built by transforming the text of meaning to the requirement of GloVe as much as possible.

`emo_collection_word2vec.csv` is built by transforming the text of meaning to the requirement of Word2Vec as much as possible.

### 2.2.Pretrained Word2Vec Resource and Pretrained GloVe Resource

Since vector embedding is not the topic of this project, I simply use pretrained word2vec resource and pretrained GloVe resource for transforming certain words into vectors.

For word2vec, I use the lexicon called `GoogleNews-vectors-negative300.bin.gz` provided by "Google Archive", and here is the link below:

* `https://code.google.com/archive/p/word2vec/`

For GloVe, I use the lexicon called `glove.840B.300d.txt` provided by Jeffrey Pennington,  Richard Socher,  Christopher D. Manning, and here is the link below:

* `https://nlp.stanford.edu/projects/glove/`

And for easy use, I built `process_glove_wordsonly.py` to process lexicon `glove.840B.300d.txt`, in order to gather its distinct vocabulary and saved it as list type `glove.840B.300d_words.pkl`.

# Coding Explaination

Here I will explain the function of each coding file according the process of sentiment analysis prediction.

## 3.Preprocessing
### 3.1.Preprocessing data based on different word embedding lexicon

It's because I'm using pretrained word embedding lexicon, I have no idea which word with which format can be represented into vector correctly according the word embedding lexicon I imported. That's why I built 6 different `.ipynb` files for preprocessing data. Here are the names of them below:

* `Preprocessing_EmojiEmoticon_GloVe.ipynb`
* `Preprocessing_EmojiEmoticon_word2vec.ipynb`
* `Preprocessing_TrainData_GloVe.ipynb`
* `Preprocessing_TrainData_Word2vec.ipynb`
* `Preprocessing_TestData_GloVe.ipynb`
* `Preprocessing_TestData_Word2vec.ipynb`

Based on their names, you can see that I do preprocessing based on different word embedding, though the procedures inside the file are the same. I will explain the procedures below:

#### (1) set label category into categorical numbers

Since the label of original data are formed by 4 different textual categories namely "happy, sad, angry, others", I need to transfer them into categorical numbers for classification. The order is: `{"others":0,"happy":1,"sad":2,"angry":3}`, and save them as `train_y.pkl` and `test_y.pkl`, which are from train dataset and test dataset.

#### (2) combination

Though there are 3 turns of texts provided by train and test dataset, actually I only need one text for each row as train or test dataset. So here is the part I combine 3 turns' texts together as one. Besides, since I need to extract emoji/emoticon later, and their positions in text are also important, I still keep the 3 turns' texts.

#### (3) extract emoji/emoticon

In this part, I extracted emoji/emoticon from each text based on `emo_collection_glove.csv` and `emo_collection_word2vec.csv` according to different word embedding I'm using. These 2 dataframes are built also by preprocessing based on GloVe and Word2Vec, this is because I need to substitute the emoji/emoticon with its meaning.

* e.g. "but I'm in love with it 😁😁" -> "but I'm in love with it " & [2,"grin smile"] 
* explaination: 2 means this emoji/emoticon happened in text 2 times, and "grin smile" is its meaning.

The extraction of emoji/emoticon are later stored as `.pkl` file with names such as "extraction_emo_3_test_glove.pkl"

#### (4)
