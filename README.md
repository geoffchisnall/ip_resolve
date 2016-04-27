# ip_resolve
Resolve dnsname/hostname of a given list of IPs
Only works on Windows.

Requirements: 
1) python2.7\n
2) nslookup\n
3) ping\n
4) Currently only works on windows as it uses the "ping -a" to resolve NETBIOS.\n

Add IPs into "iplist.txt" 
e.g
C:\code\ip_resolve>type iplist.txt
10.0.0.1
10.0.0.2
10.0.0.3


