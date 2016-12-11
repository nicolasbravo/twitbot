#!/usr/bin/env python
import sys
import string
import random
from twython import Twython
from array import *

totalWordsGenerator = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
countnGenerator = ['book', 'diary', 'laptop', 'movie', 'remote', 'shoe', 'bookbag', 'paper', 'clock', 'word', 'program', 'sheet', 'exam', 'sock']

totalWords = random.choice(totalWordsGenerator)
wordCounter = 1
wordArray = []
tweetStr = ""

#words = 0

while wordCounter <= totalWords:
        wordGenerator = ['plural countn']
        word = random.choice(wordGenerator)
        if word == 'countn':
                #count noun
                countn = random.choice(countnGenerator)
                wordArray.append(countn)
        elif word == 'plural countn':
                #count noun
                countn = random.choice(countnGenerator)
                #plural count noun
                if countn[-1] == 's' or countn[-1] == 'x' or countn[-1] == 'z' or (countn[-1] == 'h' and countn[-2] == 'c') or (countn[-1] == 'h' and countn[-2] == 's'):
                        pluralCountn = countn + 'es'
                else:
                        pluralCountn = countn + 's'
                wordArray.append(pluralCountn)
        wordCounter = wordCounter + 1
for i in wordArray:
        tweetStr = tweetStr + " " + wordArray[i]
tweetStr = tweetStr[1:]
print(tweetStr)
