import unittest
import json
from auto.sync import sync

class Test1(unittest.TestCase):
    def test_sync(self):
        data = sync()
        assert data is not None

if __name__ == "__main__":
    unittest.main()