import time
from bluetooth import *

alreadyFound = []


def findDevs():
    foundDevs = discover_devices(lookup_names=True)
    for (addr, name) in foundDevs:
        if addr not in alreadyFound:
            print("[+] Found Bluetooth Device: " + str(name))
            print("[+] MAC Address: " + str(addr))
            alreadyFound.append(addr)

while True:
    findDevs()
    time.sleep(5)

"""
devList = discover_devices()
for device in devList:
    name = str(lookup_name(device))
    print("[+] Found Bluetooth Device: " + str(name))
    print("[+] MAC Address: " + str(device))
    
"""
