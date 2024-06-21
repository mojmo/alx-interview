#!/usr/bin/python3

import sys
import signal
import re

# Initialize counters and storage
lines_count = 0
total_size = 0
stats = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Regular expression to validate the input line format
validation_regex = (
    r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - "
    r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] "
    r"\"[A-Z]+\s+[^ ]+\s+HTTP\/\d\.\d\" \d{3} \d+$"
)


def print_stats():
    """Print the accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(stats.keys()):
        if stats[code] > 0:
            print(f"{code}: {stats[code]}")


def signal_handler(sig, frame):
    """Handle keyboard interrupt signal."""
    print_stats()
    sys.exit(0)


# Set up the signal handler for keyboard interrupt
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.rstrip()

        # Validate the line format
        if re.match(validation_regex, line):
            parts = line.split()
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            total_size += file_size

            if status_code in stats:
                stats[status_code] += 1

            lines_count += 1

            # Print stats after every 10 lines
            if lines_count % 10 == 0:
                print_stats()

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
finally:
    # Print stats upon exiting
    print_stats()
