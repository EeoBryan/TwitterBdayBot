import tweepy
from keys import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

BDAY_ARRAY = ['happy birthday', 'hb', 'happy bday']

print('Testing...')

for mention in reversed(mentions):
    print('id: ' + str(mention.id) + ' - ' + mention.text, flush=True)
    #previous_id = mention.id
    #store_last_seen_id(previous_id, FILE_NAME)

    for bdday_text in BDAY_ARRAY:
        if bdday_text in mention.text.lower():
            print("Someone said Happy Birthday")
            api.update_status('@' + mention.user.screen_name
            +' Thank You ' + mention.user.screen_name +'! #TestRun', mention.id)
