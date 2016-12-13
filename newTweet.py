#!/usr/bin/env python
import sys
import string
import random
#from twython import Twython
from array import *

totalWordsGenerator = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
countnGenerator = ['book', 'diary', 'laptop', 'movie', 'remote', 'shoe', 'backpack', 'paper', 'clock', 'word', 'program', 'sheet', 'exam', 'sock', 'phone', 'computer', 'dog', 'day', 'work', 'video', 'life', 'game', 'meme']
verbGenerator = ['make', 'hope', 'have', 'get', 'feel', 'like', 'steal', 'glitch', 'do', 'prosper', 'survive', 'stop', 'go', 'recite', 'tell', 'say', 'play', 'keep', 'crash', 'ruin', 'trust', 'use', 'find', 'leave', 'chill', 'practice', 'finish', 'draw', 'write']
pronounGenerator = ['I', 'you', 'he', 'she']
conjunctionGenerator = ['and', 'but', 'or']
negativeGenerator = ['', ' not']
adjectiveGenerator = ['bad', 'late', 'official', 'happy', 'educational', 'entire', 'random', 'fun', 'stupid', 'serious', 'better', 'pretty', 'boring', 'nice', 'problematic', 'real', 'scary', 'sorry']

totalWords = random.choice(totalWordsGenerator)
wordCounter = 1
wordArray = {1 : '', 2 : '', 3 : '', 4 : '', 5 : '', 6 : '', 7 : '', 8 : '', 9 : '', 10 : '', 11 : '', 12 : '', 13 : '', 14 : '', 15 : '', 16 : '', 17 : '', 18 : '', 19 : '', 20 : ''}
tweetStr = ""
num1 = 0
previous = ""
stopBoolean = False

#words = 0

#while wordCounter <= totalWords:
while stopBoolean == False:
	#count noun or plural noun
	if previous == 'count noun' or previous == 'plural noun':
		wordGenerator = ['regular past tense verb', ',', 'stop', 'verb']
		word = random.choice(wordGenerator)
	#the
	elif previous == 'the':
		wordGenerator = ['count noun', 'plural noun']
		word = random.choice(wordGenerator)
	#verb
	elif (previous == 'verb' or previous == 'regular past tense verb') and len(wordArray) <= (totalWords - 2):
		wordGenerator = ['article noun', 'plural noun', 'the', 'negative', ',', 'pronoun']
		word = random.choice(wordGenerator)
	elif (previous == 'verb' or previous == 'regular past tense verb'):
		wordGenerator = ['plural noun', 'pronoun', 'stop', 'count noun', 'adjective']
		word = random.choice(wordGenerator)
	#comma
	elif previous == ',':
		wordGenerator = ['conjunction', 'pronoun']
		word = random.choice(wordGenerator)
	#conjuction
	elif previous == 'conjunction':
		wordGenerator = ['count noun', 'plural noun', 'verb', 'regular past tense verb', 'pronoun']
		word = random.choice(wordGenerator)
	#pronoun
	elif previous == 'pronoun':
		wordGenerator = ['verb', 'regular past tense verb']
		word = random.choice(wordGenerator)
	#negative
	elif previous == 'negative':
		wordGenerator = ['verb', 'adjective']
		word = random.choice(wordGenerator)
	#article
	elif previous == 'article noun':
		wordGenerator = ['regular past tense verb']
		word = random.choice(wordGenerator)
	#adjective
	elif previous == 'adjective':
		wordGenerator = ['plural noun']
		word = random.choice(wordGenerator)
	#beginning of sentence
	else:
        	wordGenerator = ['plural noun', 'article noun', 'the', 'verb', 'pronoun']
		word = random.choice(wordGenerator)
	#start word generation
        if word == 'count noun':
                #count noun
                countn = random.choice(countnGenerator)
                wordArray[num1] = " " + countn
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
                wordArray[num1] = " " + pluralCountn
	elif word == 'article noun':
		#count noun
		countn = random.choice(countnGenerator)
		#article noun
		if countn[0] == 'a' or countn[0] == 'e' or countn[0] == 'i' or countn[0] == 'o' or countn[0] == 'u':
			articleCountn = 'an ' + countn
		else:
			articleCountn = 'a ' + countn
		wordArray[num1] = " " + articleCountn
	elif word == 'verb':
		#verb
		verb = random.choice(verbGenerator)
		wordArray[num1] = " " + verb
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
		wordArray[num1] = " " + regularPastVerb
	elif word == 'the':
		wordArray[num1] = ' the'
	elif word == ',':
		wordArray[num1] = ','
	elif word == 'pronoun':
		pronoun = random.choice(pronounGenerator)
		wordArray[num1] = " " + pronoun
	elif word == 'conjunction':
		conjunction = random.choice(conjunctionGenerator)
		wordArray[num1] = " " + conjunction
	elif word == 'negative':
		negative = random.choice(negativeGenerator)
		wordArray[num1] = negative
	elif word == 'stop':
		#wordCounter = totalWords + 1
		stopBoolean = True
	elif word == 'adjective':
		adjective = random.choice(adjectiveGenerator)
		wordArray[num1] = " " + adjective
	previous = word
        wordCounter = wordCounter + 1
        num1 = num1 + 1
for s in wordArray:
        tweetStr = tweetStr + wordArray[s]
tweetStr = tweetStr[1:]
print(tweetStr)
print(140 - len(tweetStr))
