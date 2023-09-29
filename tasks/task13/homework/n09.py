from ipaddress import ip_network

for mask in range(33):
    net1 = ip_network(f'165.112.200.70/{mask}', False)
    net2 = ip_network(f'165.112.175.80/{mask}', False)
    if net1 == net2:
        print(net1)
