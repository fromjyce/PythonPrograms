from scapy.all import *

class Firewall:
    def __init__(self, packet_file, inbound_blocked_ports, inbound_blocked_protocols, inbound_blocked_ips, inbound_allowed_ports, outbound_blocked_ports, outbound_blocked_protocols, outbound_blocked_ips, outbound_allowed_ports, outbound_blocked_domains):
        self.packet_file = packet_file
        self.inbound_blocked_ports = inbound_blocked_ports
        self.inbound_blocked_protocols = inbound_blocked_protocols
        self.inbound_blocked_ips = inbound_blocked_ips
        self.inbound_allowed_ports = inbound_allowed_ports
        self.outbound_blocked_ports = outbound_blocked_ports
        self.outbound_blocked_protocols = outbound_blocked_protocols
        self.outbound_blocked_ips = outbound_blocked_ips
        self.outbound_allowed_ports = outbound_allowed_ports
        self.outbound_blocked_domains = outbound_blocked_domains

    def apply_inbound_rules(self, packet):
        if TCP in packet and packet[TCP].dport in self.inbound_blocked_ports:
            print(f"Blocked inbound packet (TCP port {packet[TCP].dport}):", packet.summary())
            return True
        
        for protocol in self.inbound_blocked_protocols:
            if protocol in packet:
                print("Blocked inbound packet ({})".format(protocol.name), packet.summary())
                return True
        
        if IP in packet and packet[IP].src in self.inbound_blocked_ips:
            print("Blocked inbound packet (Blocked IP):", packet.summary())
            return True
        
        if TCP in packet and packet[TCP].dport in self.inbound_allowed_ports:
            print("Allowed inbound packet:", packet.summary())
            return False
        
        print("Packet didn't match any inbound rules:", packet.summary())
        
        print("Blocked inbound packet (Default):", packet.summary())
        return True

    def apply_outbound_rules(self, packet):
        if TCP in packet and packet[TCP].sport in self.outbound_blocked_ports:
            print("Blocked outbound packet (TCP port {packet[TCP].dport}):", packet.summary())
            return True
        
        if UDP in packet:
            print("Blocked outbound packet (UDP):", packet.summary())
            return True
        
        for protocol in self.outbound_blocked_protocols:
            if protocol in packet:
                print("Blocked outbound packet ({})".format(protocol.name), packet.summary())
                return True
        
        if IP in packet and packet[IP].dst in self.outbound_blocked_ips:
            print("Blocked outbound packet (Blocked IP):", packet.summary())
            return True
        
        if UDP in packet and packet[UDP].dport in self.outbound_allowed_ports:
            print("Allowed outbound packet:", packet.summary())
            return False
        
        if DNS in packet and packet[DNS].qd.qname.decode().strip('.') in self.outbound_blocked_domains:
            print("Blocked outbound packet (Blocked Domain):", packet.summary())
            return True
        
        print("Outbound packet did not match any rules:", packet.summary())
        return False

    def process_packet(self, packet):
        if IP in packet:
            if packet[IP].src == "192.168.1.150":
                is_blocked = self.apply_outbound_rules(packet)
            else:
                is_blocked = self.apply_inbound_rules(packet)
        else:
            print("Non-IP packet:", packet.summary())

    def main(self):
        packets = rdpcap(self.packet_file)
        for packet in packets:
            self.process_packet(packet)

inbound_blocked_ports = [22, 23]
inbound_blocked_protocols = [ICMP, TCP, UDP]
inbound_blocked_ips = ["192.168.1.100"]
inbound_allowed_ports = [80, 443]

outbound_blocked_ports = [25]
outbound_blocked_protocols = [UDP]
outbound_blocked_ips = ["10.0.0.1"]
outbound_allowed_ports = [53]
outbound_blocked_domains = ["youtube.com"]

packet_file = 'data.pcapng'
firewall = Firewall(packet_file, inbound_blocked_ports, inbound_blocked_protocols, inbound_blocked_ips, inbound_allowed_ports, outbound_blocked_ports, outbound_blocked_protocols, outbound_blocked_ips, outbound_allowed_ports, outbound_blocked_domains)
firewall.main()
