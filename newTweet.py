#!/usr/bin/env python
import sys
import string
import random
#from twython import Twython
from array import *

totalWordsGenerator = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
ncountnGenerator = ['tennis']
countnGenerator = ['book', 'diary', 'laptop', 'movie', 'remote', 'shoe', 'backpack', 'paper', 'clock', 'word', 'program', 'sheet', 'exam', 'sock', 'phone', 'computer', 'dog', 'day', 'work', 'video', 'life', 'game', 'meme', 'boy', 'number', 'person', 'director', 'firm', 'drill', 'mustache', 'garden', 'fence', 'neighbor', 'outlet', 'table']
nounGenerator = ncountnGenerator + countnGenerator
verbGenerator = ['make', 'hope', 'have', 'get', 'feel', 'like', 'steal', 'glitch', 'do', 'prosper', 'survive', 'stop', 'go', 'recite', 'tell', 'say', 'play', 'keep', 'crash', 'ruin', 'trust', 'use', 'find', 'leave', 'chill', 'practice', 'finish', 'draw', 'write', 'expect', 'spy', 'destroy', 'watch', 'type']
thirdPronounGenerator = ['he', 'she', 'it']
personalPronounGenerator = ['I', 'you', 'we', 'they']
conjunctionGenerator = ['and', 'but', 'or']
negativeGenerator = ['', ' not']
adjectiveGenerator = ['bad', 'late', 'official', 'happy', 'educational', 'entire', 'random', 'fun', 'stupid', 'serious', 'better', 'pretty', 'boring', 'nice', 'problematic', 'real', 'scary', 'sorry', 'normal', 'perfect', 'strange', 'mysterious', 'small', 'large']
verbTense = ""
dependentGenerator = ['when', 'because']

totalWords = random.choice(totalWordsGenerator)
wordCounter = 1
wordArray = {1 : '', 2 : '', 3 : '', 4 : '', 5 : '', 6 : '', 7 : '', 8 : '', 9 : '', 10 : '', 11 : '', 12 : '', 13 : '', 14 : '', 15 : '', 16 : '', 17 : '', 18 : '', 19 : '', 20 : ''}
tweetStr = ""
num1 = 0
previous = ""
stopBoolean = False
nounBoolean = False
verbBoolean = False
commaCounter = 0
periodBoolean = False
#commaTracker = 0
dependentBoolean = False
#words = 0

#while wordCounter <= totalWords:
while stopBoolean == False:
	#simple sentence
	if nounBoolean == True and verbBoolean == True and dependentBoolean == False and conjunctionBoolean == False:
		wordGenerator = ['conjunction', 'stop', 'dependent']
		word = random.choice(wordGenerator)
	elif nounBoolean == True and verbBoolean == True and dependentBoolean == True and conjunctionBoolean == False:
		wordGenerator = ['conjunction', 'stop']
		word = random.choice(wordGenerator)
	elif nounBoolean == True and verbBoolean == True and dependentBoolean == False and conjunctionBoolean == True:
		wordGenerator = ['stop', 'dependent']
		word = random.choice(wordGenerator)
	elif nounBoolean == True and verbBoolean == True and dependentBoolean == True and conjunctionBoolean == True:
		word = 'stop'
	elif previous == 'noun':
		if verbTense == 'regular past tense verb':
			wordGenerator = ['regular past tense verb', 'punctuation']
			word = random.choice(wordGenerator)
		else:
			wordGenerator = ['punctuation', 'third person singular present verb']
			word = random.choice(wordGenerator)
	#count noun
	elif previous == 'count noun':
		if verbTense == 'regular past tense verb':
			wordGenerator = ['regular past tense verb', 'punctuation']
			word = random.choice(wordGenerator)
		else:
			wordGenerator = ['punctuation', 'third person singular present verb']
			word = random.choice(wordGenerator)
	#plural noun
	elif previous == 'plural noun':
		if verbTense == 'regular past tense verb':
			wordGenerator = ['regular past tense verb', 'punctuation']
			word = random.choice(wordGenerator)
		else:
			wordGenerator = ['punctuation', 'verb']
			word = random.choice(wordGenerator)
	#the
	elif previous == 'the':
		wordGenerator = ['count noun', 'plural noun']
		word = random.choice(wordGenerator)
	#verb
	elif (previous == 'verb' or previous == 'regular past tense verb' or previous == 'third person singular present verb') and len(wordArray) <= (totalWords - 2):
		wordGenerator = ['article noun', 'plural noun', 'the', 'negative', 'punctuation', 'third person pronoun']
		word = random.choice(wordGenerator)
	elif (previous == 'verb' or previous == 'regular past tense verb' or previous == 'third person singular present verb'):
		wordGenerator = ['plural noun', 'third person pronoun', 'noun', 'adjective']
		word = random.choice(wordGenerator)
	#comma
	elif previous == 'punctuation':
		wordGenerator = ['conjunction', 'third person pronoun']
		word = random.choice(wordGenerator)
	#conjuction or dependent clause
	elif previous == 'conjunction' or previous == 'dependent':
		if verbTense == 'regular past tense verb':
			wordGenerator = ['noun', 'plural noun', 'regular past tense verb', 'third person pronoun']
			word = random.choice(wordGenerator)
		else:
			wordGenerator = ['noun', 'plural noun', 'verb', 'third person pronoun']
			word = random.choice(wordGenerator)
	#pronoun
	elif previous == 'third person pronoun':
		if verbTense == 'regular past tense verb':
			wordGenerator = ['regular past tense verb']
			word = random.choice(wordGenerator)
		else:
			wordGenerator = ['third person singular present verb']
			word = random.choice(wordGenerator)
	#negative
	elif previous == 'negative':
		if verbTense == 'regular past tense verb':
			wordGenerator = ['regular past tense verb', 'adjective']
			word = random.choice(wordGenerator)
		else:
			wordGenerator = ['verb', 'adjective']
			word = random.choice(wordGenerator)
	#article
	elif previous == 'article noun':
		if verbTense == 'regular past tense verb':
			wordGenerator = ['regular past tense verb']
			word = random.choice(wordGenerator)
		else:
			wordGenerator = ['third person singular present verb']
			word = random.choice(wordGenerator)
	#adjective
	elif previous == 'adjective':
		wordGenerator = ['plural noun', 'noun']
		word = random.choice(wordGenerator)
	#third person singular present verb
	elif previous == 'third person singular present verb':
		wordGenerator = ['plural noun', 'noun']
	elif previous == 'personal pronoun':
		if verbTense == 'regular past tense verb':
			wordGenerator = ['regular past tense verb']
			word = random.choice(wordGenerator)
		else:
			wordGenerator = ['verb']
			word = random.choice(wordGenerator)
	#beginning of sentence
	else:
        	wordGenerator = ['plural noun', 'article noun', 'the', 'verb', 'third person pronoun']
		word = random.choice(wordGenerator)
	#start word generation
        if word == 'noun':
		nounBoolean = True
                #noun
                noun = random.choice(nounGenerator)
                wordArray[num1] = " " + noun
	elif word == 'count noun':
		nounBoolean = True
		#count noun
		countn = random.choice(countnGenerator)
		wordArray[num1] = " " + countn
        elif word == 'plural noun':
		nounBoolean = True
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
		nounBoolean = True
		#count noun
		countn = random.choice(countnGenerator)
		#article noun
		if countn[0] == 'a' or countn[0] == 'e' or countn[0] == 'i' or countn[0] == 'o' or countn[0] == 'u':
			articleCountn = 'an ' + countn
		else:
			articleCountn = 'a ' + countn
		wordArray[num1] = " " + articleCountn
	elif word == 'verb':
		verbBoolean = True
		#verb
		verb = random.choice(verbGenerator)
		wordArray[num1] = " " + verb
		verbTense = 'verb'
	elif word == 'regular past tense verb':
		verbBoolean = True
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
		verbTense = 'regular past tense verb'
	elif word == 'the':
		wordArray[num1] = ' the'
	elif word == 'punctuation':
		for x in wordArray:
			if wordArray[x] == '.':
				periodBoolean = True
		if periodBoolean == True:
			stopBoolean = True
		else:
			wordArray[num1] = '.'
	elif word == 'third person pronoun':
		nounBoolean = True
		thirdPronoun = random.choice(thirdPronounGenerator)
		wordArray[num1] = " " + thirdPronoun
	elif word == 'conjunction':
		nounBoolean = False
		verbBoolean = False
		#num2 = num1 - 1
		#for x in wordArray:
		#	if wordArray[x] == ',':
		#		commaCounter = commaCounter + 1
		#	if commaCounter < 2:
		#		wordArray[num2] = ","
		#	else:
		#		wordArray[num2] = "."
		conjunction = random.choice(conjunctionGenerator)
		wordArray[num1] = " " + conjunction
	elif word == 'dependent':
		nounBoolean = False
		verbBoolean = False
		dependentBoolean = True
		dependent = random.choice(dependentGenerator)
		wordArray[num1] = " " + dependent
	elif word == 'negative':
		negative = random.choice(negativeGenerator)
		wordArray[num1] = negative
	elif word == 'stop':
		#wordCounter = totalWords + 1
		stopBoolean = True
	elif word == 'adjective':
		adjective = random.choice(adjectiveGenerator)
		wordArray[num1] = " " + adjective
	elif word == 'third person singular present verb':
		verbBoolean = True
		#verb
		verb = random.choice(verbGenerator)
		#third person singular present verb
		if ((verb[-1] == 's' and verb[-2] == 's') or (verb[-1] == 'z' and verb[-2] == 'z') or (verb[-1] == 'h' and verb[-2] == 's') or (verb[-1] == 'i' and verb[-2] == 's') or (verb[-1] == 'h' and verb[-2] == 'c') or verb[-1] == 'j') or (verb[-1] == 'o' and verb[-2] != 'a' and verb[-2] != 'e' and verb[-2] != 'i' and verb[-2] != 'o' and verb[-2] != 'u'):
			thirdPresentVerb = verb + 'es'
		elif verb[-1] == 'y' and verb[-2] != 'a' and verb[-2] != 'e' and verb[-2] != 'i' and verb[-2] != 'o' and verb[-2] != 'u':
			thirdPresentVerb = verb[:-1] + 'ies'
		else:
			thirdPresentVerb = verb + 's'
		previous = 'third person singular present verb'
		wordArray[num1] = " " + thirdPresentVerb
	elif word == 'personal pronoun':
		nounBoolean = True
		personalPronoun = random.choice(personalPronounGenerator)
		wordArray[num1] = " " + personalPronoun
	previous = word
        wordCounter = wordCounter + 1
        num1 = num1 + 1
#for n in wordArray:
#	if wordArray[n] == ','
#		nTracker = n
#		commaTracker = commaTracker + 1
#if commaTracker == 1:
#	nplusone = nTracker + 1
#	if wordArray[nplusone] == 'and' or wordArray[nplusone] == 'or' or wordArray[nplusone] == 'but':
#		wordArray[nTracker] = ''
for s in wordArray:
        tweetStr = tweetStr + wordArray[s]
tweetStr = tweetStr[1:]
while len(tweetStr) > 140:
	space = tweetStr.rfind(" ")
	tweetStr = tweetStr[:space]
print(tweetStr)
print(140 - len(tweetStr))
