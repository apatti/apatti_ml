__author__ = 'apatti'

#tutorial from kaggle
#introduction to NLP

import pandas as pd
from bs4 import BeautifulSoup
import re
import nltk
nltk.download()

from nltk.corpus import stopwords

def review_to_words(review_text):
    #remove html
    review_text = BeautifulSoup.get_text(review_text)

    #remove puntuation and numbers
    review_text = re.sub("[^a-zA-Z]"," ",review_text)

    #convert to lower case
    review_text = review_text.lower()

    #words
    review_words = review_text.split()

    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))

    #remove stop words
    review_words = [w for w in review_words if not w in stops]

    #There are many other things we could do to the data - For example, Porter Stemming and
    # Lemmatizing (both available in NLTK) would allow us to treat "messages", "message", and "messaging"
    # as the same word, which could certainly be useful.

    return (" ".join(review_words))

if __name__ == '__main__':
    #header=0 --> First line contains column names
    #quoting=3 --> ignore double quotes in the file.
    train = pd.read_csv("labeledTrainData.tsv", header=0, delimiter="\t",quoting=3)

    #number of rows and columns
    #(25000,3)
    #print train.shape

    #column names
    #id,sentiment, review
    #print train.columns.values

    clean_train_reviews = []

    clean_train_reviews = [review_to_words(review) for review in train["review"]]

    print clean_train_reviews[1:2]






