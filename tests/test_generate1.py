import unittest
import json
import os
import tempfile
from auto.generate import generate_setup_conf

class Test1(unittest.TestCase):
    def test_generate1(self):
        setup_file = tempfile.NamedTemporaryFile(prefix='setup_')
        print(setup_file.name)
        os.environ["SETUP_PATH"] = setup_file.name
        history = [{'id': 123, 'networkAddress': '172.17.1.5', 'streamName': '00001_1', 'services': [{'type': 'LIVE', 'enabled': False}, {'type': 'HISTORY', 'enabled': True}]}]
        live = [{'id': 124, 'networkAddress': '172.17.1.3', 'streamName': '00001_2', 'services': [{'type': 'LIVE', 'enabled': True}, {'type': 'HISTORY', 'enabled': False}]}]
        movement = [{'id': 125, 'networkAddress': '172.17.1.6', 'streamName': '00001_3', 'services': [{'type': 'LIVE', 'enabled': False}, {'type': 'HISTORY', 'enabled': False}]}]
        tag = "00001_desc"
        generate_setup_conf(history, live, movement, tag)
        assert True

if __name__ == "__main__":
    unittest.main()