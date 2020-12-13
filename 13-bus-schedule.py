#!/usr/bin/env python3

from functools import reduce
from math import ceil, gcd

def multiply(nums):
    return reduce(lambda a, b: a * b, nums)

def main():
    with open("13.txt") as bus_file:
        timestamp = int(bus_file.readline())
        buses = [(i, int(num)) for i, num in enumerate(bus_file.readline().split(",")) if num != "x"]
    
    earliest_bus = -1
    best_minutes = timestamp

    for _, bus in buses:
        if bus == 0:
            continue

        bus_caught = ceil(timestamp / bus) * bus
        minutes = bus_caught - timestamp

        if minutes < best_minutes:
            earliest_bus = bus
            best_minutes = minutes
    
    print("Earliest bus:", earliest_bus, "*", best_minutes, "=", earliest_bus * best_minutes)

    chains = {}
    
    for i, num in buses:
        for j, other in buses:
            if i == j or 0 in [num, other] \
                or (j - i) % num != 0:
                continue
            
            if j not in chains:
                chains[j] = other
            
            chains[j] *= num
    
    index, best_chain = max(chains.items(), key=lambda pair: pair[1])
    multiple = best_chain
    to_check = [(index - i, num) for i, num in chains.items() if i != index]
    
    while True:
        for i, num in to_check:
            if (multiple - i) % num:
                break
        else:
            print("Earliest offset combo:", multiple - index)
            break

        multiple += best_chain

if __name__ == "__main__":
    main()