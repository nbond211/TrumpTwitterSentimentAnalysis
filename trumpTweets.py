import twitter
import time
from datetime import datetime


class TrumpTweetsViewModel:
    def __init__(self, twitterData):
        self.profileImage = twitterData[0].user.profile_image_url
        self.screenName = twitterData[0].user.screen_name
        self.tweets = []
        for tweet in twitterData:
            ts = time.strptime(tweet.created_at,'%a %b %d %H:%M:%S +0000 %Y')
            dt = datetime.fromtimestamp(time.mktime(ts))
            self.tweets.append({'dateCreated': dt, 'id': tweet.id, 'text': tweet.text})


api = twitter.Api(consumer_key='ts7ocCeuQXjhmlPOWV67r4luM',
                  consumer_secret='M4v7k0bgA28UB4nA1JtJUdZGBMet40fQSHib2AmUGYmyU2M5yb',
                  access_token_key='3709897817-AJ2mG11lM8uJnKXY4bZynGv9bAhj2MhJkmwexGg',
                  access_token_secret='DbnnDa4hcghFkNtte5Y8z2iOBHG2p5rzNAcmLqDa0s0Tr')


def get_latest_trump_tweets():
    tweets = api.GetUserTimeline(user_id=25073877, count=100)
    return TrumpTweetsViewModel(tweets)
