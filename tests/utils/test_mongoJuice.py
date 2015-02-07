__author__ = 'mengpeng'

from ggp.utils.mongo_juice import MongoJuice
from unittest import TestCase
import unittest

@unittest.skip("succ")
class TestMongoJuice(TestCase):

    def setUp(self):
        self.mongo = MongoJuice()

    def test_insert(self):
        item = {"_id": 1003, "name": "test _id"}
        self.mongo.insert(item)
        self.assertEqual(3, self.mongo.count())

    @unittest.skip("succ")
    def test_find(self):
        item = self.mongo.find()
        print(list(item))

    @unittest.skip("succ")
    def test_count(self):
        self.assertEqual(1, self.mongo.count())