from functools import *
import math

import json

with open("tweets.json", "r") as tweet_db:
    tweets = json.load(tweet_db)

def flatten(xs):
    return list(reduce(lambda x, y: x+y, xs, []))

#print(flatten([[1,2],[],[3,4]]))

def difference(xs, ys):
    return list(filter(lambda x: x not in ys, xs)) + list(filter(lambda x: x not in xs, ys))

#print(difference([1, 2], [2, 3]) )

def to_text(tweets):
    return list((map(lambda x: x["content"], tweets)))

#tweet1 = {"cotent": "This is a tweet!", "conte": "Hey", "content": ""}
#tweet2 = {"content": "This is, too.", "HUL": "HUHUHU"}
#tweet3 = {"content": "More tweets!"}
#tweets = [tweet1, tweet2, tweet3]

#print(to_text(tweets))

def to_lowercase(tweets):
    return list((map(lambda y, x: {**y, **{"content": x["content"].lower()}}, tweets, tweets)))

#print(to_lowercase(tweets))
#print(to_text(to_lowercase(tweets)))

def nonempty(tweets):
    return list(filter(lambda x: x["content"] is not "", tweets))

#print(nonempty(tweets))
#tweet11 = {"content": "This is a tweet.", "duck": "lll"}
#tweet22 = {"content": ""}
#tweet33 = {"content": "This is also a tweet."}
#tweets0 = [tweet11, tweet22, tweet33]
#print(to_text(nonempty(tweets0)))


def total_word_count(tweets):
    l_one = list(map(lambda x: (x["content"]).split(), tweets))
    l_two = list(reduce(lambda x, y: x+y, l_one))
    return len(l_two)
#print(total_word_count(tweets))
#tweet10 = {"content": "This is a tweet."}
#tweet20 = {"content": "Twitter is so cool."}
#tweet30 = {"content": "We can use words."}
#tweets00 = [tweet10, tweet20, tweet30]
#print(total_word_count(tweets00))
#**
def hashtags(tweet):
    l_one = list(tweet["content"].split())
    return list(filter(lambda x: x[0] is "#", l_one))

#tweetHH = {"content": "Hello, America. #MAGA #Trump2016"}

#print(hashtags(tweetHH))
#*********    for # and @ only check the beginning
#**
def mentions(tweet):
    l_one = list(tweet["content"].split())
    return list(filter(lambda x: x[0] is "@", l_one))

#tweetM = {"content": "@mike_pence and I are very happy to be here."}
#print(mentions(tweetM))

# ******************** Counting Problems **************** #

def all_hashtags(tweets):
    lst = list(map(lambda x: (hashtags(x)), tweets))
    return flatten(lst)

#tweet1C = {"content": "Hello, America. #MAGA #Trump2016"}
#tweet2C = {"content": "Iran, you’re on notice!!!! Let’s #MAGA"}
#tweet3C = {"content": "No hashtags in here."}
#tweetsC = [tweet1C, tweet2C, tweet3C]
#print(all_hashtags(tweetsC))

def all_mentions(tweets):
    return flatten(list(map(lambda x: mentions(x), tweets)))

#tweet1AM = {"content": "@michellemalkin You were born stupid!"}
#tweet2AM = {"content": "The Emmys are sooooo boring!"}
#tweet3AM = {"content": "@azizansari deserved the Emmy!"}
#tweetsAM = [tweet1AM, tweet2AM, tweet3AM]
#print(all_mentions(tweetsAM))

def all_caps_tweets(tweets):
    return list(filter(lambda x: x["content"].isupper() is True, tweets))

#tweet1AT = {"content": "MAKE AMERICA SAFE AGAIN!"}
#tweet2AT = {"content": "The Emmys are soooo boring!"}
#tweet3AT = {"content": "SEE YOU IN COURT!!"}
#tweetsAT = [tweet1AT, tweet2AT, tweet3AT]
#print(all_caps_tweets(tweetsAT))
#print(to_text(all_caps_tweets(tweetsAT)))

#***
def count_individual_words(tweets):
    d = {}
    l_one = list(map(lambda x: list(x["content"].split()), tweets))
    l_two = list(reduce(lambda x, y: x + y, l_one))
    l_four = list(map(lambda x: {x:l_two.count(x)}, l_two))
    d = reduce(lambda x, y: {**x, **y}, l_four, {})
    return d

#tweet1IW = {"content": "MAKE AMERICA SAFE AGAIN!"}
#tweet2IW = {"content": "america"}
#tweet3IW = {"content": "AMERICA FIRST!"}
#tweetsIW = [tweet1IW, tweet2IW, tweet3IW]
#print(count_individual_words(tweetsIW))

def count_individual_hashtags(tweets):
    lst = flatten(list(map(lambda x: hashtags(x), tweets)))
    l_four = list(map(lambda x: {x: lst.count(x)}, lst))
    return dict(reduce(lambda x, y: {**x, **y}, l_four, {}))

#tweet1IH = {"content": "#MAGA #MAGA #Trump2016"}
#tweet2IH = {"content": "#MakeAmericaGreatAgain  #maga"}
#tweet3IH = {"content": "No hashtags in here."}
#tweetsIH = [tweet1IH, tweet2IH, tweet3IH]
#print(count_individual_hashtags(tweetsIH))

def count_individual_mentions(tweets):
    lst = flatten(list(map(lambda x: mentions(x), tweets)))
    l_four = list(map(lambda x: {x: lst.count(x)}, lst))
    return dict(reduce(lambda x, y: {**x, **y}, l_four, {}))

#tweet1CM = {"content": "I am so impressed with @azizansari"}
#tweet2CM = {"content": "@TheEmmys are sooooo boring!"}
#tweet3CM = {"content": "@azizansari deserved the Emmy!"}
#tweetsCM = [tweet1CM, tweet2CM, tweet3CM]
#print(count_individual_mentions(tweetsCM))

def n_most_common(n, word_count):
    lst = list(sorted(word_count.items(), key=lambda x: (-x[1], x)))
    lst2 = lst[0:n]
    return lst2

#tweet1NC = {"content": "MAKE AMERICA SAFE AGAIN!"}
#tweet2NC = {"content": "america"}
#tweet3NC = {"content": "AMERICA FIRST!"}
#tweetsNC = [tweet1NC, tweet2NC, tweet3NC]
#print(n_most_common(1, count_individual_words(tweetsNC)))

def iphone_tweets(tweets):
    return list(filter(lambda x: "iPhone" in x["source"], tweets))


#tweet1IP = {"content": "Thanks, America", "source": "Twitter for iPhone"}
#tweet2IP = {"content": "SEE YOU IN COURT!!", "source": "Twitter for Android"}
#tweet3IP = {"content": "#MAGA", "source": "Twitter for iPhone"}
#tweetsIP = [tweet1IP, tweet2IP, tweet3IP]
#print(to_text(iphone_tweets(tweetsIP)))

def android_tweets(tweets):
    return list(filter(lambda x: "Android" in x["source"], tweets))

#tweet1AN = {"content": "Thanks, America", "source": "Twitter for iPhone"}
#tweet2AN = {"content": "SEE YOU IN COURT!!", "source": "Twitter for Android"}
#tweet3AN = {"content": "#MAGA", "source": "Twitter for iPhone"}
#tweetsAN = [tweet1AN, tweet2AN, tweet3AN]
#print(to_text(android_tweets(tweetsAN)))

def average_favorites(tweets):
   num = reduce(lambda x, y: x+y, list(map(lambda x: x["favorites"], tweets)), 0)
   return int(round(num/(len(tweets))))

#tweet1AVF = {"favorites": 32}
#tweet2AVF = {"favorites": 8}
#tweet3AVF = {"favorites": 16}
#tweetsAVF = [tweet1AVF, tweet2AVF, tweet3AVF]
#print(average_favorites(tweetsAVF))

def average_retweets(tweets):
    num = reduce(lambda x, y: x + y, list(map(lambda x: x["retweets"], tweets)), 0)
    return int(round(num / (len(tweets))))

#tweet1RE = {"retweets": 32}
#tweet2RE = {"retweets": 80}
#tweet3RE = {"retweets": 16}
#tweetsRE = [tweet1RE, tweet2RE, tweet3RE]
#print(average_retweets(tweetsRE))

def sort_by_favorites(tweets):
    return sorted(tweets, key=lambda x: x["favorites"])

#tweet1SF = {"favorites": 32, "content": 0}
#tweet2SF = {"favorites": 8}
#tweet3SF = {"favorites": 16}
#tweetsSF = [tweet1SF, tweet2SF, tweet3SF]
#print(sort_by_favorites(tweetsSF))

def sort_by_retweets(tweets):
    return list(sorted(tweets, key=lambda x: x["retweets"]))

#tweet1RET = {"retweets": 32}
#tweet2RET = {"retweets": 8}
#tweet3RET = {"retweets": 16}
#tweetsRET = [tweet1RET, tweet2RET, tweet3RET]
#print(sort_by_retweets(tweetsRET))

def upper_quartile(tweets):
    num = int(math.ceil(0.75 * len(tweets)))
    return tweets[num-1]

#tweet1UQ = {"favorites": 32}
#tweet2UQ = {"favorites": 8}
#tweet3UQ = {"favorites": 16}
#tweet4UQ = {"favorites": 19}
#tweet5UQ = {"favorites": 44}
#tweetsUQ = [tweet1UQ, tweet2UQ, tweet3UQ, tweet4UQ, tweet5UQ]
#print(upper_quartile(sort_by_favorites(tweetsUQ)))

def lower_quartile(tweets):
    num = int(math.ceil(0.25 * len(tweets)))
    return tweets[num - 1]

#tweet1LQ = {"retweets": 32}
#tweet2LQ = {"retweets": 8}
#tweet3LQ = {"retweets": 16}
#tweet4LQ = {"retweets": 19}
#tweet5LQ = {"retweets": 44}
#tweetsLQ = [tweet1LQ, tweet2LQ, tweet3LQ, tweet4LQ, tweet5LQ]
#print(lower_quartile(sort_by_retweets(tweetsLQ)))

def top_quarter_by(tweets, factor):
    lst = upper_quartile(tweets)
    num = lst[factor]
    return list(filter(lambda x: x[factor] >= num, tweets))

#tweet1TQ = {"retweets": 32}
#tweet2TQ = {"retweets": 8}
#tweet3TQ = {"retweets": 16}
#tweet4TQ = {"retweets": 19}
#tweet5TQ = {"retweets": 44}
#tweetsTQ = [tweet1TQ, tweet2TQ, tweet3TQ, tweet4TQ, tweet5TQ]
#print(top_quarter_by(sort_by_retweets(tweetsTQ), "retweets"))

def bottom_quarter_by(tweets, factor):
    lst = lower_quartile(tweets)
    num = lst[factor]
    return list(filter(lambda x: x[factor] <= num, tweets))

#tweet1BQ = {"favorites": 32}
#tweet2BQ = {"favorites": 8}
#tweet3BQ = {"favorites": 16}
#tweet4BQ = {"favorites": 19}
#tweet5BQ = {"favorites": 44}
#tweetsBQ = [tweet1BQ, tweet2BQ, tweet3BQ, tweet4BQ, tweet5BQ]
#print(bottom_quarter_by(sort_by_favorites(tweetsBQ), "favorites"))
