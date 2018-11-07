# Copyright (c) 2015–2016 Molly White
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
import tweepy
from secrets import *
from time import gmtime, strftime
import random



# ====== Individual bot configuration ==========================
bot_username = 'MayITakeYourOrder'
logfile_name = bot_username + ".log"

# ==============================================================

size=""
prefix=""
drinkType=""
sugar=""
extra=""

sizeList=['small','medium','large','tiny','uh ummmm medium, no a small','errr hmm a large, no a medium']
prefixList=['double shot','triple shot','quad shot','almond milk','extra whipped cream','soy milk','coconut milk','goat milk', 'heavy cream','decaf','iced']
drinkTypeList=['latte','macchiato','mocha','white mocha','pumpkin spice latte','caramel frappuccino','mocah frappuccino','chai latte','peppermint mocha','coffee' ]
sugarList=["no sugar", 'two pumps of sugar', 'three pumps of sugar', 'four pumps of sugar', 'ten pumps of sugar', 'caramel syrup','some mocha','with honey'\
           'with sugar free sugar','sugar free vanilla','some whisky','a dab of rum','angel tears']
extraList=['while I leave and forget I ordered a drink',' and then I will look confused at what you make me','with a dirty look','and then I will take someone elses drink'\
           'in my keep cup','in someone else keep cup','but tell me its a blueberry muffin',',but forget to make it','but ignore what I say','while I complain how slow you are'\
           'while you look like you are having an existential crisis','but spill it all over yourself','but let me spill it all over myself','but let me spill it all over the floor'\
           'while I give you a dirty look','while you give me a dirty look']
def MakeSize():
<<<<<<< Updated upstream
    size=random.randint(0,len(sizeList))
    
=======
    size=random.choice(sizeList)
    #size=sizeList[size]
>>>>>>> Stashed changes
    return size

def MakePrefix():
    prefix=random.choice(prefixList)
<<<<<<< Updated upstream
    
=======
    #prefix=prefixList[prefix]
>>>>>>> Stashed changes
    return prefix

def MakeDrinkType():
    drinkType=random.choice(drinkTypeList)
<<<<<<< Updated upstream
    
=======
    #drinkType=drinkTypeList[drinkType]
>>>>>>> Stashed changes
    return drinkType


def MakeExtra():
    extra=random.choice(extraList)
<<<<<<< Updated upstream
    
=======
    #extra=extraList[extra]
>>>>>>> Stashed changes
    return extra

def MakeSugar():
    sugar=random.choice(sugarList)
<<<<<<< Updated upstream
    
=======
    #sugar=sugarList[sugar]
>>>>>>> Stashed changes
    return sugar

def create_tweet():
    """Create the text of the tweet you want to send."""
    # Replace this with your code!
    extra=MakeExtra()
    sugar=MakeSugar()
    drinkType=MakeDrinkType()
    prefix=MakePrefix()
    size=MakeSize()
    text=""
    myTweet = "I want a %s, %s,%s with %s %s." % (size,prefix,drinkType,sugar,extra)
    text=myTweet
    return text

def tweet(text):
    """Send out the text as a tweet."""
    # Twitter authentication
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)
    message="there was an error"
    # Send the tweet and log success or failure
    try:
        api.update_status(text)
    except tweepy.error.TweepError as e:
        log(e.message)
    else:
        log("Tweeted: " + text)


def log(message):
    """Log message to logfile."""
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, logfile_name), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " " + message)


if __name__ == "__main__":
    tweet_text = create_tweet()
    tweet(tweet_text)
