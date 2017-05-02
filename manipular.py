#python test.py
import json

import pandas as pd
import matplotlib.pyplot as plt
import re

#archivo donde estan los tweets
tweets_data_path = 'guardar.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
print 'Tweets Recuperados: ', len(tweets_data)

tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['retweeted'] = map(lambda tweet: tweet['retweeted'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
print tweets



#hasthags
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

tweets['loja'] = tweets['text'].apply(lambda tweet: word_in_text('loja', tweet))
tweets['turismo'] = tweets['text'].apply(lambda tweet: word_in_text('turismo', tweet))
tweets['millones'] = tweets['text'].apply(lambda tweet: word_in_text('millones', tweet))

print 'tweets con hashtag turismo: ', tweets['turismo'].value_counts()[True]
print 'tweets con hashtag loja: ', tweets['loja'].value_counts()[True]
print 'tweets con palabra millones: ', tweets['millones'].value_counts()[True]



#palbras en descripcion

tweets['loja'] = tweets['text'].apply(lambda tweet: word_in_text('loja', tweet))
print 'tweets con descripcion loja: ', tweets['loja'].value_counts()[True]

tweets['millones'] = tweets['text'].apply(lambda tweet: word_in_text('millones', tweet))
print 'tweets con descripcion millones: ', tweets['millones'].value_counts()[True]


#print tweets['programming'].value_counts()[True]










