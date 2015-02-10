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
"Cecil B. DeMille Award",
"Host of the Show"]



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
["cecil","award"],
["golden","hosts"]]

Num_of_Category = len(Award_Categories)

remove_keywords = ["best","picture" , "actor","actress","hosts","hosting","drama","golden","globes","movie","director","song","original"
,"foreign","film","tv","series","mini","supporting","screenplay","presenting","presented","musical",
"comedy","motion","animated","feature","wins","winner","won","cecil", "b", "demille","goldenglobes","score","miniseries","award"]

Nominees = dict()


def get_nominees(index):
	 #urls must be in list, even though only one url
    urls = ["http://www.imdb.com/event/ev0000292/2013",
    "http://www.imdb.com/event/ev0000292/2015"]
    #get handler instance
    handler = GGPHandler()
    #get scraper instance with specific urls and handler
    scraper = Scraper(urls, handler)
    #result is a dict {'url': handler return}
    #print it out for more information
    result = scraper.fetch()
    #pp = pprint.PrettyPrinter(indent=0)
    #pp.pprint(result)
    #this is handle result that contains awards and nominees
    #you can iterate awards for eacha award and get related nominees
    #pp.pprint(result[urls[index]])
    Nominees = result[urls[index]]
    return Nominees
    #pdb.set_trace()

def create_useful_tweet_bank():
	word = ["winner","wins","hosts","presenting","won","hosting"]
	words = ["hosting","best actor", "best actress", "best supporting","best picture", "best movie","best director",
	"best original song", "best foreign film",
	 "best original score","best animated", "tv series",
	  "best screenplay","mini series","Cecil B. DeMille Award","presenting","presented"]
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



def get_winners():
	for x in range(0,Num_of_Category,1):
		find_winners(Award_Categories[x],Category_keywords[x])
	return


def get_fullName(word,category):
	#pdb.set_trace()
	for each in Nominees[category]:
		if each.lower().find(word) != -1:
			return each



def find_winners(category,keywords):
	new = []
	file = open("tempfile.txt", "w")
	temp_dict = dict()
	for twt in new_tweets:
		t = twt.lower()
		if ((keywords[0] in t)  and (keywords[1] in t)):
			new.append(twt)
			tn = re.sub(r'[^a-zA-Z0-9 ]',r'',twt)
			stopwords = nltk.corpus.stopwords.words('english')
			word_list = tn.split()
			res = ' '.join([i for i in word_list if i.lower() not in stopwords])
			left = res.lower()
			leftout = left.split()
			final_sentence = ' '.join([i for i in leftout if i.lower() not in remove_keywords])
			tokens = wordTokenizer.tokenize(final_sentence)
			if category == "Host of the Show":
				big = nltk.bigrams(tokens)
				for key in big:
					if key in temp_dict:
						temp_dict[key] += 1
					else:
						temp_dict[key] = 1
			else:
				for k in tokens:
					if k in temp_dict:
						temp_dict[k] += 1
					else:
						temp_dict[k] = 1
			#pdb.set_trace()
			file.write(final_sentence)
			file.write("\n")
	file.close()
	if temp_dict: 
		abc = max(temp_dict, key = temp_dict.get)
		if (category != "Cecil B. DeMille Award") and (category != "Host of the Show"):
			name = get_fullName(abc,category)
			#pdb.set_trace()
		if (category == "Host of the Show"):
			print (category +":"+"%s %s"%abc)
		elif(category == "Cecil B. DeMille Award"):
			print (category+": "+str(abc))
		else:
			print (category+": "+str(name))
	if category == "Host of the Show":
		temp_dict.pop(abc, None)
		xyz = max(temp_dict, key = temp_dict.get)
		print ("and "+"%s %s"%xyz)
		
	



def main():
	
	create_useful_tweet_bank()
	print "\n\n### WINNERS & HOSTS ### \n"
	get_winners()
	#find_winners(Award_Categories[19],Category_keywords[19])
	
	#pdb.set_trace()


if __name__ == '__main__':
	Nominees = get_nominees(0)
	main()


#pdb.set_trace()