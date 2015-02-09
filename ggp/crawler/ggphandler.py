__author__ = 'mengpeng'
import re
from handler import Handler


class GGPHandler(Handler):

    def __init__(self):
        super(GGPHandler, self).__init__()

    def parse(self, html):
        super(GGPHandler, self).save2file(html)
        awards_re = re.compile("<h2>Best.*</h2>")
        nominee_re = re.compile("(tt[0-9]*/\"\s>[A-Za-z0-9&#;\s]*<)")
        awardsraw = awards_re.findall(html)
        awards = [item[4:-5] for item in awardsraw]
        final = {'Awards': awards}
        for i in range(len(awards)):
            if i < len(awards) - 1:
                nees = nominee_re.findall(html, html.index(awards[i]), html.index(awards[i+1]))
            else:
                nees = nominee_re.findall(html, html.index(awards[i]))
            final[awards[i]] = [x[13:-1] for x in nees]
        return final