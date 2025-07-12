import socket
from datetime import datetime

def scan_ports(target, start_port, end_port):
    print(f"\n🔎 Scanning {target} from port {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Short timeout for faster scanning
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"✅ Port {port} is OPEN")
            open_ports.append(port)
        sock.close()

    if not open_ports:
        print("❌ No open ports found in the specified range.")
    else:
        print(f"\n✅ Open ports: {open_ports}")

def main():
    print("🛠️ Simple Python Port Scanner")
    target = input("Enter target IP or hostname: ")
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("❌ Invalid hostname.")
        return

    try:
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
        if start_port < 0 or end_port > 65535 or start_port > end_port:
            raise ValueError
    except ValueError:
        print("❌ Invalid port range.")
        return

    start_time = datetime.now()
    scan_ports(target_ip, start_port, end_port)
    end_time = datetime.now()
    print(f"\n⏱️ Scan completed in: {end_time - start_time}")

if __name__ == "__main__":
    main()



