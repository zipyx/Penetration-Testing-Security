import nmap
import optparse

def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print "[*]" + tgtHost + " tcp/" +tgtPort + " " + state
    
def main():

    parser = optparse.OptionParser('usage%prog ' + \
                                   '-H <target host> - p <target port>')
    parser.add_option('-H', dest='tgtHost',
