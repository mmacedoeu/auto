import unittest
import os
import pathlib
import tempfile
from auto.diff import diff

class Test1(unittest.TestCase):
    def test_diff(self):
        base = pathlib.Path(__file__).parent.absolute()
        setup_file = tempfile.NamedTemporaryFile(prefix="setup_")
        print(setup_file.name)
        os.environ["SETUP_PATH"] = setup_file.name
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