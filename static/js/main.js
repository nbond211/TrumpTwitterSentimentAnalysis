function analyzeSentiment(tweetId) {
    console.log($('#tweet-' + tweetId).text());
    $.post("/sentiment",
           {'text': $('#tweet-' + tweetId).text()},
           function(data) {console.log(createVisualization(data.positive, data.negative));});
}

function createVisualization(positive, negative) {
    
}