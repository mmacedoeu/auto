from subprocess import Popen, PIPE, STDOUT
import time

uma_hora = 3600

def run():
    while True:
        proc = start()
        time.sleep(uma_hora)
        
def start():
    cmd = ['/usr/bin/python3', '-m', 'auto.Main']
    return Popen(cmd, stdout=PIPE, stderr=STDOUT)

if __name__ == "__main__":
    run()