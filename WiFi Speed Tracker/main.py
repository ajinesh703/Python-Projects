import psutil
import time

def get_wifi_interface():
    # List all network interfaces and pick the one that is up and wireless
    # This is a heuristic; adjust for your OS if needed.
    for iface, addrs in psutil.net_if_addrs().items():
        if "wi" in iface.lower() or "wlan" in iface.lower():
            return iface
    return None

def measure_wifi_data(interval=5):
    iface = get_wifi_interface()
    if not iface:
        print("No Wi-Fi interface found.")
        return

    io_start = psutil.net_io_counters(pernic=True)[iface]
    print(f"Monitoring interface: {iface}")
    print(f"Starting bytes sent: {io_start.bytes_sent}, received: {io_start.bytes_recv}")

    time.sleep(interval)

    io_end = psutil.net_io_counters(pernic=True)[iface]
    sent = io_end.bytes_sent - io_start.bytes_sent
    recv = io_end.bytes_recv - io_start.bytes_recv

    print(f"Data used in {interval} sec:")
    print(f"Uploaded: {sent / 1024:.2f} KB")
    print(f"Downloaded: {recv / 1024:.2f} KB")
    print(f"Total: {(sent + recv) / 1024:.2f} KB")

if __name__ == "__main__":
    measure_wifi_data(10)  # measure usage for 10 seconds
