import os
import sys
import unittest

try:
    sys.path.append('../src')
    import sanji
except ImportError as e:
    print "Please check the python PATH for import test module."
    exit(1)

import paho.mqtt.client as mqtt

class Model(sanji.Sanji):
    
    def init(self):
        print "init"
        self.router.route("/model/:id")
            .get(self.get)
            .post(self.post)

    def get(self, request, response):
        print request

    def post(self, request, response):
        print request


class TestSanjiClass(unittest.TestCase):
    def setUp(self):
        self.model = Model()

    def tearDown(self):
        pass

    def test_init(self):
        self.model.run()


if __name__ == "__main__":
    unittest.main()
