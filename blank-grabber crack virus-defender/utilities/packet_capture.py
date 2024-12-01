import socket

def packet_sniffer():
    try:
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        sniffer.bind(("127.0.0.1", 0))
        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        print("Sniffing packets...")
        while True:
            packet, _ = sniffer.recvfrom(65565)
            print(packet)
    except Exception as e:
        print(f"Error: {e}")

packet_sniffer()
