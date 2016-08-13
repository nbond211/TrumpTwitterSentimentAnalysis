function analyzeSentiment(tweetId) {
    console.log($('#tweet-' + tweetId).text());
    $.post("/sentiment",
           {'text': $('#tweet-' + tweetId).text()},
           function(data) {console.log(data);});
}