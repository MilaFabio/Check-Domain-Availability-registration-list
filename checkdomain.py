#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Thomas Roccia | Check domain availability
# pip install pywhois
#

import argparse
import whois
import signal
import sys
import datetime

my_domains = 'domains.txt'
my_path = 'result'

now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

result_filename = my_path + '/' + 'result_' + now + '.txt'
# result_test = my_path + '/' + 'test_' + now + '.txt'


f = open(result_filename, 'w')
f.write('"Url"\n')
f.close()

# testResult = open(result_test, 'a')


# check if domain exist
def whois_domain(domain):
    try:
        whois.whois(domain)
        # testResult.write(str(domain)+"\n")
        print('\033[0m' + "[+] %s already exist!" % domain)
        return False
    except whois.parser.PywhoisError:
        # testResult.write(str(domain)+"\n")
        print('\033[91m' + "[!] %s СВОБОДЕН!" % domain)
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
            fileResult.write(str(domain))

    fileResult.close()
    # testResult.close()

# check single domain exist
def check_domain(domain):
    whois_domain(domain)


check_list(my_domains)
