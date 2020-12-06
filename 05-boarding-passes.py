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
    seats = [[False] * 8 for _ in range(128)]

    with open("05.txt") as passes_file:
        for line in passes_file:
            row = get_location(line[:7], 127, "B")
            col = get_location(line[7:10], 7, "R")
            seats[row][col] = True

            if (seat_id := row * 8 + col) > max_id:
                max_id = seat_id
    
    print(f"Max seat ID: {max_id}")

    for row, row_seats in enumerate(seats):
        for col in range(6):
            if row_seats[col] and not row_seats[col + 1] and row_seats[col + 2]:
                print(f"My seat ID: {row * 8 + col + 1}")
                break
        else:
            continue

        break

if __name__ == "__main__":
    main()