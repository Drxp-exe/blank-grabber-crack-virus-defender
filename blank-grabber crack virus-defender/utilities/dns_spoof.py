import socket

def dns_lookup(hostname):
    try:
        print(f"IP address of {hostname}: {socket.gethostbyname(hostname)}")
    except Exception as e:
        print(f"Error: {e}")

dns_lookup("example.com")
