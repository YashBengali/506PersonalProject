import csv, json

def scrape(key, secret):
    # Using twitter API limits us to tweets in past week
    import tweepy as tp

    auth = tp.AppAuthHandler(key,secret)
    api = tp.API(auth, wait_on_rate_limit=True)

    csvFile = open('tweets.csv', 'a')
    csvWriter = csv.writer(csvFile)
    for tweet in tp.Cursor(api.search_tweets, q='$AAPL').items(500000):
        csvWriter.writerow([tweet.created_at,tweet.user.followers_count,tweet.favorite_count,tweet.text.encode('utf-8')])
    csvFile.close()
    print('[*] All Done')

def removeDups():
    csvFile = open("tweets.csv", "r")
    lines = csvFile.read().split("\n")
    csvFile.close()
    
    noDupsCSV = open("tweets.csv", "w")
    for line in set(lines):
        noDupsCSV.write(line + "\n")
    noDupsCSV.close()

# def scrape():
#     csvFile = open('tweets.csv', 'w')
#     csvWriter = csv.writer(csvFile)
#     csvWriter.writerow(['USERNAME','LINK TO TWEET', 'IS RETWEET', 'TIME', 'TEXT', 'LIKES', 'RETWEETS'])
#     from twitter_scraper import get_tweets
#     for tweet in get_tweets('AAPL', pages=30):
#         csvWriter.writerow([tweet['username'],tweet['tweetUrl'],tweet['isRetweet'],tweet['time'],tweet['text'],tweet['likes'],tweet['retweets']])
#     csvFile.close()
#     print('[*] All Done')

if __name__ == "__main__":
    # print('[...] Loading Credentials')
    # creds = json.load(open('credentials.json'))
    # scrape(creds['key'], creds['secret'])
    removeDups()
