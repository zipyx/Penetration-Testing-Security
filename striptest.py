import socket
import os
import sys

def connect(ip, port):
    try:
        socket.setdefaulttimeout(3)
        s = socket.socket()
        s.connect((port, ip))
        banner = s.recv(1024)
        return banner
    except:
        return


def checkvul(banner, filename):
    f = open('ViolentPythonBanner.txt', 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print "[+] Server is vulnerable: " + banner.strip('\n')
        print "[-] No vulnerable servers detected"
        print "[*] Re-Check Banner Server"

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print '[-] ' + filename + ' does not exist'
            exit(0)

            if not os.access(filename, os.R_OK):
                print '[-] Access denied.'
            exit(0)

        else:
            print '[-] Usage: ' + str(sys.argv[0]) + '<vuln filename>'
            exit(0)
            portList = [21, 22, 25, 80, 110, 443, 4444, 3000, 8080]
            for x in range(1, 255):
                ip = '192.168.1.' + str(x)
                for port in portList:
                    banner = connect(ip, port)
                    print ' [+] ' + ip + ': ' + banner
                    checkvul(banner, filename)

if __name__ == '__main__':
    main()
