from bluetooth import *

def sdpBrowse(addr):

    services = find_service(address=addr)

    for service in services:
        name = service['name']
        proto = service['protocol']
        port = str(service['port'])
        print("[+] Found " + str(name) + " on " + str(proto) + ":" + port)

# Please insert MAC address of device in below sdpBrowse

sdpBrowse('B0:C5:59:32:79:D2')
