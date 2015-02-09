__author__ = 'mengpeng'

#First create a folder named tmp under crawler be like this ./crawler/tmp/
#Import scraper class and GGPHandler class
import pprint
from scraper import Scraper
from ggphandler import GGPHandler

if __name__ == '__main__':
    #urls must be in list, even though only one url
    urls = ["http://www.imdb.com/event/ev0000292/2013"]
    #get handler instance
    handler = GGPHandler()
    #get scraper instance with specific urls and handler
    scraper = Scraper(urls, handler)
    #result is a dict {'url': handler return}
    #print it out for more information
    result = scraper.fetch()
    pp = pprint.PrettyPrinter(indent=0)
    #pp.pprint(result)
    #this is handle result that contains awards and nominees
    #you can iterate awards for eacha award and get related nominees
    pp.pprint(result[urls[0]]['Awards'])