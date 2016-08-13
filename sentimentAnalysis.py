import unirest


class Sentiment:
    def __init__(self, positive, negative):
        self.positive = int((positive * 100))
        self.negative = int((negative * 100))

    def serialize(self):
        return {
            'positive': self.positive,
            'negative': self.negative
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
    return Sentiment(pos, neg)
