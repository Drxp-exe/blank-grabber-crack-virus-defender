import subprocess

def list_networks():
    print("Scanning for networks...")
    try:
        result = subprocess.run(["nmcli", "-t", "-f", "SSID,SECURITY", "dev", "wifi"], capture_output=True, text=True)
        for network in result.stdout.splitlines():
            print(network)
    except Exception as e:
        print(f"Error: {e}")

list_networks()
