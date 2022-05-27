import re
import numpy as np
import pandas as pd
from pprint import pprint
# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
# spacy for lemmatization
import spacy
# Plotting tools
import pyLDAvis
import pyLDAvis.gensim_models # if you have error messege, try 'import pyLDAvis.gensim'
import matplotlib.pyplot as plt
# Enable logging for gensim - optional
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)
#
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
#
from nltk.corpus import stopwords

stop_words = stopwords.words('english')

def import_dataset():
    df = pd.read_csv('result.csv')
    return df

def sent_to_words(df):
    # df.review is for mine, you should edit it according your dataset.
    sentences = df.review.values.tolist()
    for sentence in sentences:
        # deacc=True removes punctuations
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))

def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

def make_bigrams(texts, bigram_mod, trigram_mod):
    return [bigram_mod[doc] for doc in texts]

def make_trigrams(texts, bigram_mod, trigram_mod):
    return [trigram_mod[bigram_mod[doc]] for doc in texts]

def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent))
        texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return texts_out


    
def build_model(data_words):
    # higher threshold fewer phrases.
    bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100)
    trigram = gensim.models.Phrases(bigram[data_words], threshold=100)

    # Faster way to get a sentence clubbed as a trigram/bigram
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    trigram_mod = gensim.models.phrases.Phraser(trigram)

    # See trigram example
    print(trigram_mod[bigram_mod[data_words[0]]])

    return bigram_mod, trigram_mod

if __name__ == "__main__":
    
    #get dataset
    dataset = import_dataset()

    # Tokenize
    data_words = list(sent_to_words(dataset))
    pprint(data_words[:1])
    
    # Build Model
    bigram_mod, trigram_mod = build_model(data_words)
    
    # Remove Stop Words
    data_words_nostops = remove_stopwords(data_words)
    
    # Form Bigrams
    data_words_bigrams = make_bigrams(data_words_nostops, bigram_mod, trigram_mod)
    
    # Initialize spacy 'en_core_web_sm' model, keeping only tagger component (for efficiency)
    # python3 -m spacy download en_core_web_sm
    nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

    # Do lemmatization keeping only noun, adj, vb, adv
    data_lemmatized = lemmatization(data_words_bigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
    
    # Create Dictionary
    id2word = corpora.Dictionary(data_lemmatized)
    
    # Create Corpus
    texts = data_lemmatized
    
    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]
    
    # View
    print(corpus[:1])
    
    # Build LDA model
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
        id2word=id2word,
        num_topics=20,
        random_state=100,
        update_every=1,
        chunksize=100,
        passes=10,
        alpha='auto',
        per_word_topics=True)
    
    # Print the Keyword in the 10 topics
    print(lda_model.print_topics())
    doc_lda = lda_model[corpus]
    
    # Count Perplexity
    print('Perplexity: ', lda_model.log_perplexity(corpus))
    
    # Count Coherence
    coherence_model_lda = CoherenceModel(model=lda_model, texts=data_lemmatized, dictionary=id2word, coherence='c_v')
    coherence_lda = coherence_model_lda.get_coherence()
    print('Coherence Score: ', coherence_lda)
    
    # Visualize the topics
    visualisation = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word, mds = "mmds")
    pyLDAvis.save_html(visualisation, 'LDA_Visualization.html')
