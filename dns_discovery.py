#!/usr/bin/env python3

import sys
import socket

def resolve_hostname(hostname):
    try:
        socket.gethostbyname(hostname)
    except socket.gaierror:
        return False
    except Exception as e:
        print('[FATAL] error processing hostname {}'.format(hostname))
        print(e)
    return True

if(__name__ == '__main__'):
    if len(sys.argv) < 2:
        print("""[ERROR] usage: dns_discovery.py <domain> (<wordlist>)
example: dns_discovery.py mydomain.com list.csv""")
        sys.exit()
    elif len(sys.argv) == 2:
        print('[*] using default list: default_subdomains.csv')
        subs = open('default_subdomains.csv', 'r').read().split(',')
    else:
        print('[*] reading subdomains from provided list {}'.format(sys.argv[2]))
        subs = open(sys.argv[2], 'r').read().split(',')

    for sub in subs:
        full_hostname = sub.strip() + '.' + sys.argv[1].strip()
        if(resolve_hostname(full_hostname)):
            print(full_hostname)
