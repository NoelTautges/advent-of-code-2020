#!/usr/bin/env python3

from math import ceil

def main():
    with open("13.txt") as bus_file:
        timestamp = int(bus_file.readline())
        buses = [int(num) for num in bus_file.readline().strip().split(",") if num != "x"]
    
    earliest_bus = -1
    best_minutes = timestamp

    for bus in buses:
        bus_caught = ceil(timestamp / bus) * bus
        minutes = bus_caught - timestamp

        if minutes < best_minutes:
            earliest_bus = bus
            best_minutes = minutes
    
    print(earliest_bus, "*", best_minutes, "=", earliest_bus * best_minutes)

if __name__ == "__main__":
    main()