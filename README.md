# ip_resolve
# version 1.0
Resolve dnsname/hostname of a given list of IPs
Only works on Windows.

Requirements:

1) python2.7

2) nslookup

3) ping

4) Currently only works on windows as it uses the "ping -a" to resolve NETBIOS.

Add IPs into "iplist.txt"

e.g

C:\code\ip_resolve>type iplist.txt

10.0.0.1

10.0.0.2

10.0.0.3
