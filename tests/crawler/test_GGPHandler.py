__author__ = 'mengpeng'

from unittest import TestCase
from ggp.crawler.ggphandler import GGPHandler
from ggp.crawler.scraper import Scraper


class TestGGPHandler(TestCase):
    def test_parse(self):
        urls = ["http://www.imdb.com/event/ev0000292/2013"]
        handler = GGPHandler()
        scraper = Scraper(urls, handler)
        print(scraper.fetch())