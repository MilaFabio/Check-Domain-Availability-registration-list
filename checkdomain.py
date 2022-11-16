#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Thomas Roccia | Check domain availability
# pip install pywhois

import argparse
import whois
import signal
import sys
import datetime


my_domains = 'domains.txt'
my_path = 'result'

now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

result_filename = my_path + '/' + 'result_' + now + '.txt'


f = open(result_filename, 'w')
f.write('"Url"\n')
f.close()

# handle ctrl c
def signal_handler(sig, frame):
    print(' You pressed Ctrl+C!')
    sys.exit(0)

# check if domain exist
def whois_domain(domain):
    try:
        whois.whois(domain)
        print('\033[0m' + "[+] %s already exist!" % domain)
        return False
    except whois.parser.PywhoisError:
        print('\033[91m' + "[!] %s is available!" % domain)
        return True

# check domains from file
def check_list(filename):
    # получим объект файла
    fileResult = open(result_filename, 'a')

    domains = []
    with open(filename) as f:
        domains = f.readlines()

    for domain in domains:
        check_d = whois_domain(domain.strip())
        if check_d:
            # my_str = domain + '\n'
            fileResult.write(str(domain))

    fileResult.close()

# check single domain exist
def check_domain(domain):
    whois_domain(domain)


# main function
def main():
    # select arguments
    parser = argparse.ArgumentParser(description='checkDomain.py by Thomas Roccia')
    parser.add_argument("-d", "--domain", help="Check single domain", required=True)
    parser.add_argument("-f", "--file", help="Check domain list", required=True)
    args = parser.parse_args()

    # handle ctrl+c
    signal.signal(signal.SIGINT, signal_handler)

#     if args.domain:
#         check_domain(args.domain)
#
#     if args.file:
#         check_list(args.file)
#
#
# if __name__ == '__main__':
#     main()
# check_domain('remont-fotoapparatov-spb.ru/')

check_list(my_domains)
