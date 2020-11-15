# import logging
# #clear reported errors
# logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
#
#import scapy
from scapy.all import *
from scapy.all import IP, ICMP, sr1, ARP
#
# def ping_one(dst_ip):
#     pingpkt = IP(dst=dst_ip)/ICMP(type=8)
#     rep = sr1(pingpkt, timeout=1)
#     print(rep.show())
#     print("{} bytes from {}: ttl={}".format(rep.len, rep.src, rep.ttl))
#
# def ping_five(dst_ip):
#     rep = []
#     for i in range(0, 5):
#         pkt = IP(dst=dst_ip)/ICMP(type=8)
#         rep += sr1(pkt, timeout=1, verbose = False)
#     for i in rep:
#         print("{} bytes from {}: ttl={}".format(i[IP].len, i[IP].src, i[IP].ttl))
#
#
# if __name__ == '__main__':
#     dst_ip = input("Please type dst IP: ")
#     ping_five(dst_ip)


def arp_pkt(dst_ip, src_ip, src_mac):
    arppkt = Ether(src=src_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(hwsrc=src_mac, psrc=src_ip, pdst=dst_ip)
    rep = srp1(arppkt, timeout=1, verbose= False)
    print("IP address {}'s MAC address is: {}".format(rep[ARP].psrc, rep[ARP].hwsrc))

if __name__ == '__main__':
    dst_ip = input("Input the IP address: ")
    src_ip = "192.168.0.5"
    src_mac = "38:f9:d3:36:e6:36"
    arp_pkt(dst_ip, src_ip, src_mac)