#!/usr/bin/env python
import sys
import string
import random
from twython import Twython
from array import *

totalWordsGenerator = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
totalWords = random.choice(totalWordsGenerator)
wordCounter = 1
wordArray = array('l')

words = 0

while wordCounter <= totalWords:
        words = words + 1
        wordArray.append(words)
        wordCounter = wordCounter + 1
tweetStr = str(wordArray[1])
for l in wordArray:
        if l <= totalWords - 1:
                print(wordArray[l + 1])
                #tweetStr = tweetStr + " " + str(wordArray[l + 1])
#print(tweetStr)
