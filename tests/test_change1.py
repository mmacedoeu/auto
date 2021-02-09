import unittest
from auto.diff import has_changed

class Test1(unittest.TestCase):
    def test_diff_changed(self):
        local = {'cam_0': 'rtsp://admin:guardep0rn0s@172.17.1.5:554/ch01/0', 'cam_1': 'rtsp://admin:guardep0rn0s@172.17.1.13:554/ch01/0'}
        server = [{'id': 123, 'networkAddress': '172.17.1.5', 'streamName': '00001_1', 'services': [{'type': 'LIVE', 'enabled': False}, {'type': 'HISTORY', 'enabled': True}]},{'id': 124, 'networkAddress': '172.17.1.3', 'streamName': '00001_2', 'services': [{'type': 'LIVE', 'enabled': False}, {'type': 'HISTORY', 'enabled': True}]}]
        changed = has_changed(server, local)
        assert changed

    # def test_diff(self):
    #     local = {'cam_0': 'rtsp://admin:guardep0rn0s@172.17.1.5:554/ch01/0', 'cam_1': 'rtsp://admin:guardep0rn0s@172.17.1.13:554/ch01/0'}
    #     server = [{'id': 123, 'networkAddress': '172.17.1.5', 'streamName': '00001_1', 'services': [{'type': 'LIVE', 'enabled': False}, {'type': 'HISTORY', 'enabled': True}]},{'id': 124, 'networkAddress': '172.17.1.3', 'streamName': '00001_2', 'services': [{'type': 'LIVE', 'enabled': False}, {'type': 'HISTORY', 'enabled': True}]}]
    #     changed = diff(server, local)
    #     assert changed        

if __name__ == "__main__":
    unittest.main()