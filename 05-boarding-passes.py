#!/usr/bin/env python3

from math import ceil

def get_location(binary, upper, upper_char):
    lower = 0
    
    for c in binary:
        adjust = ceil((upper - lower) / 2)

        if c == upper_char:
            lower += adjust
        else:
            upper -= adjust
    
    return lower

def main():
    max_id = 0

    with open("05.txt") as passes_file:
        for line in passes_file:
            if (seat_id := get_location(line[:7], 127, "B") * 8 \
                + get_location(line[7:10], 7, "R")) \
                > max_id:
                max_id = seat_id
    
    print(f"Max seat ID: {max_id}")

if __name__ == "__main__":
    main()