
# import embedding resource glove pretrained data
GloVe_path="DataSet\\glove.840B.300d.txt"
def load_glove(path):
    glove_dict = dict()
    words = list()
    with open(path, mode='r', encoding="utf-8") as vec_file:
        no = 0
        for line in vec_file:
            no +=no
            if no == 5:
                eg_file = open("DataSet\\example.txt", mode='a')
                eg_file.write(line)
                break

    print("an example from dataset glove.840B.300d.txt is written")

load_glove(GloVe_path)

#save_data("DataSet\\glove.840B.300d_dict.pkl",glove_dict)