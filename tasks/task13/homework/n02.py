from ipaddress import ip_network

for mask in range(33):
    net = ip_network(f'118.193.30.139/{mask}', False)
    print(net, net.netmask)
