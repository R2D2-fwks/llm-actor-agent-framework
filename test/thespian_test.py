import socket
import sys

def test_hostname_resolution(hostname):
    """Test if a hostname can be resolved"""
    print(f"Attempting to resolve hostname: {hostname}")
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"Success! Resolved {hostname} to IP: {ip_address}")
        return True
    except socket.gaierror as e:
        print(f"Error: {e}")
        return False
        
def fix_hosts_entry(hostname, ip_address="127.0.0.1"):
    """Suggest command to fix hosts file entry"""
    print(f"\nTo fix this issue, you can add the following line to your /etc/hosts file:")
    print(f"{ip_address} {hostname}")
    print("\nOn Linux/Mac, use:")
    print(f"sudo echo '{ip_address} {hostname}' >> /etc/hosts")
    print("\nOn Windows, edit C:\\Windows\\System32\\drivers\\etc\\hosts as administrator")

if __name__ == "__main__":
    hostname = "EPINBANW023F"
    if len(sys.argv) > 1:
        hostname = sys.argv[1]
    
    success = test_hostname_resolution(hostname)
    
    if not success:
        fix_hosts_entry(hostname)
        print("\nAlternatively, in your Thespian code, you can modify the configuration to use:")
        print("- IP address directly instead of hostname")
        print("- 'localhost' or '127.0.0.1' for local testing")
