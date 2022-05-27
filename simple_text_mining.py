import re
import csv
import nltk
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from numpy import array

nltk.download('stopwords')

def senttokenize(sentence):
    lower_sentence = sentence.lower()
    temp = re.sub('[\.\!\?]', '|||', lower_sentence)
    each_sentences = temp.split('|||')

def wordtokenize(sentences):
    # transfer array to string
    sentence = " ".join(sentences)
    # download the dictionary
    nltk.download("punkt")
    # lower the sentence and tokenize it
    lower_sentence = sentence.lower()
    tokenized_sentence = nltk.word_tokenize(lower_sentence)
    #delete stop word
    resp = []
    for word in tokenized_sentence:
        if word not in stopwords.words('english'):
            resp.append(word)
    # removing punctuations
    tokenizer = RegexpTokenizer(r"\w+")
    resp = tokenizer.tokenize(' '.join(resp))
    return resp

# if your csv file is too large, transfer to use pandas.read_csv and research how pandas.read_csv chunk works
def read_data():
    fp = open("result.csv", "r", encoding="utf-8")
    data = fp.readlines()
    fp.close()
    return data

if __name__ == "__main__":
    # read data, return an array
    req = read_data()
    # word tokenize
    resp = wordtokenize(req)
    print('Use NLTK to do preprocessing:', resp, sep="\n")
    # do whatever you want ...