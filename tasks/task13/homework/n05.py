from ipaddress import ip_network

for mask in range(33):
    net = ip_network(f'173.103.25.118/{mask}', False)
    print(net, net.netmask)
