import snscrape.modules.twitter as sntwitter
import pandas as pd

# Created a list to append all tweet attributes(data)
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('groomer -is:retweet').get_items()):
    if i > 10:
        break
    attributes_container.append([tweet.date, tweet.id, tweet.likeCount, tweet.sourceLabel, tweet.rawContent])

# Create a dataframe from the tweets list above
tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "ID", "Number of Likes", "Source of Tweet", "Tweets"])

tweets_df.to_csv("results.csv")


