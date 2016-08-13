import twitter

api = twitter.Api(consumer_key='ts7ocCeuQXjhmlPOWV67r4luM',
                  consumer_secret='M4v7k0bgA28UB4nA1JtJUdZGBMet40fQSHib2AmUGYmyU2M5yb',
                  access_token_key='3709897817-AJ2mG11lM8uJnKXY4bZynGv9bAhj2MhJkmwexGg',
                  access_token_secret='DbnnDa4hcghFkNtte5Y8z2iOBHG2p5rzNAcmLqDa0s0Tr')


def get_latest_trump_tweets():
    tweets = api.GetUserTimeline(user_id=25073877, count=100)
    return tweets
