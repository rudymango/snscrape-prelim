'''
William Evans <w.evans@usm.edu>
Script to gather all mentions within a tweet
'''

import pandas as pd
import re

# Read from .csv into dataframe
tweets_df = pd.read_csv("results.csv", usecols=['Tweets'])

# List that tracks mentioned users
mentionedUsers = []

# Searches for mentions in each tweet
for tweets in tweets_df.Tweets:
    mentioned = re.search(r'@\w+', tweets)
    if(mentioned):
        mentionedUsers.append(mentioned.group())

# Dictionary to count the amount of times a user is mentioned within a subset of tweets
my_dict = {i:mentionedUsers.count(i) for i in mentionedUsers}

# Output mentions along with times mentioned
print(my_dict)