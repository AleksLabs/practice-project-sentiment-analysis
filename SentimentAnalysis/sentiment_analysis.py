"""Sentiment analysis with watson"""
import json
import requests

def sentiment_analyzer(text_to_analyse):
    """Sentiment analysis with watson"""
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1\
        /NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header, timeout=60)
    formatted_response = json.loads(response.text)
    status_code = response.status_code
    if status_code == 200:
        formatted_response = json.loads(response.text)
        label = formatted_response["documentSentiment"]["label"]
        score = formatted_response["documentSentiment"]["score"]
        return {"label": label, "score": score, "status_code": status_code}
    return {"label": None, "score": None, "status_code": status_code}
