__author__ = 'mengpeng'

import unittest
from unittest import TestCase
from ggp.tweet import Tweet
from ggp.utils.mongo_juice import MongoJuice


class TestTweet(TestCase):
    def setUp(self):
        self.sample = "{\"_id\": {\"$oid\": \"50f82aeab4aa879861000000\"}, \"text\" : \"Golden Globes, lots of fashion messes...but glad Argo won. Really good movie, along w Moonrise Kingdom and Salmon Fishing Yeman.\", \"created_at\" : { \"$date\" : 1358137508000 }, \"id\" : 290675893024747523, \"user\" : { \"screen_name\" : \"Dpharmakis23\", \"id\" : 852045842 }}"
        self.mongo = MongoJuice()

    def test_clean(self):
        pass

    @unittest.skip("succ")
    def test_str(self):
        tw = Tweet().fromstr(self.sample)
        for sign in [',', '.', '?', '!']:
            tw.text = tw.text.replace(sign, ' ')
        words = tw.text.split()
        print(words)

    @unittest.skip("succ")
    def test_tomongo(self):
        tw = Tweet.fromstr(self.sample)
        self.mongo.insert(tw.tomongo())
        self.assertEqual(4, self.mongo.count())

    @unittest.skip("succ")
    def test_frommongo(self):
        item = self.mongo.find({"_id": "50f82aeab4aa879861000000"})
        tw = Tweet.frommongo(item[0])
        print(tw)