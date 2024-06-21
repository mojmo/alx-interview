#!/usr/bin/python3

import sys

# Initialize counters and storage
lines_count = 0
total_size = 0
stats = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def print_stats():
    """Print the accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(stats.keys()):
        if stats[code] > 0:
            print(f"{code}: {stats[code]}")


try:
    for line in sys.stdin:
        line = line.rstrip()
        parts = line.split()

        # Validate the line format
        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            total_size += file_size

            if status_code in stats:
                stats[status_code] += 1
        except Exception:
            pass

        lines_count += 1

        # Print stats after every 10 lines
        if lines_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass
finally:
    # Print stats upon exiting
    print_stats()
