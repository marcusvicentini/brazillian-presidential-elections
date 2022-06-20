import pymysql
import json
import tweepy as tw
from googletrans import Translator

# Twitter API credentials: 
api_key = "enter yours"
api_key_secret = "enter yours"
bearer_token = "enter yours"


def get_tweets(search_string):
    """Get the twitter search result for search string"""
    client = tw.Client(bearer_token)
    data = client.search_recent_tweets(search_string, max_results=30)
    tweets = data.data
    return tweets

# AWS database credentials
endpoint = 'enter yours'
username = 'admin'
password = 'enter yours'
database_name = 'enter yours'



def mysql_insert_tweet(search_string, table_name):
    """
    Get tweets, translate to english and store in mysql server on aws
    """
    connection = pymysql.connect(host=endpoint, user=username, password=password, db=database_name)

    data_twitter = get_tweets(search_string)
    translator = Translator()

    sql = "insert into" + " " + table_name + " (text) values(%s)"

    for tweet in data_twitter:

        twe = translator.translate(tweet.text).text

        val = twe
        cursor = connection.cursor()
        cursor.execute(sql, val)
        connection.commit()
    connection.close()
        


# To change the targeted mention, you just have to change '@LulaOficial' for another twitter account, keep
# the rest to eliminate retweets
# The second argument is the DB name, use as you named yours
def lambda_handler(event, context):
    mysql_insert_tweet('@LulaOficial -is:retweet', 'Lula')
    
