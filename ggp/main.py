__author__ = 'mengpeng'
from cli import CLI
import adapter
import json
"""
Main entrance of the project
"""


def createcli():
    maincli = CLI('Golden Globes Project')
    cli13 = CLI('Golden Globes 2013')
    cli15 = CLI('Golden Globes 2015')
    maincli.register('Load 2013 data', adapter.loadsys, 2013)
    maincli.register('Load 2015 data', adapter.loadsys, 2015)
    maincli.register('2013 Golden Globes', cli13.show)
    maincli.register('2015 Golden Globes', cli15.show)
    maincli.register('Generate json file', generatejsonfile)
    maincli.exitcomm('q')
    for each in cli13, cli15:
        year = 2013 if each is cli13 else 2015
        each.register('Hosts', adapter.print_hosts, year)
        each.register('Winners', adapter.print_winners, year)
        each.register('Presenters', adapter.print_presenters, year)
        each.register('Best Dressed', adapter.print_bestdressed, year)
        each.register('Worst Dressed', adapter.print_worstdressed, year)
        each.register('Positive Sentiment', adapter.print_positive, year)
        each.register('Sympathy Sentiment', adapter.print_sympathy, year)
        each.register('Matched Presenters', adapter.print_match, year)
        each.exitcomm('q')
    return maincli


def generatejsonfile():
    for each in 2013, 2015:
        with open('gg{0}answer.json'.format(each), 'w') as f:
            f.write(json.dumps(feedresult(each), indent=4, separators=(',', ': ')))


def feedresult(year):
    result = adapter.getResult()[year]
    rjson = {"metadata": {"year": year,
                          "names": {
                              "hosts": {"method": "detected",
                                        "method_description": "We first reduced the corpus of tweets by filtering by words such as 'hosted', 'hosts', 'hosting'. Then we found the proper nouns with the most frequency among those tweets and cross-checked them with our nominee list."},
                              "nominees": {"method": "scraped",
                                           "method_description": "We write a generic and scalable crawler framework to scrape data from web."},
                              "awards": {"method": "hardcoded",
                                         "method_description": ""},
                              "presenters": {"method": "detected",
                                             "method_description": "We reduced the corpus of tweets by filtering by words such as 'presented', 'presenting', 'presents'. Then we found the proper nouns with the most frequentcy among the tweets and returned them."}},
                          "mappings": {
                              "nominees": {
                                  "method": "scraped",
                                  "method_description": "We write a generic and scalable crawler framework to scrape data from web."},
                              "presenters": {
                                  "method": "detected",
                                  "method_description": "We used the same method as for identifying presenter names, however we also looked for the appearance of an award name."},
                              }
    },
             "data": {"unstructured": {"hosts": result['hosts'],
                                       "winners": [x for x in result['winners'].itervalues()],
                                       "awards": [x for x in result['winners'].iterkeys()],
                                       "presenters": result['presenters'],
                                       "nominees": [x for y in result['nominees'].itervalues() for x in y]},
                      "structured": {}}}
    for x in result['nominees'].iterkeys():
        rjson["data"]["structured"][x] = {"nominees": result["nominees"][x],
                                          "winners": result["winners"][x],
                                          "presenters": []}
    return rjson

if __name__ == '__main__':
    menu = createcli()
    menu.show()