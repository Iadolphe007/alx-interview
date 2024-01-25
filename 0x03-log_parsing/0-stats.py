#!/usr/bin/python3
"""script that reads from stdin
and parses log files"""

import sys
import re

count = 10
increment = 0
totalSize = 0
codes = {}


def printStatistics(totalSize, codes):
    """prints out the statstics"""
    # print size
    print("File size: {}".format(totalSize))

    # print codes
    for code, value in sorted(codes.items()):
        if value > 0:
            print("{}: {}".format(code, value))


try:
    for index, line in enumerate(sys.stdin):
        index += 1
        s = r'(\S+) - \[([^]]+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
        match = re.match(s, line)
        if match:
            """get relevant data from the line"""
            ip_address, date, status_code, file_size = match.groups()
            totalSize += int(file_size)

            """count status codes of each line"""
            status_code = int(status_code)
            if status_code in codes:
                codes[status_code] += 1
            else:
                codes[status_code] = 1

            """check if index[9] i.e position 10, 20, 30... print statistics"""
            if index % 10 == 0:
                printStatistics(totalSize, codes)
except KeyboardInterrupt:
    pass
finally:
    printStatistics(totalSize, codes)