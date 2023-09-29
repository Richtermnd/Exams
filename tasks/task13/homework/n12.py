from ipaddress import ip_network

net = ip_network('10.48.96.0/255.255.240.0', False)

cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip.count('1') > ip.count('0'):
        cnt += 1
print(cnt)