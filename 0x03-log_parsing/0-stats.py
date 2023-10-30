#!/usr/bin/env python3
"""reads stdin line by line and compute metrics"""
import sys
# file size check, status_code count, status code arranged in ascending order


def main_log():
    """compute stats in each line"""
    file_size_total = 0
    line_count = 0
    status_code_dict = {}
    total = 0
    try:
        for line in sys.stdin:
            line = line.split(' ')
            line_count += 1
            file_size = line[len(line)-1]
            status_code = line[len(line)-2]
            if status_code in status_code_dict:
                status_code_dict[status_code] += 1
            else:
                status_code_dict[status_code] = 1
            file_size_total += int(file_size)
            if line_count % 10 == 0:
                total += file_size_total
                print(f"File size: {total}")
                for k, v in sorted(status_code_dict.items()):
                    print(f"{k}: {v}")
                status_code_dict.clear()
                file_size_total = 0
    except KeyboardInterrupt:
        print(f"File size: {file_size_total}")
        for k, v in sorted(status_code_dict.items()):
            print(f"{k}: {v}")


if __name__ == '__main__':
    main_log()
