#!/usr/bin/python3
import random
import sys
import re

def process_log_line(line):
    """
    Process a single log line and return the status code and file size if the line matches the expected format.
    """
    # Regular expression to match the line format
    log_pattern = r'(\S+) - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
    
    match = re.match(log_pattern, line)
    if match:
        ip_address = match.group(1)
        status_code = int(match.group(2))
        file_size = int(match.group(3))
        return status_code, file_size
    return None, None

def print_statistics(total_size, status_codes_count):
    """
    Print the accumulated statistics: total file size and status code counts.
    """
    print(f"Total file size: {total_size}")
    for code in [200, 301, 400, 401, 403, 404, 405, 500]:
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def main():
    total_size = 0
    status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0
    
    try:
        # Read lines from stdin continuously
        for line in sys.stdin:
            # Process the current line
            status_code, file_size = process_log_line(line)
            
            # If the line is valid, accumulate the values
            if status_code and file_size:
                total_size += file_size
                if status_code in status_codes_count:
                    status_codes_count[status_code] += 1
                line_count += 1
            
            # Print statistics after every 10 valid lines
            if line_count % 10 == 0:
                print_statistics(total_size, status_codes_count)
                
    except KeyboardInterrupt:
        # Handle keyboard interrupt (CTRL + C)
        print_statistics(total_size, status_codes_count)

if __name__ == "__main__":
    main()
