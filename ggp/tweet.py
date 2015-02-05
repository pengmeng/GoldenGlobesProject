__author__ = 'mengpeng'
import json


class Tweet(object):

    def __init__(self):
        self.text = None
        self.oid = None
        self.id = None
        self.date = None
        self.user = None

    @staticmethod
    def fromstr(content):
        jsonobj = json.loads(content)
        tw = Tweet()
        tw.text = jsonobj['text']
        tw.oid = jsonobj['_id']['$oid']
        tw.id = jsonobj['id']
        tw.date = jsonobj['created_at']['$date']
        tw.user = (jsonobj['user']['screen_name'], jsonobj['user']['id'])
        return tw

    @staticmethod
    def frommongo(item):
        pass

    def clean(self):
        pass

    def tomongo(self):
        pass

    def __str__(self):
        return "id: {0} text: {1}".format(self.id, self.text)
