import unittest
import os
import pathlib

from auto.core import run

class Test1(unittest.TestCase):
    def test_diff(self):
        base = pathlib.Path(__file__).parent.absolute()
        os.environ["SETUP_PATH"] = f'{base}/setup_reg3.conf'
        os.environ["API_MOCK_PATH"] = f'{base}/auto_prov3.json'
        run()
        assert True        

if __name__ == "__main__":
    unittest.main()