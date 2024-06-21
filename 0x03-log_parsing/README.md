# 0x03. Log Parsing

This script reads log entries from standard input (stdin), parses them, and computes statistics on the status codes and total file size. The statistics are printed every 10 lines and upon exiting the script (including via keyboard interruption).

## How It Works

The script processes log entries with the following format:

```<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>```

It extracts and accumulates the total file size and counts of status codes. The status codes tracked are:
- 200
- 301
- 400
- 401
- 403
- 404
- 405
- 500

## Features

- Reads from standard input line by line.
- Accumulates the total file size.
- Counts occurrences of specified status codes.
- Prints statistics every 10 lines.
- Handles keyboard interruptions gracefully and prints final statistics before exiting.

## Usage

To use this script, you can pipe log generator to it. For example:

```bash
./0-generator.py | ./0-stats.py
```

## Example Output

```bash
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
```
