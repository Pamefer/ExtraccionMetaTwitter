from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "317539721-AT9JmdQoTrmTWKi8kIApcPRwE6Cipddf0S8cLiqX"
access_token_secret = "6HVqjy6yFGIHtuLRZXLgoq6CivgkG6ia3Pj3SV6sWKKGx"
consumer_key = "U84DAT2PRnJoT7abyK4vnA1p2"
consumer_secret = "3XY3y7iHRdsblreicNMOnp4tioOocMxefR1CDze4QSa5QPu0Up"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #Filtra tweets en base a palabras
    stream.filter(track=['loja', 'turismo', 'millones'])
