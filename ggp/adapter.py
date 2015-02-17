__author__ = 'mengpeng'
import digest


def loadsys(year):
    print('Loading {0} data...'.format(year))
    digest.loadsys(year)
    print('Done!')


def getResult():
    return digest.Result


def print_hosts(year):
    print("\n\n***************  HOSTS OF THE SHOW  ***************\n")
    _printer(digest.Result[year]['hosts'][0:2])


def print_winners(year):
    print ("\n\n***************  WINNERS  ***************\n")
    winners = digest.Result[year]['winners']
    for k, v in winners.iteritems():
        print(k + ': ' + v)


def print_presenters(year):
    print("\n\n***************  PRESENTERS LIST ***************\n")
    _printer(digest.Result[year]['presenters'])


def print_bestdressed(year):
    print("\n\n***************  BEST DRESSED CELEBS ***************\n")
    _printer(digest.Result[year]['bestdressed'])


def print_worstdressed(year):
    print("\n\n***************  WORST DRESSED CELEBS ***************\n")
    _printer(digest.Result[year]['worstdressed'])


def print_positive(year):
    print("\n\n***************  Positive Sentiments ***************\n")
    _printer(digest.Result[year]['positive'][0:5])


def print_sympathy(year):
    print("\n\n***************  Honorable Mention (Should Have Won) ***************\n")
    _printer(digest.Result[year]['sympathy'][0:5])


def print_match(year):
    print("\n\n***************  Matched Presenters ***************\n")
    match = digest.Result[year]['match']
    for k, v in match.iteritems():
        print(k + ' presented the award for ' + v)


def _printer(obj):
    for each in obj:
        print(each)