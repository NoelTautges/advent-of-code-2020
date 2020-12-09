#!/usr/bin/env python3

from collections import deque

def main():
    queue = deque([], 25)
    
    with open("09.txt") as xmas_file:
        for line in xmas_file:
            num = int(line)

            if len(queue) < queue.maxlen \
                or any(val for val in queue if val * 2 != num and num - val in queue):
                queue.append(num)
            else:
                print("Odd number out:", num)
                break

if __name__ == "__main__":
    main()