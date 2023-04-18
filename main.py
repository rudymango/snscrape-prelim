import snscrape.modules.twitter as sntwitter
import pandas as pd

MAX_TWEETS = 1000

attributes_container = []

for i, tweet in enumerate(sntwitter.TwitterSearchScraper('groomer -is:retweet').get_items()):
    if i > MAX_TWEETS:
        break
    if i % 10 == 0:
        print("{}%"i/MAX_TWEETS)
    attributes_container.append([tweet.date, tweet.id, tweet.likeCount, tweet.sourceLabel, tweet.rawContent])

tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "ID", "Number of Likes", "Source of Tweet", "Tweets"])

tweets_df.to_csv("results.csv")