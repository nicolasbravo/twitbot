#!/usr/bin/env python
import sys
import string
import random
from twython import Twython

#noun
nouns = ['a bot', 'a tweet', 'a person', 'a day', 'work', 'physics', 'a video', 'life', 'a game', 'an app', 'fanfiction', 'an account', 'stuff', 'art', 'a skill', 'a meme', 'sound', 'a corgi', 'a cyborg', 'a post', 'a conspiracy theory']
randomNoun = random.choice(nouns)
randomNoun2 = random.choice(nouns)
#plural noun
pluralNouns = ['corgis', 'bots', 'tweets', 'people', 'days', 'videos', 'lives', 'games', 'apps', 'accounts', 'cyborgs', 'skills', 'memes', 'posts', 'conspiracy theories']
randomPluralNoun = random.choice(pluralNouns)
#proper noun
properNouns = ['Pokemon GO', 'Overwatch', 'Tumblr', 'Timo', 'Wii', 'X-Files', 'the Illuminati', 'Alien', 'Outlast', 'Mountain', 'iPhone 7']
randomProperNoun = random.choice(properNouns)
#all singular nouns
allNouns = ['a bot', 'a tweet', 'a person', 'a day', 'work', 'physics', 'a video', 'life', 'a game', 'an app', 'fanfiction', 'an account', 'stuff', 'art', 'a skill', 'a meme', 'sound', 'a corgi', 'a cyborg', 'a post', 'Pokemon GO', 'Timo', 'Wii', 'a conspiracy theory', 'the Illuminati', 'X-Files', 'Alien', 'Outlast', 'Mountain', 'iPhone 7']
randomAllNoun = random.choice(allNouns)
randomAllNoun2 = random.choice(allNouns)

#verb
verbs = ['make', 'hope', 'have', 'get', 'feel', 'like', 'steal', 'glitch', 'do', 'prosper', 'survive', 'stop', 'go', 'recite', 'tell', 'say', 'play', 'keep', 'crash', 'ruin', 'trust', 'use', 'find', 'leave', 'chill', 'practice', 'finish', 'draw', 'write']
randomVerb = random.choice(verbs)
randomVerb2 = random.choice(verbs)
randomVerb3 = random.choice(verbs)
#past tense
pastVerbs = ['made', 'hoped', 'had', 'got', 'felt', 'liked', 'stole', 'glitched', 'did', 'prospered', 'survived', 'stopped', 'went', 'recited', 'told', 'said', 'played', 'kept', 'crashed', 'ruined', 'trusted', 'used', 'found', 'left', 'practiced', 'finished', 'drew', 'wrote']
randomPastVerb = random.choice(pastVerbs)

#adjective
adjectives = ['bad', 'late', 'official', 'happy', 'educational', 'entire', 'random', 'fun', 'stupid', 'serious', 'better', 'pretty', 'boring', 'nice', 'problematic', 'real', 'scary', 'sorry']
randomAdjective = random.choice(adjectives)

#adverb (add later)

#negative
nots = [' not ', ' ']
randomNot = random.choice(nots)

#sentence
sentences = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
randomSentence = random.choice(sentences)

#perspective
perspectives = ['I', 'you']
randomPerspective = random.choice(perspectives)

#tweet contents
if randomSentence == '1':
	tweetStr = randomPerspective + " " + randomVerb + " " + randomAdjective + " " + randomNoun
elif randomSentence == '2':
	tweetStr = "why does " + randomNoun + randomNot + randomVerb + "? Because it is " + randomAdjective
elif randomSentence == '3':
	tweetStr = "why do " + randomPluralNoun + randomNot + randomVerb + "? Because they are " + randomAdjective
elif randomSentence == '4':
	tweetStr = randomAllNoun +  " is" + randomNot + randomAdjective
elif randomSentence == '5':
	tweetStr = randomPerspective + " " + randomPastVerb + " " + randomNoun
elif randomSentence == '6':
	tweetStr = randomPluralNoun + " are" + randomNot + randomAdjective
elif randomSentence == '7':
	tweetStr = "you should" + randomNot + randomVerb + ". It is " + randomAdjective
elif randomSentence == '8':
	tweetStr = "what do you " + randomVerb + "?"
elif randomSentence == '9':
	tweetStr = randomPerspective + " should" + randomNot + randomVerb + " " + randomPluralNoun
elif randomSentence == '10':
	tweetStr = randomAllNoun + " " + randomPastVerb + " " + randomAllNoun2
elif randomSentence == '11':
	tweetStr = randomPluralNoun + " out for " + randomProperNoun
elif randomSentence == '12':
	tweetStr = randomProperNoun + ", do you " + randomVerb
elif randomSentence == '13':
	tweetStr = "do you even " + randomVerb
elif randomSentence == '14':
	tweetStr = "I'm" + randomNot + randomAdjective
elif randomSentence == '15':
	tweetStr = "you're" + randomNot  + randomAdjective
elif randomSentence == '16':
	tweetStr = randomPerspective + " need to " + randomVerb
elif randomSentence == '17':
	tweetStr = "what did " + randomPerspective + " " + randomPastVerb
elif randomSentence == '18':
	tweetStr = randomVerb + " " + randomPluralNoun
elif randomSentence == '19':
	tweetStr = "how to " + randomVerb + ": first you " + randomVerb2 + " " + randomAllNoun + ", and then you " + randomVerb3
elif randomSentence == '20':
	tweetStr = randomProperNoun + " was an inside job"

#twitter consumer access information
apiKey = 'yCZyGii87mEIsbp202QV25N7h'
apiSecret = 'rkZDXBny5UgguitHL4KmqJgrFClWjvDZ5GdaZwxOguDlC5S4wp'
accessToken = '766349989513748480-DrNZ0ZBjENZ110GPCDu9iMRnCnb1Q7t'
accessTokenSecret = 'W78BvPSHdwYMbBEhUppnIJWsNrMIKMALTUCGwcNX6q7hC'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.update_status(status=tweetStr)
