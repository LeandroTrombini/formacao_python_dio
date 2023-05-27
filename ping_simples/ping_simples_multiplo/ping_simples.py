import os

print("#" * 60)

ip_or_hostname = input("Digite o Ip ou Host a ser verificado: ")

print("-" * 60)

os.system(f'ping -c 6 {ip_or_hostname}')

print("-" * 60)