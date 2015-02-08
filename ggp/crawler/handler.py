__author__ = 'mengpeng'


class Handler(object):

    def __init__(self):
        pass

    def parse(self, html):
        with open("sample.html", 'w') as outfile:
            outfile.write(html)
        return html