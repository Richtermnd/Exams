from ipaddress import ip_network

for mask in range(33):
    net = ip_network(f'154.201.208.17/{mask}', False)
    print(net, net.netmask)
