from ipaddress import ip_network

net = ip_network(f'0.0.0.0/255.255.240.0', False)
print(net.num_addresses)
