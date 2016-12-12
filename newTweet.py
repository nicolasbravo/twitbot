#!/usr/bin/env python
import sys
import string
import random
from twython import Twython
from array import *

totalWordsGenerator = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
countnGenerator = ['book', 'diary', 'laptop', 'movie', 'remote', 'shoe', 'backpack', 'paper', 'clock', 'word', 'program', 'sheet', 'exam', 'sock']
verbGenerator = ['make', 'hope', 'have', 'get', 'feel', 'like', 'steal', 'glitch', 'do', 'prosper', 'survive', 'stop', 'go', 'recite', 'tell', 'say', 'play', 'keep', 'crash', 'ruin', 'trust', 'use', 'find', 'leave', 'chill', 'practice', 'finish', 'draw', 'write']

totalWords = random.choice(totalWordsGenerator)
wordCounter = 1
wordArray = {1 : '', 2 : '', 3 : '', 4 : '', 5 : '', 6 : '', 7 : '', 8 : '', 9 : '', 10 : '', 11 : '', 12 : '', 13 : '', 14 : '', 15 : '', 16 : '', 17 : '', 18 : '', 19 : '', 20 : ''}
tweetStr = ""
num1 = 0

#words = 0

while wordCounter <= totalWords:
        wordGenerator = ['count noun', 'plural noun', 'article noun', 'regular past tense verb']
        word = random.choice(wordGenerator)
        if word == 'count noun':
                #count noun
                countn = random.choice(countnGenerator)
                #wordArray.append(countn)
                wordArray[num1] = countn
        elif word == 'plural noun':
                #count noun
                countn = random.choice(countnGenerator)
                #plural count noun
                if countn[-1] == 's' or countn[-1] == 'x' or countn[-1] == 'z' or (countn[-1] == 'h' and countn[-2] == 'c') or (countn[-1] == 'h' and countn[-2] == 's'):
                        pluralCountn = countn + 'es'
                elif countn[-1] == 'y' and countn[-2] != 'a' and countn[-2] != 'e' and countn[-2] != 'i' and countn[-2] != 'o' and countn[-2] != 'u':
                        pluralCountn = countn[:-1] + 'ies'
                elif countn[-1] == 'f' and ((countn[-2] == 'l' and countn[-3] == 'a') or (countn[-2] == 'l' and countn[-3] == 'e') or (countn[-2] == 'a' and countn[-3] == 'e')):
                        pluralCountn = countn[:-1] + 'ves'
                elif countn[-1] == 'e' and countn[-2] == 'f' and countn[-3] == 'i':
                        pluralCountn = countn[:-2] + 'ves'
                elif countn[-1] == 's' and countn[-2] == 'u':
                        pluralCountn = countn[:-2] + 'i'
                elif countn[-1] == 's' and countn[-2] == 'i':
                        pluralCountn = countn[:-2] + 'es'
                elif countn[-1] == 'x' and (countn[-2] == 'i' or countn[-2] == 'e'):
                        pluralCountn = countn[:-2] + 'ices'
                elif countn[-1] == 'u' and countn[-2] == 'a' and countn[-3] == 'e':
                        pluralCountn = countn + 'x'
                elif (countn[-1] == 'm' and countn[-2] == 'u') or (countn[-1] == 'n' and countn[-2] == 'o') and countn != 'person':
                        pluralCountn = countn[:-2] + 'a'
                elif countn == 'person':
                        pluralCountn = 'people'
                elif countn[1] == 'o' and countn[2] == 'o' and countn != 'book':
                        pluralCountn = countn.replace('o', 'e', 2)
                elif countn[-1] == 'a':
                        pluralCountn = countn + 'e'
                elif countn[-1] == 'e' and countn[-2] == 's' and countn[-3] == 'u' and countn[-4] == 'o':
                        pluralCountn = countn[:-4] + 'ice'
                else:
                        pluralCountn = countn + 's'
                wordArray[num1] = pluralCountn
	elif word == 'article noun':
		#count noun
		countn = random.choice(countnGenerator)
		#article noun
		if countn[0] == 'a' or countn[0] == 'e' or countn[0] == 'i' or countn[0] == 'o' or countn[0] == 'u':
			articleCountn = 'an ' + countn
		else:
			articleCountn = 'a ' + countn
		wordArray[num1] = articleCountn
	elif word == 'regular past tense verb':
		#verb
		verb = random.choice(verbGenerator)
		#regular past tense verb
		if verb[-1] == 'e':
			regularPastVerb = verb + 'd'
		elif verb[-1] == 'y' and verb[-2] != 'a' and verb[-2] != 'e' and verb[-2] != 'i' and verb[-2] != 'o' and verb[-2] != 'u':
			regularPastVerb = verb[:-1] + 'ed'
		#rule 5
		#rule 7
		#rule 8
		else:
			regularPastVerb = verb + 'ed'
		wordArray[num1] = regularPastVerb
        wordCounter = wordCounter + 1
        num1 = num1 + 1
for s in wordArray:
        tweetStr = tweetStr + " " + wordArray[s]
tweetStr = tweetStr[1:]
print(tweetStr)
print(140 - len(tweetStr))
