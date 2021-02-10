import docker
import os

base_url='unix://var/run/docker.sock'

def get_config_path_name():
    return os.getenv('DOCKER_PATH', base_url)  

def restart(name):
    client = docker.DockerClient(base_url=get_config_path_name())
    #client = docker.from_env()
    for c in client.containers.list():
        if name in c.image.tags[0]:
            c.restart()
            break
    # container = client.containers.get(name)