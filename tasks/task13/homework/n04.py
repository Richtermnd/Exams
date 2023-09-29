from ipaddress import ip_network

for mask in range(33):
    net = ip_network(f'122.21.49.91/{mask}', False)
    print(net, net.netmask)
