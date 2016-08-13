function analyzeSentiment(tweetId) {
    console.log($('#tweet-' + tweetId).text());
    $.post("/sentiment",
        {'text': $('#tweet-' + tweetId).text()},
        function (data) {
            createVisualization(data.positive, data.negative, data.neutral, tweetId);
        });
}

function createVisualization(positive, negative, neutral, tweetId) {
    var ctx = $('#chart-' + tweetId);

    console.log(ctx);

    var data = {
        labels: [
            "Negative",
            "Positive",
            "Neutral"
        ],
        datasets: [
            {
                data: [negative, positive, neutral],
                backgroundColor: [
                    "#FF6384",
                    "#36A2EB",
                    "#FFCE56"
                ],
                hoverBackgroundColor: [
                    "#FF6384",
                    "#36A2EB",
                    "#FFCE56"
                ]
            }]
    };

    var myDoughnutChart = new Chart(ctx, {
        type: 'doughnut',
        data: data
    });
}