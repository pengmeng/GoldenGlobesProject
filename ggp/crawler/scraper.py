__author__ = 'mengpeng'
import urllib
from handler import Handler


class Scraper(object):

    def __init__(self, urls, handler=None):
        self._urls = urls
        self._handler = handler

    @property
    def urls(self):
        return self._urls

    @urls.setter
    def urls(self, value):
        self._urls = value

    @property
    def handler(self):
        return self._handler

    @handler.setter
    def handler(self, value):
        self._handler = value

    def fetch(self):
        result = {}
        for url in self._urls:
            html = urllib.urlopen(url).read()
            result[url] = self._handler.parse(html)
        return result

if __name__ == '__main__':
    urls = ["http://www.imdb.com/event/ev0000292/2013"]
    hd = Handler()
    sp = Scraper(urls, hd)
    r = sp.fetch()
    print(urls)