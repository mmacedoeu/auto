import unittest
import os
import pathlib
from auto.diff import diff

class Test1(unittest.TestCase):
    def test_diff(self):
        base = pathlib.Path(__file__).parent.absolute()
        os.environ["SETUP_PATH"] = f'{base}/setup2.conf'
        os.environ["API_MOCK_PATH"] = f'{base}/auto_prov2.json'
        (
            change_history,
            change_live,
            change_alarm,
            server_history,
            server_live,
            server_alarm,
            server_tag,
        ) = diff()
        assert change_alarm        

if __name__ == "__main__":
    unittest.main()