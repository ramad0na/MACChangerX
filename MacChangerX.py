RED = "\033[1;31m"
banner = r"""
 __  __             ____ _                               __  __
|  \/  | __ _  ___ / ___| |__   __ _ _ __   __ _  ___ _ _\ \/ /
| |\/| |/ _` |/ __| |   | '_ \ / _` | '_ \ / _` |/ _ \ '__\  /
| |  | | (_| | (__| |___| | | | (_| | | | | (_| |  __/ |  /  \
|_|  |_|\__,_|\___|\____|_| |_|\__,_|_| |_|\__, |\___|_| /_/\_\
                                           |___/      ramad0na
"""

print(RED + banner)

# Requesting the network interface name from the user (example: eth0 or wlan0)
network_interface = input("\033[1;33mEnter Network Interface: ")
print (network_interface)

# Requesting the user's new MAC address
mac_address = input("\033[1;33mEnter New Mac Address: ")
print (mac_address)

# Get all existing network interfaces using ifconfig
import subprocess
interfaces = subprocess.check_output("ifconfig", shell=True).decode()

# Verify whether the network interface inserted by the user is present or not
if network_interface + ":" not in interfaces:
    print("\033[1;31mError: Network interface" + " " +  network_interface + " " +  "not found!") 
    exit()

# Disable the network interface before changing the MAC address
subprocess.call("ifconfig " + network_interface + " down", shell=True)

# Change the MAC Address of the Network interface
subprocess.call("ifconfig " + network_interface + " hw ether " + mac_address, shell=True)

# Restart the network interface after the change
subprocess.call("ifconfig " + network_interface + " up", shell=True)

# Confirmation message: MAC Address change successfully
print("\033[1;39m[+] Changing MAC Address for " + network_interface + " to " + mac_address)

