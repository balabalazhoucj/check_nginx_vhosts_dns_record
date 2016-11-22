#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import Socket
import sys


f = open(sys.argv[1],'rb')
for line in f:
    #time.sleep(1)
    #print line
    pattern = re.compile('server_name')
    if pattern.search(line.strip()):
        l = line.strip()
        record = re.split(' +|;',l)[1]
        length = '%' + str(30 - len(record)) + 's'
        print record + length %("=> ") + Socket.getaddrinfo(record, None)[0][4][0]
f.close()

