from ipaddress import ip_network

for mask in range(33):
    net = ip_network(f'158.116.11.146/{mask}', False)
    print(net, net.netmask)
