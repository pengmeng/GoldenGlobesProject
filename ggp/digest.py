import json
import re
from collections import defaultdict

import nltk
from nltk.tokenize import TreebankWordTokenizer

from crawler.scraper import Scraper
from crawler.ggphandler import GGPHandler


wordTokenizer = TreebankWordTokenizer()
Award_Categories = []
tweet_text = []

Award_Categories_13 = ["Best Motion Picture - Drama",
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

Award_Categories_15 = ["Best Motion Picture - Drama",
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
                       "Best Animated Feature Film",
                       # TV AWARDS
                       "Best Television Series - Drama",
                       "Best Television Series - Comedy or Musical",
                       "Best Performance by an Actor in a Television Series - Drama",
                       "Best Performance by an Actress in a Television Series - Drama",
                       "Best Performance by an Actor in a Television Series - Comedy or Musical",
                       "Best Performance by an Actress in a Motion Picture - Comedy or Musical",
                       "Best Performance by an Actor in a Mini-Series or a Motion Picture Made for Television",
                       "Best Performance by an Actress in a Mini-Series or a Motion Picture Made for Television",
                       "Best Performance by an Actor in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television",
                       "Best Performance by an Actress in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television",
                       "Best Mini-Series or Motion Picture Made for Television",
                       "Cecil B. DeMille Award"]

Category_keywords = [["best picture", "drama"],
                     ["best picture", "comedy"],
                     ["best", "director"],
                     ["best actor", "drama"],
                     ["best actor", "comedy"],
                     ["best actress", "drama"],
                     ["best actress", "comedy"],
                     ["best supporting", "actor"],
                     ["best supporting", "actress"],
                     ["best", "screenplay"],
                     ["best", "original score"],
                     ["best", "original song"],
                     ["best", "foreign language"],
                     ["best animated", "film"],
                     ["best tv series", "drama"],
                     ["best tv series", "comedy"],
                     ["best actor", "tv series drama"],
                     ["best actress", "tv series drama"],
                     ["best actor tv", "comedy"],
                     ["best actress", "tv series comedy"],
                     ["best actor", "miniseries"],
                     ["best actress", "miniseries"],
                     ["best supporting actor", "tv"],
                     ["best supporting actress", "tv"],
                     ["best miniseries", "tv"],
                     ["cecil", "DeMille"]]

new_tweets = []
Num_of_Category = len(Award_Categories)
NUMBER_OF_BEST_DRESSED = 5
NUMBER_OF_PRESENTERS = 26
BIGRAM_RE = "([A-Z][a-z]+\s[A-Z][-'a-zA-Z]+)"
BEST_DRESSED = []
presenter_tweet = []
PRESENTERS = []
HOSTS = []

remove_keywords = ["best", "picture", "actor", "actress", "hosts", "hosting", "drama", "golden", "globes",
                   "movie", "director", "song", "original", "foreign", "film", "tv", "series", "mini", "supporting",
                   "screenplay",
                   "presenting", "presented", "musical", "comedy", "motion", "animated", "feature", "win", "wins",
                   "winner", "won", "cecil",
                   "demille", "goldenglobes", "score", "miniseries", "award", "dressed", "dress", "b", "globe", "red",
                   "carpet", "annual",
                   "stars", "show", "new", "congrats"]

Nominees = dict()


def get_nominees(index):
    # urls must be in list, even though only one url
    urls = ["http://www.imdb.com/event/ev0000292/2013",
            "http://www.imdb.com/event/ev0000292/2015"]
    #get handler instance
    handler = GGPHandler()
    #get scraper instance with specific urls and handler
    scraper = Scraper(urls, handler)
    #result is a dict {'url': handler return}
    #print it out for more information
    result = scraper.fetch()
    #this is handle result that contains awards and nominees
    #you can iterate awards for eacha award and get related nominees
    global Nominees
    Nominees = result[urls[index]]


def create_useful_tweet_bank():
    word = ["winner", "wins", "hosts", "presenting", "won", "hosting", "dress", "dressed"]
    count = 0
    file = open("newfile.txt", "w")
    for t in tweet_text:
        temp = t.lower()
        for w in word:
            if (w in temp) and ("RT" not in t):
                new_tweets.append(t)
                token = re.sub(r'[^a-zA-Z0-9 ]', r'', t)
                file.write(token)
                file.write("\n")
                count += 1
    file.close()


def get_winners():
    result = {}
    for x in range(0, Num_of_Category, 1):
        name = find_winners(Award_Categories[x], Category_keywords[x])
        if name:
            result[Award_Categories[x]] = name
        else:
            result[Award_Categories[x]] = 'missing'
    return result


def get_fullName(word, category):
    # pdb.set_trace()
    for each in Nominees[category]:
        if each.lower().find(word) != -1:
            return each


def find_winners(category, keywords):
    new = []
    file = open("tempfile.txt", "w")
    temp_dict = dict()
    for twt in new_tweets:
        t = twt.lower()
        if ((keywords[0] in t) and (keywords[1] in t)):
            new.append(twt)
            tn = re.sub(r'[^a-zA-Z0-9 ]', r'', twt)
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
            file.write(final_sentence)
            file.write("\n")
    file.close()
    if temp_dict:
        abc = max(temp_dict, key=temp_dict.get)
        if (category != "Cecil B. DeMille Award"):
            abc = get_fullName(abc, category)
        return abc

def find_best_dressed():
    # This function will find the best dressed celebrities of the show.
    results = dict()
    for tweet in new_tweets:
        possible_winners = list()
        tt = tweet.lower()
        host_words = ["best dressed", "best dress"]
        tn = re.sub(r'[^a-zA-Z0-9 ]', r'', tweet)
        stopwords = nltk.corpus.stopwords.words('english')
        word_list = tn.split()
        res = ' '.join([i for i in word_list if i.lower() not in stopwords])
        for w in host_words:
            if w in tt:
                possible_winners = possible_winners + re.findall(BIGRAM_RE, res)
        for r in possible_winners:
            if r in results:
                results[r] += 1
            else:
                results[r] = 1
    results.pop("Golden Globes")
    results.pop("Best Dressed")
    i = 0

    for key in results:
        for w in remove_keywords:
            if (w in key.lower()):
                results[key] = 0

    best_dressed = list()
    while results and (i < NUMBER_OF_BEST_DRESSED):
        next = max(results, key=results.get);
        best_dressed.append(next);
        results.pop(next);
        i += 1
    return best_dressed


def find_worst_dressed(best_dressed):
    # This function will find the worst dressed celebrities of the show.
    results = dict()
    for tweet in new_tweets:
        possible_winners = list()
        tt = tweet.lower()
        host_words = ["worst dressed", "worst dress", "terrible"]
        tn = re.sub(r'[^a-zA-Z0-9 ]', r'', tweet)
        stopwords = nltk.corpus.stopwords.words('english')
        word_list = tn.split()
        res = ' '.join([i for i in word_list if i.lower() not in stopwords])
        for w in host_words:
            if w in tt:
                possible_winners = possible_winners + re.findall(BIGRAM_RE, res)
        for r in possible_winners:
            if r in results:
                results[r] += 1
            else:
                results[r] = 1
    results.pop("Golden Globes")
    results.pop("Worst Dressed")
    results.pop("Best Dressed")

    for key in results:
        for w in remove_keywords:
            if (w in key.lower()):
                results[key] = 0
    i = 0
    worst_dressed = list()
    while results and (i < NUMBER_OF_BEST_DRESSED):
        next = max(results, key=results.get);
        if (next not in best_dressed):
            worst_dressed.append(next);
            i += 1
        results.pop(next);
    return worst_dressed


def find_host():
    # This function will find the worst dressed celebrities of the show.
    results = dict()
    for tweet in new_tweets:
        possible_winners = list()
        tt = tweet.lower()
        host_words = ["host", "hosting", "hosts", "hosted"]
        for w in host_words:
            if w in tt:
                possible_winners = possible_winners + re.findall(BIGRAM_RE, tweet)
        for r in possible_winners:
            if r in results:
                results[r] += 1
            else:
                results[r] = 1
    results.pop("Golden Globes")
    i = 0
    host = list()
    while results and (i < 2):
        next = max(results, key=results.get);
        host.append(next)
        results.pop(next)
        i += 1
    return host


def find_presenters():
    # This function will find the presenters of the show.
    results = dict()
    stopwords = nltk.corpus.stopwords.words('english')
    for tweet in new_tweets:
        possible_winners = list()
        tt = tweet.lower()
        host_words = ["presenting", "presented"]
        tn = re.sub(r'[^a-zA-Z0-9 ]', r'', tweet)
        stopwords = nltk.corpus.stopwords.words('english')
        word_list = tn.split()
        res = ' '.join([i for i in word_list if i not in stopwords])
        for w in host_words:
            if w in tt:
                presenter_tweet.append(tn)
                possible_winners = possible_winners + re.findall(BIGRAM_RE, res)
        for r in possible_winners:
            if r in results:
                results[r] += 1
            else:
                results[r] = 1
    for key in results:
        for w in remove_keywords:
            if (w in key.lower()):
                results[key] = 0

    i = 0
    presenters = list()
    while results and (i < NUMBER_OF_PRESENTERS):
        next = max(results, key=results.get)
        presenters.append(next);
        results.pop(next);
        i += 1
    return presenters


def find_sentiments(type):
    # This function will find the presenters of the show.
    results = dict()
    stopwords = nltk.corpus.stopwords.words('english')
    for tweet in new_tweets:
        possible_winners = list()
        tt = tweet.lower()
        if type == "positive":
            host_words = ["i am so happy", "delighted", "deserves", "well deserved"]
        else:
            host_words = ["should have won", "cant believe"]
        tn = re.sub(r'[^a-zA-Z0-9 ]', r'', tweet)
        stopwords = nltk.corpus.stopwords.words('english')
        word_list = tn.split()
        res = ' '.join([i for i in word_list if i.lower() not in stopwords])
        for w in host_words:
            if w in tt:
                presenter_tweet.append(tn)
                possible_winners = possible_winners + re.findall(BIGRAM_RE, res)
        for r in possible_winners:
            if r in results:
                results[r] += 1
            else:
                results[r] = 1
    # results.pop("Golden Globes")
    for key in results:
        for w in remove_keywords:
            if (w in key.lower()):
                results[key] = 0

    i = 0
    sentiments = list()
    while results and (i < 10):
        next = max(results, key=results.get);
        sentiments.append(next);
        results.pop(next);
        i += 1
    return sentiments


def match_presenters(category,keywords,PRESENTERS):
    # This function will find the presenters of the show.
    results = dict()
    filter_tweets = []
    presenter_list = dict()
    stopwords = nltk.corpus.stopwords.words('english')
    for tweet in new_tweets:
        possible_winners = list()
        tt = tweet.lower()
        host_words = ["presents the", "presenting the"]
        tn = re.sub(r'[^a-zA-Z0-9 ]',r'',tweet)
        stopwords = nltk.corpus.stopwords.words('english')
        word_list = tn.split()
        res = ' '.join([i for i in word_list if i.lower() not in stopwords])
        for w in host_words:
            if w in tn.lower() and "RT" not in tn:
                filter_tweets.append(tn)
    for tw in filter_tweets:
        for name in PRESENTERS:
            if name in tw:
                for i in range(0,Num_of_Category,1):
                    if ((keywords[i][0] != "best"))and ((keywords[i][0] in tw.lower()) or (keywords[i][1] in tw.lower())):
                        if name in presenter_list:
                            continue
                        else:
                            presenter_list[name] = category[i]

    return presenter_list

Result = defaultdict(dict)
Result[2013] = defaultdict(dict)
Result[2015] = defaultdict(dict)


def loadsys(year):
    global Result
    loadfile(year)
    if year not in Result:
        Result[year] = {}
    Result[year]['hosts'] = find_host()
    Result[year]['winners'] = get_winners()
    Result[year]['presenters'] = find_presenters()
    Result[year]['bestdressed'] = find_best_dressed()
    Result[year]['worstdressed'] = find_worst_dressed(Result[year]['bestdressed'])
    Result[year]['positive'] = find_sentiments('positive')
    Result[year]['sympathy'] = find_sentiments('sympathy')
    Result[year]['match'] = match_presenters(Award_Categories, Category_keywords, Result[year]['presenters'])
    Result[year]['nominees'] = Nominees


def loadfile(year):
    global Award_Categories, tweet_text, Num_of_Category
    if year == 2013:
        get_nominees(0)
        Award_Categories = Award_Categories_13
        filename = 'gg2013.json'
    elif year == 2015:
        get_nominees(1)
        Award_Categories = Award_Categories_15
        filename = 'gg15mini.json'
    Num_of_Category = len(Award_Categories)
    with open(filename) as json_data:
        tweets = json.load(json_data)
    tweet_text = [tweet['text'] for tweet in tweets]
    create_useful_tweet_bank()


def main():
    create_useful_tweet_bank()
    print("\n\n********  HOSTS OF THE SHOW  ***************")
    hosts = find_host()
    for a in range(0, 2, 1):
        print(str(hosts[a]))
    print ("\n\n***************  WINNERS  *******************\n")
    winners = get_winners()
    for k, v in winners.iteritems():
        print(k + ': ' + v)
    presenter = find_presenters()
    print("\n\n***********  PRESENTERS LIST ************")
    for k in range(0, len(presenter), 1):
        print(str(presenter[k]))
    BEST_DRESSED = find_best_dressed()
    print("\n*************  FUN GOALS  *****************\n")
    print ("\n\n********  BEST DRESSED CELEBS  ************")
    for i in range(0, len(BEST_DRESSED), 1):
        print(str(BEST_DRESSED[i]))
    worst_dress = find_worst_dressed(BEST_DRESSED)
    print ("\n\n********   WORST DRESSED CELEBS   ***********")
    for j in range(0, len(worst_dress), 1):
        print(str(worst_dress[j]))
    print ("\n\n******* positive sentiments *********")
    sentiments = find_sentiments("positive")
    flag = 0
    for i in range(0, 5, 1):
        if sentiments[i] not in HOSTS:
            print(str(sentiments[i]))
        else:
            flag = 1
    if flag == 1:
        print (HOSTS[0] + " & " + HOSTS[1] + " did a great job hosting the Golden Globe awards!!!")

    print ("\n\n******** Should have won  ************")
    sentiments = find_sentiments("sympathy")
    for i in range(0, 5, 1):
        print(str(sentiments[i]))

    '''match = match_presenters(Award_Categories,Category_keywords,presenter)
    print ("\n\n********   test   ***********")
    for j in range(0,len(match),1):
        print(str(match[j]))'''


if __name__ == '__main__':
    loadfile(2013)
    main()