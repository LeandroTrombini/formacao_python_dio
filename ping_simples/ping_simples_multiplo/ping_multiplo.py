import os 
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        os.system(f'ping -c 2 {ip}')
        time.sleep(5)