from flask import Flask, render_template, url_for, jsonify, request
import trumpTweets
import sentimentAnalysis

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', tweets=trumpTweets.get_latest_trump_tweets())

@app.route('/sentiment', methods=['POST'])
def sentiment():
    text = request.form['text']
    sentiment = sentimentAnalysis.analyze_tweet(text)
    return jsonify(sentiment.serialize())

if __name__ == '__main__':
    app.run(debug=True)
