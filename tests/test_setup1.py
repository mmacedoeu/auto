import unittest
import json
import os
import pathlib
from auto.setup_parser import import_vars, decode_live, decode_history

class Test1(unittest.TestCase):
    def test_parse_setup(self):
        base = pathlib.Path(__file__).parent.absolute()
        os.environ["SETUP_PATH"] = f'{base}/setup.conf'
        setup_dict = import_vars()
        stream_name = setup_dict['stream_name']
        stream_desc = setup_dict['stream_desc']
        livestream = setup_dict['livestream']
        history = setup_dict['history']
        assert stream_name is not None and stream_desc is not None and livestream is not None and history is not None

    def test_parse_setup_history(self):
        base = pathlib.Path(__file__).parent.absolute()
        os.environ["SETUP_PATH"] = f'{base}/setup.conf'
        history = decode_history()
        print(history)
        assert history is not None

    def test_parse_setup_live(self):
        base = pathlib.Path(__file__).parent.absolute()
        os.environ["SETUP_PATH"] = f'{base}/setup.conf'
        live = decode_live()
        print(live)
        assert live is not None

if __name__ == "__main__":
    unittest.main()