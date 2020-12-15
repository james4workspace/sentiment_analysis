"""

**Author Information**(16 Nov. 2020):

Superviser: Prof.Dr.Goran Glovas

Author: Shenghan ZHANG

E-mail: shezhang@mail.uni-mannheim.de

"""

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
* `keras_self_attention`


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

Please download it and save it in DataSet archive.

For GloVe, I use the lexicon called `glove.840B.300d.txt` provided by Jeffrey Pennington,  Richard Socher,  Christopher D. Manning, and here is the link below:

* `https://nlp.stanford.edu/projects/glove/`

Please download it and save it in DataSet archive.

And for easy use, I built `process_glove_wordsonly.py` to process lexicon `glove.840B.300d.txt`, in order to gather its distinct vocabulary and saved it as list type `glove.840B.300d_words.pkl`.

# Coding Explaination

Here I will explain the function of each coding file according the process of sentiment analysis prediction.

## 3.Preprocessing
### 3.1.Preprocessing data based on TF-IDF word embedding - baseline model
The name of the code file is `Preprocessing_TrainATest_TFIDF.ipynb`, which is for preprocessing of train data into tf-idf vectors and apply the same preprocessing procedure produced by train data to test data. These procedures include lowering the words in text, seperate the adhered words combination such as "you?" into "you ?", remove emoji/emoticons, remove stopwords, remove punctuations, correct missepll and stemming. 

All these procedures were done based on the number of distinct vocabulary of all texts from train data. E.g. "crazzzzy" is same as the word "crazy", if without correction of mispell, they will be taken as 2 different distinct words. So the lower number of the distinct vocabulary of train data, the better the preprocessing is. Especially for TF-IDF word embedding, because the number of vocabulary is also the number of dimension of the vector for one sentence, which means lower the vocabulary can ease the job for model training.

The original number of distinct words vocabulary is 33,024, while after preprocessing, the number turned into 8,399, which is a large improvement. And I take 3 models namely Logistic Regression, SVM, and Kernel SVM as baseline models for checking the performance of TF-IDF word embedding, which you can also check them in the coding files so called `LogisticRegression_baselinemodel.ipynb`, `Kernel_SVM_baselinemodel.ipynb`, `SVM_baselinemodel.ipynb`.

### 3.2.Preprocessing data based on different word embedding lexicon

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

#### (4) lower the words

In this part, I lower the words in text.

* e.g. "Just for time pass" -> "just for time pass"

#### (5) Seperate the adhered words with space and remove redundant emoji, emoticons
Some emoji/emoticon may not be covered by crawled emoji/emoticon explaination dataframe, therefore, I need to clean them out here. And also some words sticked together can make word embedding hard to extract them exactly.

* e.g. "yess i am crazyyy😂😂" -> "yess i am crazyyy 😂 😂" -> "yess i am crazyyy "
* e.g. "when did i?" -> "when did i ?" here "i?" should be seperated into "i ?"

#### (6) Correct common words
There are some words hard to explain in word embedding but necessary to explain, such as "don't", "isn't". Because for example "isn't happy" is on the opposite side of "is happy".
Besides after step (5) the words within punctuation are seperated with space, which also need correction.

* e.g. "he isn ' t happy" -> "he is not happy"

#### (7) Correct missing characters
While checking the dataset in train data, I found out there are a lot of this kind of situation happend in text: "hmmm i can talk no w" or "this is wel l known". So I add function to correct the situation.

#### (8) Remove punctuation
Punctuations are not able to be transfered into vector by word2vec and mostly useless in sentiment analysis. Therefore, I just delete them.

#### (9) Remove stopwords
Since stopwords make sense in sentence with certain order, I only remove those stopwords which can't be transfered into vector due to the limit of word embedding.

Till now, I have the first version of data - data without correction of misspell and translation of shorthand words, and also without emoji/emoticon values inside. I call them "train0" and "test0" through word2vec, "train3" and "test3" through GloVe.

#### (10) Correction of misspell and translation of shorthand words
By using `pyspellchecker`, I can correct the words such as "crazzzy", "amazzzzing". And some words are not able to be translated even via spellchecker, therefore, I translate them hand-crafted.

Till now, I have the second version of data - data with correction of misspell and translation of shorthand words but without emoji/emoticon values. I call them "train1" and "test1" through word2vec, "train4" and "test4" through GloVe.

#### (11) Check coverage of data based on different word embedding
All the process I did above are based on the calculation of coverage of data based on word2vec or GloVe. These information is in `check data format part`. I firstly extract distinct vocabulary of all words in data, and then check how much percentage of the vocabulary can be transfered into vector by word2vec or GloVe. 

And after all those process, I can have coverage of data based on word2vec below:

`In Embedding Index we have 88.91% coverage of distinct vocabulary`

`And we have 99.52% coverage of all text`

`The number of words which are not covered in word2vec resource is: 1249`

And based on GloVe, the final result is below:

`In Embedding Index we have 95.11% coverage of distinct vocabulary`

`And we have 99.85% coverage of all text`

`The number of words which are not covered in word2vec resource is: 551`

### 3.3.transfer data from text into vectors
In `VectorBuild_word2vec.ipynb` and `VectorBuild_glove.ipynb`, I transfered the preprocessed data into vectors for further classification.

While transfering the vectors, I calculate each emoji/emoticon vector by taking the average vector of vectors transfered from its meaning. E.g. `[2,"grin smile"]` -> 2 vector of average vector of word "grin" and word "smile". And I add these emoji/emoticon back to where they were before. Therefore, I have 3rd version of data. They are called "train2" and "test2" based on word2vec, "train5" and "test5" based on GloVe.

### 3.4.data description
| data name  | data version  | word embedding | characteristics |
| ------------- | ------------- | ------------- | ------------- |
| train_df_tfidf.csv  | _baseline | tf-idf  | vectors of train data with correttion of misspell and stemming, but without emoji/emoticon |
| test_df_tfidf.csv  | _baseline | tf-idf  | vectors of train data with correttion of misspell and stemming, but without emoji/emoticon |
| vec_train_a_no_cor_word2vec.pkl  | 0 | word2vec  | vectors of train data without correttion of misspell, emoji/emoticon |
| vec_train_a_no_emo_word2vec.pkl  | 1  | word2vec  | vectors of train data without emoji/emoticon vectors |
| vec_train_a_emo_word2vec.pkl  | 2  | word2vec  | vectors of train data with emoji/emoticon and correction of misspell  |
| vec_train_a_no_cor_glove.pkl  | 3 | GloVe  | vectors of train data without correttion of misspell, emoji/emoticon |
| vec_train_a_no_emo_glove.pkl  | 4  | GloVe | vectors of train data without emoji/emoticon vectors |
| vec_train_a_emo_glove.pkl  | 5  | GloVe | vectors of train data with emoji/emoticon and correction of misspell  |
| vec_test_a_no_cor_word2vec.pkl  | 0 | word2vec  | vectors of test data without correttion of misspell, emoji/emoticon |
| vec_test_a_no_emo_word2vec.pkl  | 1  | word2vec  | vectors of test data without emoji/emoticon vectors |
| vec_test_a_emo_word2vec.pkl  | 2  | word2vec  | vectors of test data with emoji/emoticon and correction of misspell  |
| vec_test_a_no_cor_glove.pkl  | 3 | GloVe  | vectors of test data without correttion of misspell, emoji/emoticon |
| vec_test_a_no_emo_glove.pkl  | 4  | GloVe | vectors of test data without emoji/emoticon vectors |
| vec_test_a_emo_glove.pkl  | 5  | GloVe | vectors of test data with emoji/emoticon and correction of misspell  |

## 4.Models Explaination
### 4.1.Building and Training Phase

According to reference research, I choose 6 models as classifiers to predict the result. There are 6 models are below:

* `Logistic Regression`
* `SVM`
* `Kernel SVM`
* `CNN`
* `LSTM`
* `GRU`

Since it's much easy to explain them in coding, please check them directly in my coding files.

While running these models, I also save the models, their predictions and scores in archive `DataSet` and `Prediction`, if you don't have much time running the models, you could directly load them in the coding file to check the result.

### 4.2.Evaluation Phase

For evaluation, I calculate the accuracy, precision, recall, f1 score for evaluating the result from different version of data under same model. And I also built functions for getting ROC Curve, AUC and P-R Curve, average precision for detailed comparison.

In deep learning models such as CNN, LSTM, GRU, I also built learning curve to show the history of accuracy change and loss change in each epoch.

All these pictures of curves can also be found in archive `Pictures`.

## 5.Evaluation
For further comparison to understand which version of data outperformed in same model comparing with other versions of data, and also for the purpose of understanding which model outperformed other models, I built this coding file named `Evaluation.ipynb`.

In 2nd part "Evaluation on accuracy, precision, f1 score", I built the dataframe to contain all the metrics of evaluations of different data under different model, which is saved as `df_evaluation.xlsx`. The reason why I saved the dataframe as xlsx, it's because it's easy to produce charts demonstrating the comparison of each metrics. You can check them in the xlsx file.

In 3rd part "Evaluation with ROC curve, AUC on same model", I built functions for gathering tpr, fpr, auc, and precision, recall, etc. By using these data, I built charts for showing the performance of different data under same model with different standards, and charts for showing the performance of same data under different model with different standards.

Here I didn't use P-R curve to demonstrate the performance of each model, since AUC can be better for illustrating how good a model or a version of data is.
