__author__ = 'mengpeng'

#First create a folder named tmp under crawler be like this ./crawler/tmp/
#Import scraper class and GGPHandler class
import pprint
from scraper import Scraper
from ggphandler import GGPHandler

if __name__ == '__main__':
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
    #this is handle result that contains awards and nominees
    #you can iterate awards for eacha award and get related nominees
    pprint.pprint(result[urls[0]])
    pprint.pprint(result[urls[1]])