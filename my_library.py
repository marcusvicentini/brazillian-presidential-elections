import json
import pandas as pd
import tweepy as tw
from textblob import TextBlob
from unidecode import unidecode
import seaborn as sns
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
import re
import pymysql

def clean_tweet(tweet):
        """
        clean tweet text by removing links, special characters
        using simple regex statements.
        """
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def remove_stop_words(sentence):
    """
    Remove stop words from the given sentence
    """
    sentence = sentence.lower()
    stopwords_set = set(stopwords.words('english'))
    palavras = [i for i in sentence.split() if not i in stopwords_set]
    return (" ".join(palavras))

def stemmigg_tweets(sentence):
    stemmer = RSLPStemmer()
    words = []
    for word in sentence.split():
        words.append(stemmer.stem(word))
    return (" ".join(words))

def preprocess_data_pipe(data):
    """ Apply all functions to preprocess tweets, removing stop words and special characters"""
    data = clean_tweet(data)
    data = remove_stop_words(data)
    data = data.replace('rt', '')
    data = stemmigg_tweets(data)
    return data

def get_items_aws(table_name, aws_endpoint, aws_user, aws_password, aws_dbname):
    """
    Return all data from a table in aws. Return a Series of items
    """

    connection = pymysql.connect(host= aws_endpoint,
                             user= aws_user, 
                             password= aws_password, 
                             db= aws_dbname)
    
    cursor = connection.cursor()
    sql = "select * from " + table_name
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.close()
    return rows

def sentiment_classes(polarity):
    """
    Create 3 classes depending on polarity
    """
    if polarity < 0:
        return 'negative'
    elif polarity == 0:
        return 'neutral'
    else:
        return 'positive'

def transform_sentiment_classes(text):
    """
    Perform a sentiment analysys on a sentence and then classify it 
    according to sentiment_classes() function
    """
    polarity = TextBlob(text).polarity
    return sentiment_classes(polarity)
