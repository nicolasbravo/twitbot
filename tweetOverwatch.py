#!/usr/bin/env python
import sys
import string
import random
from twython import Twython

#noun
nouns = ["Justice", "Child", "Pain", "Mother", "Scope", "Challenger", "Bad Guy", "Hack", "Blade", "Challenge", "Balance", "Human", "Water", "Thing", "Distraction", "Moment", "Dragon", "Dojo", "Barbecue", "Birthday", "Day", "Rhythm", "Champion", "World", "Noise", "Huckleberry", "Bullet", "Name", "Sky", "Lesson", "Obstacle", "Eye", "Consultation Fee", "Doctor", "Miracle", "Opinion", "Cake", "Hand", "Sky", "Radar", "Professional", "Break", "Man", "Refrigerator", "Psychopath", "Ghost", "Dog", "Apocalypse", "Candy", "Baby", "Hook", "Line", "Death", "Bacon", "Animal", "Lawn", "Punk", "Army", "War", "Watch", "Soldier", "Victory", "Medal", "Imagination", "Harmony", "Reality", "Hard Work", "Dedication", "Chicken", "Feather", "Beard", "Letterbox", "Engineer", "Person", "Expert", "Pig", "Bag", "Cavalry", "Feeling", "Hero", "Dust", "Death", "Cake", "Shot", "Kill", "Spider" , "Fly", "Banana", "Monkey", "Peanut Butter", "Science", "Mountain", "Russia", "Game", "Bear", "Gun", "Gain", "Submarine", "Mind", "Butterfly", "Peace", "Blessing", "Iris", "Halloween", "Cyborg Ninja", "Graveyard", "Candy", "Glitch", "System", "Planet", "Bug", "Head", "Moon", "Winter", "Life", "Gift", "Funeral", "Ice", "Celebration", "Forecast", "Firework", "Rooster", "Fortune", "Party", "Costume", "Snowflake", "Pen", "Outlook", "Hug", "Module", "Programming", "Assistance", "Analysis", "Situation", "Error", "Functionality", "Rain", "Sword", "Enemy", "Fire", "Hole", "Rule", "Resistance", "Rocket", "Queen", "Hammer", "Sight", "Light", "Craftsman", "Tool", "Performance", "Emotion", "Combo", "K.O.", "Punch", "Commentary", "Fist", "Hell", "Father", "Boss", "Drink", "Judgement", "Level", "Protection", "Compliance", "Beer", "Honor", "Firepower", "Adult", "Car Wash", "Existence"]
randomNoun = random.choice(nouns)
randomNoun2 = random.choice(nouns)
randomNoun3 = random.choice(nouns)
cnouns = ["Child", "Mother", "Scope", "Challenger", "Bad Guy", "Hack", "Blade", "Challenge", "Human", "Thing", "Distraction", "Moment", "Dragon", "Dojo", "Barbecue", "Birthday", "Day", "Rhythm", "Champion", "World", "Noise", "Bullet", "Name", "Lesson", "Obstacle", "Eye", "Consultation Fee", "Doctor", "Miracle", "Opinion", "Cake", "Hand", "Professional", "Break", "Man", "Refrigerator", "Psychopath", "Ghost", "Dog", "Apocalypse", "Baby", "Hook", "Animal", "Punk", "Army", "War", "Watch", "Soldier", "Medal", "Chicken", "Feather", "Beard", "Letterbox", "Engineer", "Person", "Expert", "Pig", "Bag", "Feeling", "Hero", "Spider", "Fly", "Banana", "Monkey", "Mountain", "Game", "Bear", "Gun", "Submarine", "Butterfly", "Blessing", "Cyborg Ninja", "Graveyard", "Glitch", "System", "Planet", "Bug", "Head", "Moon", "Life", "Gift", "Funeral", "Celebration", "Firework", "Rooster", "Party", "Costume", "Snowflake", "Pen", "Hug", "Module", "Analysis", "Situation", "Error", "Sword", "Enemy", "Fire", "Hole", "Rule", "Resistance", "Rocket", "Queen", "Hammer", "Light", "Craftsman", "Tool", "Performance", "Emotion", "Combo", "K.O.", "Punch", "Fist", "Father", "Boss", "Drink", "Judgement", "Level", "Adult", "Car Wash"]
randomCNoun = random.choice(cnouns)
randomCNoun2 = random.choice(cnouns)
if randomCNoun[0] == "A" or randomCNoun[0] == "E" or randomCNoun[0] == "I" or randomCNoun[0] == "O" or randomCNoun[0] == "U":
	randomArticleNoun = "An " + randomCNoun
else:
	randomArticleNoun = "A " + randomCNoun
if randomCNoun2[0] == "A" or randomCNoun2[0] == "E" or randomCNoun2[0] == "I" or randomCNoun[0] == "O" or randomCNoun[0] == "U":
	randomArticleNoun2 = "An " + randomCNoun2
else:
	randomArticleNoun2 = "A " + randomCNoun2
#plural
pluralNouns = ["Children", "Mothers", "Scopes", "Challengers", "Bad Guys", "Hacks", "Blades", "Challenges", "Humans", "Things", "Distractions", "Moments", "Dragons", "Dojos", "Barbecues", "Birthdays", "Days", "Champions", "Worlds", "Noises", "Bullets", "Names", "Lessons", "Obstacles", "Eyes", "Consultation Fees", "Doctors", "Miracles", "Opinions", "Cakes", "Hands", "Skies", "Radars", "Professionals", "Breaks", "Men", "Refrigerators", "Psychopaths", "Ghosts", "Dogs", "Candies", "Babies", "Hooks", "Animals", "Punks", "Armies", "Wars", "Soldiers", "Medals", "Realities", "Chickens", "Feathers", "Letterboxes", "Engineers", "People", "Experts", "Pigs", "Bags", "Feelings", "Heroes", "Deaths", "Cakes", "Kills", "Spiders", "Flies", "Bananas", "Monkeys", "Mountains", "Games", "Bears", "Guns", "Submarines", "Minds", "Butterflies", "Blessings", "Graveyards", "Candies", "Glitches", "Systems", "Planets", "Bugs", "Heads", "Moons", "Lives", "Gifts", "Funerals", "Celebrations", "Fireworks", "Roosters", "Parties", "Costumes", "Snowflakes", "Pens", "Hugs", "Modules", "Situations", "Errors", "Functionalities", "Swords", "Enemies", "Fires", "Holes", "Rules", "Rockets", "Queens", "Hammers", "Sights", "Lights", "Tools", "Performances", "Emotions", "Glasses", "Combos", "Punches", "Commentaries", "Fists", "Fathers", "Bosses", "Drinks", "Judgements", "Levels", "Beers", "Adults", "Car Washes"]
randomPluralNoun = random.choice(pluralNouns)
#proper
heroNouns = ["Ana", "Bastion", "Doomfist", "DVa", "Genji", "Hanzo", "Junkrat", "Lucio", "McCree", "Mei", "Mercy", "Moira", "Orisa", "Pharah", "Reaper", "Reinhardt", "Roadhog", "Soldier: 76", "Sombra", "Symmetra", "Torbjorn", "Tracer", "Widowmaker", "Winston", "Zarya", "Zenyatta"]
randomHeroNoun = random.choice(heroNouns)
#bastion
bastionWords = ["Doo", "Woo", "Boo", "Doo", "Dee", "Chirr", "Dah", "Wee", "Dun", "Boop", "Dweet", "Hee", "Hoo", "Sh", "Zwee", "Bud", "Dwee", "Woop", "Woh", "Bew"]
randomBastion1 = random.choice(bastionWords)
randomBastion2 = random.choice(bastionWords)
randomBastion3 = random.choice(bastionWords)
randomBastion4 = random.choice(bastionWords)
randomBastion5 = random.choice(bastionWords)
randomBastion6 = random.choice(bastionWords)
#outlook
outlookPhrases = ["Negative", "Optimal", "Concerning", "Uncertain", "Slight Chance Of Rain"]
randomOutlook = random.choice(outlookPhrases)

#verb
verbs = ["Behave", "Deliver", "Die", "Know", "Learn", "Need", "Tuck", "Think", "Witness", "Expect", "Flow", "Do", "Ignore", "Doubt", "Remember", "Choose", "Step", "Want", "Have", "Give", "Smile", "Hit", "Stop", "Hear", "Believe", "Watch", "Kill", "Like", "Lose", "Reach", "Want", "Chill", "Fight", "Move", "Freeze", "Send", "Take", "See", "Achieve", "Fly", "Look", "Walk", "Kill", "Live", "Salute", "Crush", "Respect", "Take", "Say", "Start", "Finish", "Smell", "Want", "Lack", "Think", "Struggle", "Make", "Underestimate", "Leave", "Buy", "Keep", "Shoot", "Score", "Eat", "Change", "Look", "Miss", "Bench", "Break", "Play", "Hug", "Think", "Swim", "Dream", "Juggle", "Embrace", "Strive", "Hack", "Squish", "Mess", "Die", "Show", "Crow", "Fall", "Find", "Follow", "Request", "Park", "Shine", "Compute", "Divide", "Nerf", "Power", "Balance", "Consume", "Boop", "Cease", "Adjust", "Blame", "Hide", "Fire", "Experience", "Go", "Sit", "Spare", "Talk", "Try", "Joke", "Help", "Trust", "Hold", "Work"]
randomVerb = random.choice(verbs)
randomVerb2 = random.choice(verbs)
#past tense
pastVerbs = ["Delivered", "Behaved", "Died", "Knew", "Rained", "Learnt", "Needed", "Tucked", "Thought", "Witnessed", "Expected", "Flowed", "Did", "Ignored", "Doubted", "Remembered", "Chose", "Stepped", "Wanted", "Had", "Gave", "Smiled", "Hit", "Stopped", "Heard", "Believed", "Watched", "Killed", "Liked", "Lost", "Reached", "Wanted", "Chilled", "Fought", "Moved", "Froze", "Sent", "Took", "Saw", "Achieved", "Flew", "Walked", "Killed", "Lived", "Saluted", "Crushed", "Respected", "Took", "Said", "Started", "Finished", "Smelled", "Wanted", "Lacked", "Thought", "Struggled", "Made", "Underestimated", "Left", "Bought", "Kept", "Shot", "Scored", "Ate", "Changed", "Looked", "Missed", "Benched", "Broke", "Played", "Hugged", "Thought", "Swam", "Freed", "Dreamt", "Juggled", "Embraced", "Strived", "Hacked", "Squished", "Messed", "Died", "Showed", "Crowed", "Fell", "Found", "Followed", "Requested", "Parked", "Computed", "Divided", "Balanced", "Consumed", "Booped", "Adjusted", "Blamed", "Hid", "Fired", "Experienced", "Went", "Sat", "Spared", "Talked", "Tried", "Joked", "Helped", "Trusted", "Held", "Worked"]
randomPastVerb = random.choice(pastVerbs)
randomPastVerb2 = random.choice(pastVerbs)
#present tense
presentVerbs = ["Dies", "Behaves", "Delivers", "Knows", "Rains", "Learns", "Needs", "Tucks", "Thinks", "Witnesses", "Expects", "Flows", "Does", "Ignores", "Doubts", "Remembers", "Chooses", "Steps", "Wants", "Has", "Gives", "Smiles", "Hits", "Stops", "Hears", "Believes", "Watches", "Kills", "Likes", "Loses", "Reaches", "Wants", "Chills", "Fights", "Moves", "Freezes", "Sends", "Takes", "Sees", "Achieves", "Flies", "Looks", "Walks", "Kills", "Lives", "Salutes", "Crushes", "Respects", "Takes", "Says", "Starts", "Finishes", "Smells", "Wants", "Lacks", "Thinks", "Struggles", "Makes", "Underestimates", "Leaves", "Buys", "Keeps", "Shoots", "Scores", "Eats", "Changes", "Misses", "Looks", "Benches", "Breaks", "Plays", "Hugs", "Thinks", "Swims", "Frees", "Dreams", "Juggles", "Embraces", "Strives", "Hacks", "Squishes", "Messes", "Dies", "Shows", "Crows", "Falls", "Finds", "Follows", "Requests", "Parks", "Shines", "Computes", "Divides", "Balances", "Consumes", "Boops", "Adjusts", "Blames", "Hides", "Fires", "Experiences", "Goes", "Sits", "Spares", "Talks", "Tries", "Jokes", "Helps", "Trusts", "Holds", "Works"]
randomPresentVerb = random.choice(presentVerbs)
randomPresentVerb2 = random.choice(presentVerbs)
#ing
ingVerbs = ["Behaving", "Delivering", "Dying", "Knowing", "Raining", "Learning", "Needing", "Tucking", "Thinking", "Witnessing", "Expecting", "Flowing", "Doing", "Ignoring", "Doubting", "Remembering", "Choosing", "Stepping", "Wanting", "Having", "Giving", "Smiling", "Hitting", "Stopping", "Hearing", "Believing", "Watching", "Killing", "Liking", "Losing", "Reaching", "Wanting", "Chilling", "Fighting", "Moving", "Freezing", "Sending", "Taking", "Seeing", "Achieving", "Flying", "Looking", "Walking", "Killing", "Living", "Saluting", "Crushing", "Respecting", "Taking", "Saying", "Starting", "Finishing", "Smelling", "Lacking", "Thinking", "Struggling", "Making", "Underestimating", "Leaving", "Buying", "Keeping", "Shooting", "Scoring", "Eating", "Changing", "Looking", "Missing", "Benching", "Breaking", "Playing", "Hugging", "Thinking", "Swimming", "Freeing", "Dreaming", "Juggling", "Embracing", "Striving", "Hacking", "Squishing", "Messing", "Dying", "Showing", "Crowing", "Falling", "Finding", "Following", "Requesting", "Parking", "Shining", "Computing", "Dividing", "Balancing", "Consuming", "Booping", "Adjusting", "Blaming", "Hiding", "Firing", "Experiencing", "Going", "Sitting", "Sparing", "Talking", "Trying", "Joking", "Helping", "Trusting", "Holding", "Working"]
randomIngVerb = random.choice(ingVerbs)

#sentence
sentences = ['ana', 'dva', 'genji', 'hanzo', 'junkrat', 'lucio', 'mccree', 'bastion', 'mei', 'mercy', 'pharah', 'reaper', 'reinhardt', 'roadhog', 'soldier', 'symmetra', 'torbjorn', 'tracer', 'widowmaker', 'winston', 'zarya', 'zenyatta', 'sombra', 'orisa', 'doomfist', 'moira']
randomSentence = random.choice(sentences)
#ana
anaSentences = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
ana = random.choice(anaSentences)
#dva
dvaSentences = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
dva = random.choice(dvaSentences)
#genji
genjiSentences = ['1', '2', '3', '4', '5', '6', '7', '8']
genji = random.choice(genjiSentences)
#hanzo
hanzoSentences = ['1', '2', '3', '4', '5', '6']
hanzo = random.choice(hanzoSentences)
#junkrat
junkratSentences = ['1', '2', '3', '4', '5', '6', '7']
junkrat = random.choice(junkratSentences)
#lucio
lucioSentences = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
lucio = random.choice(lucioSentences)
#mccree
mccreeSentences = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
mccree = random.choice(mccreeSentences)
#bastion
bastionSentences = ['1', '2', '3', '4', '5', '6']
bastion = random.choice(bastionSentences)
#mei
meiSentences = ['1', '2', '3', '4', '5', '6', '7', '8']
mei = random.choice(meiSentences)
#mercy
mercySentences = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
mercy = random.choice(mercySentences)
#pharah
pharahSentences = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
pharah = random.choice(pharahSentences)
#reaper
reaperSentences = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
reaper = random.choice(reaperSentences)
#reinhardt
reinhardtSentences = ['1', '2', '3', '4', '5', '6', '7']
reinhardt = random.choice(reinhardtSentences)
#roadhog
roadhogSentences = ['1', '2', '3', '4',  '5', '6', '7', '8', '9', '10', '11']
roadhog = random.choice(roadhogSentences)
#soldier: 76
soldierSentences = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
soldier = random.choice(soldierSentences)
#symmetra
symmetraSentences = ['1', '2', '3', '4', '5', '6']
symmetra = random.choice(symmetraSentences)
#torbjorn
torbjornSentences = ['1', '2', '3', '4', '5', '6']
torbjorn = random.choice(torbjornSentences)
#tracer
tracerSentences = ['1', '2', '3', '4', '5', '6', '7', '8']
tracer = random.choice(tracerSentences)
#widowmaker
widowmakerSentences = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
widowmaker = random.choice(widowmakerSentences)
#winston
winstonSentences = ['1', '2', '3', '4', '5', '6']
winston = random.choice(winstonSentences)
#zarya
zaryaSentences = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
zarya = random.choice(zaryaSentences)
#zenyatta
zenyattaSentences = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
zenyatta = random.choice(zenyattaSentences)
#sombra
sombraSentences = ['1', '2', '3', '4', '5', '6', '7']
sombra = random.choice(sombraSentences)
#orisa
orisaSentences = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
orisa = random.choice(orisaSentences)
#doomfist
doomfistSentences = ['1', '2', '3', '4', '5', '6', '7']
doomfist = random.choice(doomfistSentences)
#moira
moiraSentences = ['1', '2', '3']
moira = random.choice(moiraSentences)

#tweet contents
if randomSentence == 'ana':
#ana
	if ana == '1':
		tweetStr = "Ana: " + randomNoun + " Delivered"
	elif ana == '2':
		tweetStr = "Ana: " + randomPluralNoun + ", Behave"
	elif ana == '3':
		tweetStr = "Ana: Everyone " + randomPresentVerb
	elif ana == '4':
		tweetStr = "Ana: It Takes " + randomArticleNoun + " To " + randomVerb + " It"
	elif ana == '5':
		tweetStr = "Ana: " + randomVerb + " From The " + randomNoun
	elif ana == '6':
		tweetStr = "Ana: Mother " + randomPresentVerb + " Best"
	elif ana == '7':
		tweetStr = "Ana: What Are You " + randomIngVerb + "?"
	elif ana == '8':
		tweetStr = "Ana: " + randomVerb + " Me"
	elif ana == '9':
		tweetStr = "Ana: You " + randomVerb + " Nothing"
	elif ana == '10':
		tweetStr = "Ana: " + randomVerb + " From The " + randomNoun
	elif ana == '11':
		tweetStr = "Ana: I'm " + randomIngVerb + " Out For You"
	elif ana == '12':
		tweetStr = "Ana: The " + randomNoun + " In " + randomNoun2
	elif ana == '13':
		tweetStr = "Ana: The " + randomNoun + " " + randomPresentVerb
	elif ana == '14':
		tweetStr = "Ana: " + randomVerb + " Me If You Want To " + randomVerb2
	elif ana == '15':
		tweetStr = "Ana: Shh, The " + randomPluralNoun + " Are " + randomIngVerb
elif randomSentence == 'dva':
	#dva
	if dva == '1':
		tweetStr = "DVa: Love " + randomHeroNoun 
	elif dva == '2':
		tweetStr = "DVa: Here Comes A New " + randomNoun +  "!"
	elif dva == '3':
		tweetStr = "DVa: I Play To " + randomVerb
	elif dva == '4':
		tweetStr = "DVa: No " + randomPluralNoun + " Required"
	elif dva == '5':
		tweetStr = "DVa: Happy " + randomNoun + "!"
	elif dva == '6':
		tweetStr = "DVa: I Get The Feeling You're Not " + randomIngVerb + " Me Seriously"
	elif dva == '7':
		tweetStr = "DVa: " + randomVerb + " This"
	elif dva == '8':
		tweetStr = "DVa: DVa - 1, " + randomHeroNoun + " - 0"
	elif dva == '9':
		tweetStr = "DVa: I'm #" + str(random.randrange(0,100)) + "!"
elif randomSentence == 'genji':
	#genji
	if genji == '1':
		tweetStr = "Genji: A Steady " + randomNoun + " " + randomPresentVerb + " The " + randomNoun
	elif genji == '2':
		tweetStr = "Genji: I Was Hoping For " + randomArticleNoun
	elif genji == '3':
		tweetStr = "Genji: Let's " + randomVerb
	elif genji == '4':
		tweetStr = "Genji: " + randomVerb + " Twice, " + randomVerb2 + " Once"
	elif genji == '5':
		tweetStr = "Genji: My " + randomNoun + " Seeks Balance"
	elif genji == '6':
		tweetStr = "Genji: My Halloween Costume? " + randomNoun
	elif genji == '7':
		tweetStr = "Genji: " + randomNoun + " And " + randomNoun2 + " " + randomVerb + " On The Edge Of My " + randomNoun3
	elif genji == '8':
		tweetStr = "Genji: You Seem Nice, I Hate To " + randomVerb + " You"
elif randomSentence == 'hanzo':
	#hanzo
	if hanzo == '1':
		tweetStr = "Hanzo: Ignore All " + randomPluralNoun
	elif hanzo == '2':
		tweetStr = "Hanzo: Remember This " + randomNoun
	elif hanzo == '3':
		tweetStr = "Hanzo: I Choose You, Spirit " + randomNoun
	elif hanzo == '4':
		tweetStr = "Hanzo: Step Into The " + randomNoun
	elif hanzo == '5':
		tweetStr = "Hanzo: " + randomArticleNoun + " For You"
	elif hanzo == '6':
		tweetStr = "Hanzo: " + randomVerb + " Like " + randomNoun
elif randomSentence == 'junkrat':
	#junkrat
	if junkrat == '1':
		tweetStr = "Junkrat: Anyone Want Some " + randomNoun + "?"
	elif junkrat == '2':
		tweetStr = "Junkrat: Have A Nice " + randomNoun
	elif junkrat == '3':
		tweetStr = "Junkrat: It's The Little " + randomPluralNoun
	elif junkrat == '4':
		tweetStr = "Junkrat: Happy " + randomNoun
	elif junkrat == '5':
		tweetStr = "Junkrat: Fire In The " + randomNoun
	elif junkrat == '6':
		tweetStr = "Junkrat: Oops... " + randomPastVerb + " Something"
	elif junkrat == '7':
		tweetStr = "Junkrat: I Give It A " + str(random.randrange(0,11)) + "!"
elif randomSentence == 'lucio':
	#lucio
	if lucio == '1':
		tweetStr = "Lucio: To The " + randomNoun
	elif lucio == '2':
		tweetStr = "Lucio: Be " + randomPluralNoun
	elif lucio == '3':
		tweetStr = "Lucio: Can't " + randomVerb + ", Won't " + randomVerb
	elif lucio == '4':
		tweetStr = "Lucio: " + randomVerb + " Me!"
	elif lucio == '5':
		tweetStr = "Lucio: Not Hearing That " + randomNoun
	elif lucio == '6':
		tweetStr = "Lucio: You Gotta " + randomVerb + "!"
	elif lucio == '7':
		tweetStr = "Lucio: " + randomPastVerb + " It!"
	elif lucio == '8':
		tweetStr = "Lucio: Happy " + randomNoun + "!"
	elif lucio == '9':
		tweetStr = "Lucio: Have Some " + randomHeroNoun + "-Oh's!"
	elif lucio == '10':
		tweetStr = "Lucio: I'm On Top Of The " + randomNoun
elif randomSentence == 'mccree':
	#mccree
	if mccree == '1':
		tweetStr = "McCree: Watch And " + randomVerb
	elif mccree == '2':
		tweetStr = "McCree: You Seem Familiar. Ain't I " + randomPastVerb + " You Before?"
	elif mccree == '3':
		tweetStr = "McCree: I Don't Much Like " + randomIngVerb
	elif mccree == '4':
		tweetStr = "McCree: I'm Your " + randomNoun
	elif mccree == '5':
		tweetStr = "McCree: I've Got " + randomArticleNoun + " With Your Name On It"
	elif mccree == '6':
		tweetStr = "McCree: Reach For The " + randomNoun
	elif mccree == '7':
		tweetStr = "McCree: I Don't Much Like " + randomIngVerb
	elif mccree == '8':
		tweetStr = "McCree: It's Your " + randomNoun
	elif mccree == '9':
		tweetStr = "McCree: Had To " + randomVerb + " The " + randomNoun
	elif mccree == '10':
		tweetStr = "McCree: Calls For " + randomArticleNoun
	elif mccree == '11':
		tweetStr = "McCree: A Man's Gotta Have " + randomPluralNoun
	elif mccree == '12':
		tweetStr = "McCree: It's High " + randomNoun
	elif mccree == '13':
		tweetStr = "McCree: Boom Goes The " + randomNoun
elif randomSentence == 'bastion':
	#bastion
	if bastion == '1':
		tweetStr = "Bastion: " + randomBastion1
	elif bastion == '2':
		tweetStr = "Bastion: " + randomBastion1 + " " + randomBastion2
	elif bastion == '3':
		tweetStr = "Bastion: " + randomBastion1 + " " + randomBastion2 + " " + randomBastion3
	elif bastion == '4':
		tweetStr = "Bastion: " + randomBastion1 + " " + randomBastion2 + " " + randomBastion3 + " " + randomBastion4
	elif bastion == '5':
		tweetStr = "Bastion: " + randomBastion1 + " " + randomBastion2 + " " + randomBastion3 + " " + randomBastion4 + " " + randomBastion5
	elif bastion == '6':
		tweetStr = "Bastion: " + randomBastion1 + " " + randomBastion2 + " " + randomBastion3 + " " + randomBastion4 + " " + randomBastion5 + " " + randomBastion6
	#end of the sentence, doing nothing for the declarative since it is already done
	bastionSentenceGenerator = ['declarative', 'interrogative', 'exclamatory']
	bastionSentence = random.choice(bastionSentenceGenerator)
	if bastionSentence == 'interrogative':
		tweetStr = tweetStr + "?"
	elif bastionSentence == 'exclamatory':
		tweetStr = tweetStr + "!"
elif randomSentence == 'mei':
	#mei
	if mei == '1':
		tweetStr = "Mei: " + randomVerb + " For Our " + randomNoun
	elif mei == '2':
		tweetStr = "Mei: I Hope You " + randomPastVerb + " Your " + randomNoun
	elif mei == '3':
		tweetStr = "Mei: Overcome All " + randomPluralNoun
	elif mei == '4':
		tweetStr = "Mei: " + randomVerb + "! Don't " + randomVerb2 + "!"
	elif mei == '5':
		tweetStr = "Mei: You Have To Let It " + randomVerb
	elif mei == '6':
		tweetStr = "Mei: I Was Only Trying To " + randomVerb
	elif mei == '7':
		tweetStr = "Mei: Did You " + randomVerb + " Something?"
	elif mei == '8':
		tweetStr = "Mei: I'm Going To Have To " + randomVerb + " The Heck Out Of This!"
elif randomSentence == 'mercy':
	#mercy
	if mercy == '1':
		tweetStr = "Mercy: I Have My " + randomNoun + " On You"
	elif mercy == '2':
		tweetStr = "Mercy: I'll Send You My " + randomNoun
	elif mercy == '3':
		tweetStr = "Mercy: Need A Second " + randomNoun
	elif mercy == '4':
		tweetStr = "Mercy: On A Scale Of One To Ten, How Is Your " + randomNoun + "?"
	elif mercy == '5':
		tweetStr = "Mercy: Piece Of " + randomNoun
	elif mercy == '6':
		tweetStr = "Mercy: The " + randomNoun + " Is In"
	elif mercy == '7':
		tweetStr = "Mercy: " + randomPluralNoun + " Never " + randomVerb
	elif mercy == '8':
		tweetStr = "Mercy: The Doctor Will " + randomVerb + " You"
	elif mercy == '9':
		tweetStr = "Mercy: Sometimes You " + randomVerb + " Me"
elif randomSentence == 'pharah':
	#pharah
	if pharah == '1':
		tweetStr = "Pharah: Put Your " + randomNoun + " In My " + randomPluralNoun
	elif pharah == '2':
		tweetStr = "Pharah: " + randomVerb + " Like An Egyptian"
	elif pharah == '3':
		tweetStr = "Pharah: " + randomIngVerb + " The Friendly " + randomPluralNoun
	elif pharah == '4':
		tweetStr = "Pharah: I've Got You On My " + randomNoun
	elif pharah == '5':
		tweetStr = "Pharah: Play Nice, Play " + randomHeroNoun
	elif pharah == '6':
		tweetStr = "Pharah: Sorry, But I Need To " + randomVerb
	elif pharah == '7':
		tweetStr = "Pharah: I " + randomVerb + " The " + randomNoun
	elif pharah == '8':
		tweetStr = "Pharah: I Am The " + randomNoun + " Queen"
	elif pharah == '9':
		tweetStr = "Pharah: " + randomNoun + " " + randomPresentVerb + " From Above"
	elif pharah == '10':
		tweetStr = "Pharah: " + randomVerb + " Casual"
	elif pharah == '11':
		tweetStr = "Pharah: " + randomVerb + " Me"
	elif pharah == '12':
		tweetStr = "Pharah: Leave This To " + randomArticleNoun
	elif pharah == '13':
		tweetStr = "Pharah: Put Your " + randomNoun + " In My " + randomPluralNoun
elif randomSentence == 'reaper':
	#reaper
	if reaper == '1':
		tweetStr = "Reaper: What Are You " + randomIngVerb + " At?"
	elif reaper == '2':
		tweetStr = "Reaper: Dead Man " + randomIngVerb
	elif reaper == '3':
		tweetStr = "Reaper: Give Me " + randomArticleNoun
	elif reaper == '4':
		tweetStr = "Reaper: Haven't I " + randomPastVerb + " You Somewhere Before?"
	elif reaper == '5':
		tweetStr = "Reaper: If It " + randomPresentVerb + ", I Can " + randomVerb + " It"
	elif reaper == '6':
		tweetStr = "Reaper: It's In The " + randomNoun
	elif reaper == '7':
		tweetStr = "Reaper: I Am Not " + randomArticleNoun + ". I Am A High-Functioning " + randomNoun
	elif reaper == '8':
		tweetStr = "Reaper: You Look Like You've Seen " + randomArticleNoun
	elif reaper == '9':
		tweetStr = "Reaper: I " + randomVerb + " The " + randomNoun + " Shift"
	elif reaper == '10':
		tweetStr = "Reaper: Now Those Are Some " + randomPluralNoun
	elif reaper == '11':
		tweetStr = "Reaper: " + randomVerb + ", " + randomVerb + ", " + randomVerb
	elif reaper == '12':
		tweetStr = "Reaper: I'll " + randomVerb + " You In Hell"
	elif reaper == '13':
		tweetStr = "Reaper: No " + randomNoun + " Left Behind"
	elif reaper == '14':
		tweetStr = "Reaper: Just " + randomVerb
elif randomSentence == 'reinhardt':
	#reinhardt
	if reinhardt == '1':
		tweetStr = "Reinhardt: I " + randomVerb + " You"
	elif reinhardt == '2':
		tweetStr = "Reinhardt: I'm The Ultimate " + randomIngVerb + " Machine"
	elif reinhardt == '3':
		tweetStr = "Reinhardt: " + randomVerb + " Your Elders"
	elif reinhardt == '4':
		tweetStr = "Reinhardt: " + randomNoun + "! " + randomNoun2 + "! Reinhardt!"
	elif reinhardt == '5':
		tweetStr = "Reinhardt: Are You Afraid To " + randomVerb + " Me?"
	elif reinhardt == '6':
		tweetStr = "Reinhardt: This Old " + randomNoun + " Still Knows A Few Tricks"
	elif reinhardt == '7':
		tweetStr = "Reinhardt: " + str(random.randrange(0,101)) + "% German Power"
elif randomSentence == 'roadhog':
	#roadhog
	if roadhog == '1':
		tweetStr = "Roadhog: Welcome To The " + randomNoun
	elif roadhog == '2':
		tweetStr = "Roadhog: Like Taking " + randomPluralNoun + " From " + randomArticleNoun
	elif roadhog == '3':
		tweetStr = "Roadhog: " + randomNoun + ", " + randomNoun2 + ", And Sinker"
	elif roadhog == '4':
		tweetStr = "Roadhog: Life Is " + randomNoun + ", So Is Death"
	elif roadhog == '5':
		tweetStr = "Roadhog: Piece Of " + randomNoun
	elif roadhog == '6':
		tweetStr = "Roadhog: Say " + randomNoun + " One More Time"
	elif roadhog == '7':
		tweetStr = "Roadhog: We Are All " + randomPluralNoun
	elif roadhog == '8':
		tweetStr = "Roadhog: Want Some " + randomNoun + "?"
	elif roadhog == '9':
		tweetStr = "Roadhog: I've " + randomPastVerb + " " + "Someone For Less Than That"
	elif roadhog == '10':
		tweetStr = "Roadhog: There's No 'I' In " + randomNoun
	elif roadhot == '11':
		tweetStr = "Roadhog: I Don't Like " + randomPluralNoun
elif randomSentence == 'soldier':
	#soldier: 76
	if soldier == '1':
		tweetStr = "Soldier 76: Young " + randomPluralNoun + ", Get Off My " + randomNoun
	elif soldier == '2':
		tweetStr = "Soldier 76: I Didn't Start This " + randomNoun + ", But I Am Damn Well Gonna Finish It"
	elif soldier == '3':
		tweetStr = "Soldier 76: Not On My " + randomNoun
	elif soldier == '4':
		tweetStr = "Soldier 76: Old " + randomPluralNoun + " Never Die, And They Don't Fade Away"
	elif soldier == '5':
		tweetStr = "Soldier 76: Smells Like " + randomNoun
	elif soldier == '6':
		tweetStr = "Soldier 76: You Want A " + randomNoun + "?"
	elif soldier == '7':
		tweetStr = "Soldier 76: The " + randomNoun + " " + randomPresentVerb + " At Midnight"
	elif soldier == '8':
		tweetStr = "Soldier 76: I've Got You In My " + randomPluralNoun
	elif soldier == '9':
		tweetStr = "Soldier 76: I'm Not Your " + randomNoun
	elif soldier == '10':
		tweetStr = "Soldier 76: You're The " + randomNoun
elif randomSentence == 'symmetra':
	#symmetra
	if symmetra == '1':
		tweetStr = "Symmetra: Such A Lack Of " + randomNoun
	elif symmetra == '2':
		tweetStr = "Symmetra: Welcome To My " + randomNoun
	elif symmetra == '3':
		tweetStr = "Symmetra: Why Do You " + randomVerb + "?"
	elif symmetra == '4':
		tweetStr = "Symmetra: " + randomNoun + " And " + randomNoun2 + " Pays Off"
	elif symmetra == '5':
		tweetStr = "Symmetra: Setting Up The " + randomNoun
	elif symmetra == '6':
		tweetStr = "Symmetra: What... Interesting Ways Your " + randomNoun + " " + randomPresentVerb
elif randomSentence == 'torbjorn':
	#torbjorn
	if torbjorn == '1':
		tweetStr = "Torbjorn: " + randomNoun + " Pays Off"
	elif torbjorn == '2':
		tweetStr = "Torbjorn: You're Making " + randomArticleNoun + " Out Of " + randomArticleNoun2
	elif torbjorn == '3':
		tweetStr = "Torbjorn: People Always Underestimate The " + randomPluralNoun
	elif torbjorn == '4':
		tweetStr = "Torbjorn: Let's Not Buy The " + randomNoun + " While It Is Still In The " + randomNoun2
	elif torbjorn == '5':
		tweetStr = "Torbjorn: Just Start " + randomIngVerb
	elif torbjorn == '6':
		tweetStr = "Torbjorn: " + randomVerb + " Me"
elif randomSentence == 'tracer':
	#tracer
	if tracer == '1':
		tweetStr = "Tracer: Cheers, Love! The " + randomNoun + "'s Here!"
	elif tracer == '2':
		tweetStr = "Tracer: Keep Calm And " + randomHeroNoun + " On"
	elif tracer == '3':
		tweetStr = "Tracer: She " + randomPresentVerb + ", She " + randomPresentVerb2 + "!"
	elif tracer == '4':
		tweetStr = "Tracer: The World Could Always Use More " + randomPluralNoun
	elif tracer == '5':
		tweetStr = "Tracer: Eat My " + randomNoun
	elif tracer == '6':
		tweetStr = "Tracer: It's In The " + randomNoun
	elif tracer == '7':
		tweetStr = "Tracer: Who's Ready For Some " + randomPluralNoun + "?"
	elif tracer == '8':
		tweetStr = "Tracer: Did I " + randomVerb + " Something?"
#widowmaker
elif randomSentence == 'widowmaker':
	if widowmaker == '1':
		tweetStr = "Widowmaker: A Single " + randomNoun + " Can " + randomVerb + " Everything"
	elif widowmaker == '2':
		tweetStr = "Widowmaker: Let Them " + randomVerb + " " + randomNoun
	elif widowmaker == '3':
		tweetStr = "Widowmaker: Look For The " + randomNoun
	elif widowmaker == '4':
		tweetStr = "Widowmaker: One " + randomNoun + ", One " + randomNoun2
	elif widowmaker == '5':
		tweetStr = "Widowmaker: I Don't " + randomVerb
	elif widowmaker == '6':
		tweetStr = "Widowmaker: The " + randomNoun + " Is Over"
	elif widowmaker == '7':
		tweetStr = "Widowmaker: The " + randomNoun + " Is About To Begin"
	elif widowmaker == '8':
		tweetStr = "Widowmaker: Your " + randomPluralNoun + " Make You Vulnerable"
	elif widowmaker == '9':
		tweetStr = "Widowmaker: No One Can Hide From My " + randomNoun
	elif widowmaker == '10':
		tweetStr = "Widowmaker: What " + randomArticleNoun
	elif widowmaker == '11':
		tweetStr = "Widowmaker: A Perfect " + str(random.randrange(0, 11))
	elif widowmaker == '12':
		shot = random.randrange(0, 100)
		if shot != 1:
			shotString = str(shot) + " Shots"
		else:
			shotString = str(shot) + " Shot"
		tweetStr = "Widowmaker: " + shotString + ", 1 Kill"
#winston
elif randomSentence == 'winston':
	if winston == '1':
		tweetStr = "Winston: No, I Do Not Want " + randomArticleNoun
	elif winston == '2':
		tweetStr = "Winston: Did Someone Say " + randomNoun + "?"
	elif winston == '3':
		tweetStr = "Winston: The Power Of " + randomNoun
	elif winston == '4':
		tweetStr = "Winston: This Is Not " + randomArticleNoun
	elif winston == '5':
		tweetStr = "Winston: Have You " + randomPastVerb + " My " + randomPluralNoun
	elif winston == '6':
		tweetStr = "Winston: It's My Time To " + randomVerb + "!"
#zarya
elif randomSentence == 'zarya':
	if zarya == '1':
		tweetStr = "Zarya: Strong As The " + randomNoun
	elif zarya == '2':
		tweetStr = "Zarya: I Can " + randomVerb + " More Than You"
	elif zarya == '3':
		tweetStr = "Zarya: I Will " + randomVerb + " You"
	elif zarya == '4':
		tweetStr = "Zarya: In Russia, " + randomNoun + " " + randomPresentVerb + " You"
	elif zarya == '5':
		tweetStr = "Zarya: I Want To " + randomVerb + " You Like Big, Fuzzy Siberian " + randomNoun
	elif zarya == '6':
		tweetStr = "Zarya: Welcome To The " + randomNoun + " Show"
	elif zarya == '7':
		tweetStr = "Zarya: No " + randomNoun + ", No " + randomNoun2
	elif zarya == '8':
		tweetStr = "Zarya: Get Down, Give Me " + str(random.randrange(0, 100)) + "!"
	elif zarya == '9':
		tweetStr = "Zarya: It's Only " + randomArticleNoun + ", Why Do You Have To Be Mad?"
#zenyatta
elif randomSentence == 'zenyatta':
	if zenyatta == '1':
		tweetStr = "Zenyatta: " + randomNoun + " Is Whimsical Today"
	elif zenyatta == '2':
		tweetStr = "Zenyatta: Do I " + randomVerb + "? Does " + randomArticleNoun + " " + randomVerb + "?"
	elif zenyatta == '3':
		tweetStr = "Zenyatta: " + randomVerb + " Your " + randomNoun
	elif zenyatta == '4':
		tweetStr = "Zenyatta: I Dreamt I Was " + randomArticleNoun
	elif zenyatta == '5':
		tweetStr = "Zenyatta: I " + randomVerb + ", Therefore I Am"
	elif zenyatta == '6':
		tweetStr = "Zenyatta: I Will Not " + randomVerb
	elif zenyatta == '7':
		tweetStr = "Zenyatta: The " + randomNoun + " " + randomPresentVerb + " You"
	elif zenyatta == '8':
		tweetStr = "Zenyatta: No " + randomNoun + " Ever " + randomPresentVerb + " In The Wrong Place"
	elif zenyatta == '9':
		tweetStr = "Zenyatta: Every " + randomNoun + " " + randomPresentVerb + " In Its Own " + randomNoun
	elif zenyatta == '10':
		tweetStr = "Zenyatta: " + randomVerb + " Along The Path To Enlightenment"
	elif zenyatta == '11':
		tweetStr = "Zenyatta: " + randomNoun + " And " + randomPluralNoun + " Be Upon You All"
#sombra
elif randomSentence == 'sombra':
	if sombra == '1':
		tweetStr = "Sombra: You're Just " + randomArticleNoun + " In The " + randomNoun2
	elif sombra == '2':
		tweetStr = "Sombra: " + randomVerb + " The " + randomNoun
	elif sombra == '3':
		tweetStr = "Sombra: Just " + randomIngVerb + " " + randomArticleNoun
	elif sombra == '4':
		tweetStr = "Sombra: " + randomVerb + " With The Best And " + randomVerb2 + " Like The Rest"
	elif sombra == '5':
		tweetStr = "Sombra: I'd Love To Stay And " + randomVerb + ", But I'm Not Going To"
	elif sombra == '6':
		tweetStr = "Sombra: I Need " + randomArticleNoun
	elif sombra == '7':
		tweetStr = "Sombra: Were You Done " + randomIngVerb
#orisa
elif randomSentence == 'orisa':
	if orisa == '1':
		tweetStr = "Orisa: Current Outlook - " + randomOutlook
	elif orisa == '2':
		tweetStr = "Orisa: Do You Need A " + randomNoun
	elif orisa == '3':
		tweetStr = "Orisa: I Am Simply " + randomIngVerb + " My " + randomNoun
	elif orisa == '4':
		tweetStr = "Orisa: Would You Like My Analysis Of The " + randomNoun + "?"
	elif orisa == '5':
		tweetStr = "Orisa: No " + randomIngVerb
	elif orisa == '6':
		tweetStr = "Orisa: " + randomVerb + " Your " + randomPluralNoun
	elif orisa == '7':
		tweetStr = "Orisa: That Does Not " + randomVerb
	elif orisa == '8':
		tweetStr = "Orisa: Are You Satisfied With Your " + randomNoun + "?"
	elif orisa == '9':
		tweetStr = "Orisa: Thank You For Your " + randomNoun
#doomfist
elif randomSentence == 'doomfist':
	if doomfist == '1':
		tweetStr = "Doomfist: " + randomNoun + " Breaker!"
	elif doomfist == '2':
		tweetStr = "Doomfist: Go And " + randomVerb
	elif doomfist == '3':
		tweetStr = "Doomfist: One " + randomNoun + " Is All I Need"
	elif doomfist == '4':
		tweetStr = "Doomfist: Spare Me The " + randomNoun
	elif doomfist == '5':
		tweetStr = "Doomfist: Talk To The " + randomNoun
	elif doomfist == '6':
		tweetStr = "Doomfist: " + randomVerb + " Me"
	elif doomfist == '7':
		tweetStr = "Doomfist: You Must Be " + randomIngVerb
#moira
elif randomSentence == 'moira':
	if moira == '1':
		tweetStr = "Moira: I'm " + randomIngVerb
	elif moira == '2':
		tweetStr = "Moira: One " + randomNoun + " " + randomPresentVerb + ", The Other " + randomPresentVerb2
	elif moira == '3':
		tweetStr = "Moira: What An Interesting " + randomNoun
