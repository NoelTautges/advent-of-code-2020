#!/usr/bin/env python3

from collections import deque

def main():
    queue = deque([], 25)
    invalid = -1
    sum_queue = deque()
    cur_sum = 0
    
    with open("09.txt") as xmas_file:
        for line in xmas_file:
            num = int(line)

            if len(queue) < queue.maxlen \
                or any(val for val in queue if val * 2 != num and num - val in queue):
                queue.append(num)
            else:
                invalid = num
                print("Invalid number:", invalid)
                break
    
        xmas_file.seek(0)

        for line in xmas_file:
            num = int(line)

            if num > invalid:
                sum_queue.clear()
                continue
            
            while num + cur_sum > invalid:
                cur_sum -= sum_queue.popleft()
            
            sum_queue.append(num)
            cur_sum += num

            if cur_sum == invalid:
                print("Smallest + largest = ", min(sum_queue) + max(sum_queue))
                break

if __name__ == "__main__":
    main()