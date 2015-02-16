__author__ = 'mengpeng'
import re
from handler import Handler


class GGPHandler(Handler):

    def __init__(self):
        super(GGPHandler, self).__init__()

    def parse(self, html):
        awards_re = re.compile("<h2>Best.*</h2>")
        awardsraw = awards_re.findall(html)
        awards = [item[4:-5] for item in awardsraw]
        final = {'Awards': awards}
        for i in range(len(awards)):
            start = html.index(awards[i])
            end = len(html) if i == len(awards) - 1 else html.index(awards[i + 1])
            final[awards[i]] = self.parsesec(html[start:end])
        return final

    def parsesec(self, sec):
        movie_re = re.compile("(tt[0-9]*/\"\s>[A-Za-z0-9&#;\s\-\.]*<)")
        name_re = re.compile("(nm[0-9]*/\"\s>[A-Za-z0-9&#;\s\-\.]*<)")
        movies = movie_re.findall(sec)
        movies = [x[13:-1] for x in movies]
        for i in range(len(movies)):
            start = sec.index(movies[i])
            end = len(sec) if i == len(movies) - 1 else sec.index(movies[i + 1])
            names = name_re.findall(sec, start, end)
            if names:
                names = [x[13:-1] for x in names]
                movies[i] += ': ' + ', '.join(names)
        return movies