"""Sentiment analysis flask app"""
from flask import Flask, request, render_template
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")
''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    if not text_to_analyze:
        return "The prompt is empty, try again."

    result = sentiment_analyzer(text_to_analyze)
    if result["label"]:
        label = result["label"]
        score = result["score"]
        return f"The given text has been identified as {label.split('_')[1]} \
            with a score of {score}."
    return "Invalid input ! Try again."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    