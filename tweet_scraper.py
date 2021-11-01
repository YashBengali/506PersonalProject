import tweepy as tp
import csv, json

def scrape(key, secret):
    auth = tp.AppAuthHandler(key,secret)
    api = tp.API(auth, wait_on_rate_limit=True)

    csvFile = open('tweets.csv', 'a')
    csvWriter = csv.writer(csvFile)
    for tweet in tp.Cursor(api.search_tweets, q='$AAPL').items(500000):
        csvWriter.writerow([tweet.created_at,tweet.user.followers_count,tweet.favorite_count,tweet.text.encode('utf-8')])
    csvFile.close()
    print('[*] All Done')

if __name__ == "__main__":
    print('[...] Loading Credentials')
    creds = json.load(open('credentials.json'))
    print('[...] Scraping tweets')
    scrape(creds['key'], creds['secret'])