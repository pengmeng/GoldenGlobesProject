__author__ = 'mengpeng'

import unittest
from unittest import TestCase
from ggp.tweet import Tweet


class TestTweet(TestCase):

    def setUp(self):
        self.sample = "{\"_id\": {\"$oid\": \"50f82aeab4aa879861000000\"}, \"text\" : \"Golden Globes, lots of fashion messes...but glad Argo won. Really good movie, along w Moonrise Kingdom and Salmon Fishing Yeman.\", \"created_at\" : { \"$date\" : 1358137508000 }, \"id\" : 290675893024747523, \"user\" : { \"screen_name\" : \"Dpharmakis23\", \"id\" : 852045842 }}"

    def test_clean(self):
        pass

    def test_str(self):
        tw = Tweet().fromstr(self.sample)
        for sign in [',', '.', '?', '!']:
            tw.text = tw.text.replace(sign, ' ')
        words = tw.text.split()
        print(words)