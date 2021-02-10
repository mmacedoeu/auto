import unittest
import json
import auto
from auto.json_parser import decode_history, decode_movement

class Test1(unittest.TestCase):
    def test_parse_history(self):
        with open('./tests/auto_prov.json', 'r') as myfile:
            data=myfile.read()
            obj = json.loads(data)
            cameras_history = decode_history(obj)
            print(cameras_history)
            assert len(cameras_history) == 1

    def test_parse_movement(self):
        with open('./tests/auto_prov2.json', 'r') as myfile:
            data=myfile.read()
            obj = json.loads(data)
            cameras_movement = decode_movement(obj)
            print(cameras_movement)
            assert len(cameras_movement) >= 1            

if __name__ == "__main__":
    unittest.main()