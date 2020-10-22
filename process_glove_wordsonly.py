from tqdm import tqdm
import pickle
import numpy as np
# import embedding resource glove pretrained data
GloVe_path="DataSet\\glove.840B.300d.txt"
def load_glove(path):
    glove_dict = dict()
    words = list()
    with open(path, mode='r', encoding="utf-8") as vec_file:
        for line in tqdm(vec_file):
            values = line.split()
            word = values[0]
            words.append(word)

    print("There are {0} distinct words in this pretrained GloVe DataSet.".format(len(words)))
    return words

glove_words = load_glove(GloVe_path)

def save_data(path,data):
    pickle_file = open(path, mode='wb')
    pickle.dump(data, pickle_file)
    pickle_file.close()
    print("the data of glove is saved successfully!")

save_data("DataSet\\glove.840B.300d_words.pkl",glove_words)