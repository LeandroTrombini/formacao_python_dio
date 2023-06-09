import ipaddress

ip = '192.168.0.1'
ip2 = '192.168.0.0/24'

address = ipaddress.ip_address(ip)
network = ipaddress.ip_network(ip2)

print(address + 257)
print(network)