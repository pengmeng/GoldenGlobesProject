__author__ = 'mengpeng'

from unittest import TestCase
from ggp.utils.log import withlogger
import unittest


@unittest.skip("succ")
class TestLog(TestCase):
    def test_withlogger(self):
        print('here')
        withlogger('ggp').info('test info massage')