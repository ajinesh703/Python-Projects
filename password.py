import subprocess

def get_wifi_password(wifi_name):
    try:
        # Run the command to retrieve the Wi-Fi details
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi_name, 'key=clear'], text=True)

        # Look for the line containing the key (password)
        for line in result.split('\n'):
            if "Key Content" in line:
                # Extract the password from the line
                password = line.split(":")[1].strip()
                return f"Wi-Fi Name: {wifi_name}\nPassword: {password}"

        return f"No password found for Wi-Fi: {wifi_name}. It might be an open network."
    
    except subprocess.CalledProcessError:
        return f"Could not find Wi-Fi: {wifi_name}. Make sure it is a saved network."

# Example Usage
wifi_name = input("Enter the name of the Wi-Fi network: ")
print(get_wifi_password(wifi_name))
