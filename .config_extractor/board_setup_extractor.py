#!/usr/bin/env python3
import paramiko
import string
import common_setup_parser
from os import path
from os import listdir
from os.path import isfile, join

class BoardSetupExtractor():
    def extract(self, targetIp, username="pi", password="raspberry"):

        cleanIP = targetIp.replace('.', '-')

        files = [f for f in listdir('output') if (isfile(join('output', f)) and (f.find(cleanIP) > -1))]
        if len(files) > 0:
            print(f'{targetIp} already processed.\n')
            return

        print(f'Connection to {targetIp}...')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(targetIp, 22, username, password)

        
        serialNumber = self.getSerialNumber(ssh)
        setup =  self.getSetup(ssh)

        del setup["history"]
        del setup["livestream"]
        streamName = setup.pop("stream_name")
        streamDesc = setup.pop("stream_desc")
        
        print('Generating output...')
        csvOutputFileName = f'output\\{streamName}__{streamDesc}__{cleanIP}__{serialNumber}.csv'
        with open(csvOutputFileName, 'w') as csv:
            csv.write("camera_name;awsStreamName;camera_address")
            for item in setup:
                awsStreamName = item.replace('cam', streamName)
                cameraAddress = setup[item].split('@').pop(1).split(':').pop(0)
                csv.write(f'\n{item};{awsStreamName};{cameraAddress}')
            
        
        print('Done!\n') 

        ssh.close()

    def getSerialNumber(self, ssh):
        # print("Getting device S/N...")
        _, stdout, _ = ssh.exec_command('cat /proc/cpuinfo | grep Serial')
        for line in stdout:
            serialNumber = line.strip('\n').split(':')[1].strip()
            # print(serialNumber)
        
        return serialNumber

    def getSetup(self, ssh):
        # print("Getting device setup...")
        _, stdout, _ = ssh.exec_command('cat ~/.apps/common/setup.conf')
        setupConf = []
        for line in stdout:
            setupConf.append(line.strip('\n'))

        return common_setup_parser.import_vars(setupConf)