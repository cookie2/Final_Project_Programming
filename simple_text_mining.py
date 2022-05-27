import re
import nltk
from nltk import word_tokenize
from nltk.probability import FreqDist

def senttokenize(sentence):
    lower_sentence = sentence.lower()
    temp = re.sub('[\.\!\?]', '|||', lower_sentence)
    each_sentences = temp.split('|||')

def wordtokenize(sentence):
    nltk.download("punkt")
    lower_sentence = sentence.lower()
    tokenized_sentence = nltk.word_tokenize(lower_sentence)