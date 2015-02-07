__author__ = 'mengpeng'

import pymongo


class MongoJuice(object):

    client = pymongo.MongoClient('localhost', 27017)

    def __init__(self, db_name='gg', coll_name='test'):
        self._db_name = db_name
        self._coll_name = coll_name
        self._db = MongoJuice.client[db_name]
        self._coll = self.db[coll_name]

    @property
    def db_name(self):
        return self._db_name

    @property
    def coll_name(self):
        return self._coll_name

    @property
    def db(self):
        return self._db

    @db.setter
    def db(self, value):
        self._db_name = value
        self._db = MongoJuice.client[self._db_name]

    @property
    def coll(self):
        return self._coll

    @coll.setter
    def coll(self, value):
        self._coll_name = value
        self._coll = self._db[value]

    def insert(self, items):
        self._coll.insert(items)

    def find(self, query=None, limit=0, sort=None, skip=0):
        return self._coll.find(spec=query, limit=limit, sort=sort, skip=skip)

    def count(self):
        return self._coll.count()