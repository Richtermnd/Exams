from ipaddress import ip_network

for mask in range(33):
    net = ip_network(f'191.173.145.240/{mask}', False)
    print(net, net.num_addresses)
