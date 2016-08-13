import unirest


class Sentiment:
    def __init__(self, positive, negative, neutral):
        self.positive = int((positive * 100))
        self.negative = int((negative * 100))
        self.neutral = int((neutral * 100))

    def serialize(self):
        return {
            'positive': self.positive,
            'negative': self.negative,
            'neutral': self.neutral
        }


def analyze_tweet(text):
    response = unirest.post("http://text-processing.com/api/sentiment/",
                            headers={
                                "Content-Type": "application/x-www-form-urlencoded",
                                "Accept": "application/json"
                            },
                            params={
                                "language": "english",
                                "text": text
                            }
                            )
    pos = response.body['probability']['pos']
    neg = response.body['probability']['neg']
    neutral = response.body['probability']['neutral']
    return Sentiment(pos, neg, neutral)
