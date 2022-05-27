import re
import csv
import nltk
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

nltk.download('stopwords')

def senttokenize(sentence):
    lower_sentence = sentence.lower()
    temp = re.sub('[\.\!\?]', '|||', lower_sentence)
    each_sentences = temp.split('|||')

def wordtokenize(sentences):
    sentence = " ".join(sentences)
    sentence = re.sub(r'[^\w\s]','', sentence)
    nltk.download("punkt")
    lower_sentence = sentence.lower()
    tokenized_sentence = nltk.word_tokenize(lower_sentence)
    for word in tokenized_sentence:
        if word in stopwords.words('english'):
            tokenized_sentence.remove(word)
    return tokenized_sentence

#if your csv file is too large, transfer to use pandas.read_csv and research how pandas.read_csv chunk works
def read_data():
    fp = open("result.csv", "r", encoding="utf-8")
    data = fp.readlines()
    fp.close()
    return data

if __name__ == "__main__":
    req = read_data()
    resp = wordtokenize(req)
    print('Use NLTK to do preprocessing:', resp, sep="\n")
