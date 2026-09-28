import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port, open_ports):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            print(f"[OPEN] Port {port} ({service})")
            open_ports.append((port, service))

        s.close()

    except:
        pass


def main():
    target = input("Enter target IP: ")

    print(f"\nScanning {target}...\n")

    open_ports = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(1, 1025):
            executor.submit(scan_port, target, port, open_ports)

    print("\nScan Complete")
    print("Open Ports:", open_ports)

    # Save results
    with open("results.txt", "w") as f:
        for port, service in open_ports:
            f.write(f"{port} - {service}\n")


if __name__ == "__main__":
    main()
