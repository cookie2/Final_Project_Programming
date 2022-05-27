import re
import csv
import nltk
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

def senttokenize(sentence):
    lower_sentence = sentence.lower()
    temp = re.sub('[\.\!\?]', '|||', lower_sentence)
    each_sentences = temp.split('|||')

def wordtokenize(sentence):
    nltk.download("punkt")
    lower_sentence = sentence.lower()
    tokenized_sentence = nltk.word_tokenize(lower_sentence)
    for word in tokenized_sentence:
        if word in stopwords.words('english'):
            tokenized_sentence.remove(word)
    print('Use NLTK to do preprocessing:', tokenized_sentence, sep="\n")

def read_data():
    with open('result.csv' , 'r', newline='') as csvfile:
        rows = csv.reader(csvfile)
        return rows

if __name__ == "__main__":
    resp = read_data()
    