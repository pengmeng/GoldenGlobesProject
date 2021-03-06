import json
import nltk
import re, string
import pdb
import pprint
from nltk.corpus import stopwords
from nltk.util import ngrams
from crawler.scraper import Scraper
from crawler.ggphandler import GGPHandler


sentenceTokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
with open('goldenglobes.json', 'r') as f:
    tweets = map(json.loads, f)

tweet_text = [tweet['text'] for tweet in tweets]
new_tweets = []

from nltk.tokenize import TreebankWordTokenizer
wordTokenizer = TreebankWordTokenizer()


Award_Categories = ["Best Motion Picture - Drama",
"Best Motion Picture - Comedy or Musical",
"Best Director - Motion Picture",
"Best Performance by an Actor in a Motion Picture - Drama",
"Best Performance by an Actor in a Motion Picture - Comedy or Musical",
"Best Performance by an Actress in a Motion Picture - Drama",
"Best Performance by an Actress in a Motion Picture - Comedy or Musical",
"Best Performance by an Actor in a Supporting Role in a Motion Picture",
"Best Performance by an Actress in a Supporting Role in a Motion Picture",
"Best Screenplay - Motion Picture",
"Best Original Score - Motion Picture",
"Best Original Song - Motion Picture",
"Best Foreign Language Film",
"Best Animated Film",
# TV AWARDS
"Best Television Series - Drama",
"Best Television Series - Musical or Comedy",
"Best Performance by an Actor in a Television Series - Drama",
"Best Performance by an Actress in a Television Series - Drama",
"Best Performance by an Actor in a Television Series - Musical or Comedy",
"Best Performance by an Actress in a Television Series - Musical or Comedy",
"Best Performance by an Actor in a Mini-Series or a Motion Picture Made for Television",
"Best Performance by an Actress in a Mini-Series or a Motion Picture Made for Television",
"Best Performance by an Actor in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television",
"Best Performance by an Actress in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television",
"Best Mini-Series or Motion Picture Made for Television",
"Cecil B. DeMille Award"]



Category_keywords = [["best picture","drama"],
["best picture","comedy"],
["best","director"],
["best actor","drama"],
["best actor","comedy"],
["best actress","drama"],
["best actress","comedy"],
["best supporting","actor"],
["best supporting","actress"],
["best","screenplay"],
["best","original score"],
["best","original song"],
["best","foreign language"],
["best animated","film"],
["best tv series","drama"],
["best tv series","comedy"],
["best actor","tv series drama"],
["best actress","tv series drama"],
["best actor tv","comedy"],
["best actress","tv series comedy"],
["best actor","miniseries"],
["best actress","miniseries"],
["best supporting actor","tv"],
["best supporting actress","tv"],
["best miniseries","tv"],
["cecil","award"]]

Num_of_Category = len(Award_Categories)
NUMBER_OF_BEST_DRESSED = 5
NUMBER_OF_PRESENTERS = 26
BIGRAM_RE = "([A-Z][a-z]+\s[A-Z][-'a-zA-Z]+)"

remove_keywords = ["best","picture" , "actor","actress","hosts","hosting","drama","golden","globes",
"movie","director","song","original","foreign","film","tv","series","mini","supporting","screenplay",
"presenting","presented","musical","comedy","motion","animated","feature","wins","winner","won","cecil",
 "demille","goldenglobes","score","miniseries","award","dressed","dress","b"]


def create_useful_tweet_bank():
	word = ["winner","wins","hosts","presenting","won","hosting","dress","dressed", "party", "parties", "should", "better"]
	count = 0
	file = open("newfile.txt", "w")
	for t in tweet_text:
		temp = t.lower()
		for w in word:
			if (w in temp) and ("RT" not in t):
				new_tweets.append(t)
				token = re.sub(r'[^a-zA-Z0-9 ]',r'',t)
				file.write(token)
				file.write("\n")
				count += 1
	#pdb.set_trace()
	file.close()
	#print count

def find_biggest_upsets():
    # This function will find the biggest upsets of the show according to twitter
    results = dict()
    for tweet in new_tweets:
        possible_winners = list()
        tt = tweet.lower()
        host_words = ["better win", "should have won"]
        for w in host_words:
            if w in tt:
                possible_winners = possible_winners + re.findall(BIGRAM_RE, tweet)
        for r in possible_winners:
            if r in results:
                results[r] += 1
            else:
                results[r] = 1
    results.pop("Golden Globes")
    results.pop("better win")       # This is a list of words we want to remove if I'm not mistaken?
    results.pop("should have won")
    i = 0
    biggest_upsets = list()
    while results and (i < 3):
        each = max(results, key = results.get);
        if biggest_upsets != winners_list           # THIS IS BASICALLY PSEUDOCODE #######################################
            biggest_upsets.append(each);            # If one of these returned names is in the winners list, they can't be an upset (they won)
        results.pop(each);
        i += 1
    return biggest_upsets

def main():
    create_useful_tweet_bank()
    upsets = find_biggest_upsets()                  # We have the most talked about people/pictures
    for loser in upsets:                            # For each of these candidates
        for anyone in nominees_list                 # We find their corresponding entry among our Nominees
            if loser = anyone                       # From this we can should be able to get the award category???
                upset_award = anyone.award_category
    print(str(loser) + "should have won" + str(upset_award))     # We print that the loser could have won the award and title it "Biggest Upsets According to Twitter"



if __name__ == '__main__':
	main()
