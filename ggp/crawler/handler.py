__author__ = 'mengpeng'


class Handler(object):

    def __init__(self):
        pass

    def parse(self, html):
        self.save2file(html)
        return html

    def save2file(self, html):
        filename = "./tmp/" + str(hash(html) & 0xffffffff) + ".html"
        with open(filename, 'w') as outfile:
            outfile.write(html)
            outfile.flush()