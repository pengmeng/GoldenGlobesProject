__author__ = 'mengpeng'
from cli import CLI
import adapter
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
        each.exitcomm('q')
    return maincli


def generatejsonfile():
    pass


def feedresult(year):
    result = adapter.getResult()
    rjson = {"metadata": {"year": year,
                          "hosts": {"method": "detected",
                                    "method_description": ""},
                          "nominees": {"method": "scraped",
                                       "method_description": ""},
                          "awards": {"method": "hardcoded",
                                     "method_description": ""
                          },
                          "presenters": {
                              "method": "detected",
                              "method_description": ""
                          }},
             "data": {"unstructured": {"hosts": result[year]['hosts'],
                                       "winners": [x for x in result[year]['winners'].itervalues()],
                                       "awards": [x for x in result[year]['winners'].iterkeys()],
                                       "presenters": result[year]['presenters'],
                                       "nominees": []},
                      "structured": {}}}


if __name__ == '__main__':
    menu = createcli()
    try:
        menu.show()
    except KeyError and TypeError:
        print('Please load data first!')
        menu.show()