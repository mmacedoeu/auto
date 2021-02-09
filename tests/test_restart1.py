import unittest
import docker
import os
from auto.restart import restart

base_url='/var/run/docker.sock'

def get_config_path_name():
    return os.getenv('DOCKER_PATH', base_url)  

class Test1(unittest.TestCase):
    def test_restart(self):
        # client = docker.APIClient(base_url=get_config_path_name())
        client = docker.from_env()
        container = client.containers.run("nginxdemos/hello:plain-text",
                                      detach=True)
        container.reload()
        name = container.name
        restart(name)
        container.reload()
        container.stop()       
        assert True

    # def test_diff(self):
    #     local = {'cam_0': 'rtsp://admin:guardep0rn0s@172.17.1.5:554/ch01/0', 'cam_1': 'rtsp://admin:guardep0rn0s@172.17.1.13:554/ch01/0'}
    #     server = [{'id': 123, 'networkAddress': '172.17.1.5', 'streamName': '00001_1', 'services': [{'type': 'LIVE', 'enabled': False}, {'type': 'HISTORY', 'enabled': True}]},{'id': 124, 'networkAddress': '172.17.1.3', 'streamName': '00001_2', 'services': [{'type': 'LIVE', 'enabled': False}, {'type': 'HISTORY', 'enabled': True}]}]
    #     changed = diff(server, local)
    #     assert changed        

if __name__ == "__main__":
    unittest.main()