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
        tw = Tweet()
        tw.text = item['text']
        tw.oid = item['_id']
        tw.id = item['id']
        tw.date = item['date']
        tw.user = (item['user_name'], item['user_id'])
        return tw

    def clean(self):
        pass

    def tomongo(self):
        item = {'_id': self.oid,
                'id': self.id,
                'text': self.text,
                'date': self.date,
                'user_name': self.user[0],
                'user_id': self.user[1]}
        return item

    def __str__(self):
        return "{" + "oid: {0}, id: {1}, text: {2}, date: {3}, user: {4}"\
            .format(self.oid, self.id, self.text, self.date, self.user) + "}"