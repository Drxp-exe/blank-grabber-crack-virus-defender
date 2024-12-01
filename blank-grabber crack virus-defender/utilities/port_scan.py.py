import socket

def scan_ports(target, port_range):
    print(f"Scanning {target}...")
    for port in port_range:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                if s.connect_ex((target, port)) == 0:
                    print(f"Port {port} is open.")
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

scan_ports("127.0.0.1", range(20, 1025))
