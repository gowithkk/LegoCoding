from scapy.all import IP, ICMP, sr1

def arp_pkt(dst_ip, src_ip, src_mac):
    arppkt = Ether(src=src_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(hwsrc=src_mac, psrc=src_ip, pdst=dst_ip)
    rep = srp1(arppkt, verbose=False)
    print("IP address {}'s MAC address is: {}".format(rep[ARP].psrc, rep[ARP].hwsrc))

if __name__ == '__main__':
    dst_ip = input("Input the IP address: ")
    src_ip = "192.168.100.5"
    src_mac = "C8:5B:76:50:50:9A"
    arp_pkt(dst_ip, src_ip, src_mac)