#!/usr/bin/python3
"""
This script reads from stdin line by line and computes metrics.
"""
import sys


status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
code_count = {code: 0 for code in status_codes}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        data = line.split()
        try:
            """
            Extract status code and file size from line
            """
            status_code = int(data[-2])
            file_size = int(data[-1])
            """
            Update status code count and total file size
            """
            if status_code in status_codes:
                code_count[status_code] += 1
            total_size += file_size
        except:
            pass
        """
        Print statistics every 10 lines
        """
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code, count in sorted(code_count.items()):
                if count > 0:
                    print("{}: {}".format(code, count))
    """
    Print final statistics
    """
    print("File size: {}".format(total_size))
    for code, count in sorted(code_count.items()):
        if count > 0:
            print("{}: {}".format(code, count))
except KeyboardInterrupt:
    """
    Print statistics on keyboard interruption
    """
    print("File size: {}".format(total_size))
    for code, count in sorted(code_count.items()):
        if count > 0:
            print("{}: {}".format(code, count))
    raise
