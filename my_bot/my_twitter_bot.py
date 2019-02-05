import tweepy
import time

from keys import *

print('startin BdayBot200...')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

BDAY_ARRAY = ['happy birthday', 'hb', 'happy bday']

FILE_NAME = 'previous_ids.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    previous_id = int(f_read.read().strip())
    f_read.close()
    return previous_id

def store_last_seen_id(previous_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(previous_id))
    f_write.close()
    return

def reply_back():

    id_count = 0

    print('Retrieving tweets...', flush=True)
    previous_id = retrieve_last_seen_id(FILE_NAME)

    mentions = api.mentions_timeline(
                                    previous_id,
                                    tweet_mode='extended')

    for mention in reversed(mentions):
        if hasattr(mention, 'happy birthday'):
            print('id count: ' + str(id_count) +'id: ' + str(mention.id) + ' - ' + mention.text, flush=True)
        previous_id = mention.id
        store_last_seen_id(previous_id, FILE_NAME)

        for bdday_text in BDAY_ARRAY:
            if hasattr(mention, 'happy birthday'):
                if bdday_text in mention.text.lower():
                    print("Someone said Happy Birthday")
                    api.update_status('@' + mention.user.screen_name
                    +' Thank You ' + mention.user.screen_name +'! #TestRun', mention.id)
        id_count += 1

while True:
    reply_back()
    time.sleep(15)
