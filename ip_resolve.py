#IP_RESOLVE
#Version 1.0
#Author: Geoffrey Chisnall
#2016

import os,sys,subprocess

iplist = "iplist.txt"
 
ipfile = open(iplist,'rb')
lines = ipfile.readlines()
ipfile.close()


dnsresults = open('ips_resolved.txt','w')
for ip in lines:
    pingoutput="ping -a -n 1 %s" % (ip)
    try:
        pingresult = subprocess.check_output(pingoutput, shell=True)
        hostname = pingresult.split()[1]
        print ip.strip(), hostname, "ping"
        dnsresults.write("%s %s\n" % (ip.strip(),hostname))
                
    
    except:
        nslookup="nslookup %s" % (ip)
        nslookupoutput = subprocess.check_output(nslookup, shell=True)
        nslookupresult = nslookupoutput.strip()
                
        if 'Name' in nslookupresult:
            nslookuphostname = nslookupresult.split()[5]
            print ip.strip(), nslookuphostname, "nslookup_name"
            dnsresults.write("%s %s\n" % (ip.strip(),nslookuphostname.strip()))
        else:
            nslookupodd = ip.strip(), "noDNS, nslookup_error"
            if '' in nslookupodd:
                print "EMPTY", "EMPTY", "nslookup_blank"
                dnsresults.write("EMPTY EMPTY\n")
            else:
                print ip.strip(), "noDNS, nslookup_noDNS"
                dnsresults.write("%s noDNS\n" % (ip.strip()))
                
dnsresults.close()
