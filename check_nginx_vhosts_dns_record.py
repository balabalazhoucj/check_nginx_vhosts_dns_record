#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import socket
import sys


f = open(sys.argv[1],'rb')
sum = 0
print "Domain %31s" % "Record A"
print "."*50
for line in f:
    #time.sleep(1)
    #print line
    pattern = re.compile('server_name')
    if pattern.search(line.strip()):
        l = line.strip()
        domain = re.split(' +|;',l)[1]
        record = socket.getaddrinfo(domain, None)[0][4][0]
        length = '%' + str(30 - len(domain)) + 's'
        print domain + length %("=> ") + record
        sum += 1
f.close()
print 'Total: %d' % sum
