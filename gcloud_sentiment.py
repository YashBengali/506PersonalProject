from google.cloud import language
import pandas as pd
import csv

def valence_from_tweets():
    df = pd.read_csv('tweets.csv')
    client = language.LanguageServiceClient()
    sentimentFile = open('sentiments.csv', 'a')
    csvWriter = csv.writer(sentimentFile)
    csvWriter.writerow(['SCORE','MAGNITUDE'])
    for tweet in df['CONTENT']:
        document = {"content": tweet, "type_": language.Document.Type.PLAIN_TEXT, "language":"en"}
        response = client.analyze_sentiment(request = {'document': document, 'encoding_type': language.EncodingType.UTF8})
        score = response.document_sentiment.score
        mag = response.document_sentiment.magnitude
        csvWriter.writerow([score, mag])
    sentimentFile.close()

if __name__=='__main__':
    valence_from_tweets()