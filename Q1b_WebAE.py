# Q1b
__author__ = 'Ming Ho Wu'

'''
Aim: To run the mongo server

First, 
Go to cmd with the administrator mode 
Type the word: mongo 

'''

# Aim: Collecting Imports

from pymongo import MongoClient
import tweepy
import json
import time
import logging
# Aim: Connect MongoDB and PyCharm via a Twitter Account
# Be sure to first create a developer account
# I lost the method to do it, but there should be examples on YouTube

# You can find the following data in your Twitter Account
access_token = "1237038999522422785-Vt2Pehfi7HDArLyuS3lZLYFZ4cmPfc"
access_token_secret = "oVQ9PaVBzfgE39CyYiSreJOylxNPeSNcFOxxvDwywUipe"
consumer_key = "QytLwqIh9JHa3R1udsxatBGlF"
consumer_secret = "MYG7dzgYsnNoF0ixyVH8qM4PdfgIdhdP3X6SoVBHrMDVSqrSma"

# Reference for auth setup:
# https://stackoverflow.com/questions/22469713/managing-tweepy-api-search

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

client = MongoClient()
db = client["Q1b_DB"]
collection = db["Q1b_Collection"]

q = ['Technology']


print("Crawling begins.........")
# Aim: Start Twitter Crawling Process

# It is estimated the program will retrieve about 20 tweets in 10 seconds
# By calculation, we can conclude that in 2 hours, it will find 14400 records
# Let the number of tweet to retrieve is 15000.

# Note that if the text is over 140 character,
# it will be shortened to only 140 characters.
# To find the full text,
# go to retweeted_status then full_text.
# If the text is not over 140 characters,
# the retweeted_status heading will not exist.
duplication_check = []
error_list = []
timeout = time.time() + 60 * 60 * 2
while time.time() < timeout:
    try:
        results_n10 = api.search(q=q, count=100, tweet_mode='extended')
    except Exception as e:
        print("error is occuring")
        timeout += 60 * 20
        error_list.append("0")
        time.sleep(60 * 20)
        logging.exception(e)
        continue
    # count = 100 is the maximum number of tweet per request set in the program

    for i in results_n10:
        # print("Start: ------------- ith in results_n10 data")
        # print(json.loads(json.dumps(i._json)))
        results_n1 = json.loads(json.dumps(i._json))
        # print(results_n1['id'])
        if results_n1['id'] not in duplication_check:
            duplication_check.append(results_n1['id'])
            collection.insert_one(results_n1)
            print(results_n1)
print(error_list)
# print(duplication_check)
# print("End:------------- ith in results_n10 data")

# print("End: -------------- end for every 10th result")

# Aim: The following code is just for the purpose of having a backup
# of tried implementation

import twitter
from pprint import pprint
from twitter.archiver import statuses
# auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
# db = client.tweet_db123456789

# tweet_collection = db.tweet_collection
# tweet_collection.create_index([("id", pymongo.ASCENDING)], unique=True)

# Set Query


# class MyStreamListener(tweepy.StreamListener):
#
#     def on_status(self, status):
#         print(json.loads(json.dumps(status._json)))
#         return json.loads(json.dumps(status._json))
#
#     def on_error(self, status_code):
#         if status_code == 420:
#             # returning False in on_error disconnects the stream
#             return False
#
#             # returning non-False reconnects the stream, with backoff.
# Searching Results


# pprint(search_results['search_metadata'])

# Printing search results

# print(search_results)
# document_results = search_results[0]
# print(document_results)
# print(document_results._json)
# import pprint
# pprint.pprint(document_results._json)
# dir(document_results)
# document_results.id
# print(document_results.id)
# document_results.text
# print(document_results.text)
# document_results.created_at
# print(document_results.created_at)
# document_results.retweet
# print(document_results.retweet)

# import time
# timeout = time.time() + 60*600
#
# while True:
#
#     if time.time() > timeout:
#         break
#
#     search_results = api.search(count=count, q=q)
#
#     for statues in search_results:
#         print("ABC-----------------------------------")
#         print(statues.id)
#         print(statues.text)
#         print(statues.created_at)
#         print("********")
#         resultsdict = {"id": statues.id, "text": statues.text, "created_at": statues.created_at}
#         tweet_collection.insert_one(resultsdict)
#         print("1...........")
# print("xxxxxxxxxxxxxxxxxx")
# tweet_collection.estimated_document_count()
# tweet_cursor = tweet_collection.find()
#     #print(tweet_cursor)
#     #dir(tweet_cursor)
#     #print(tweet_cursor.clone)
#
# for r in tweet_cursor:
#     print(r)

# %%
