import scapy.all as scapy

def sniff_packets(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
    if packet.haslayer(scapy.IP):
        source_ip = packet[scapy.IP].src
        destination_ip = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto
        
        if packet.haslayer(scapy.TCP):
            protocol = "TCP"
            source_port = packet[scapy.TCP].sport
            destination_port = packet[scapy.TCP].dport
            print(f"[+] {source_ip}:{source_port} --> {destination_ip}:{destination_port} [TCP]")

            if packet.haslayer(scapy.Raw):
                payload = packet[scapy.Raw].load.decode("utf-8", errors='ignore')
                print(f"    Payload: {payload}")

        elif packet.haslayer(scapy.UDP):
            protocol = "UDP"
            source_port = packet[scapy.UDP].sport
            destination_port = packet[scapy.UDP].dport
            print(f"[+] {source_ip}:{source_port} --> {destination_ip}:{destination_port} [UDP]")

            if packet.haslayer(scapy.Raw):
                payload = packet[scapy.Raw].load.decode("utf-8", errors='ignore')
                print(f"    Payload: {payload}")

        else:
            print(f"[+] {source_ip} --> {destination_ip} [Protocol: {protocol}]")

def main():
    interface = input("[*] Enter interface to sniff on (e.g., Wi-Fi): ")
    print("[*] Starting packet sniffer...")
    sniff_packets(interface)

if __name__ == "__main__":
    main()
