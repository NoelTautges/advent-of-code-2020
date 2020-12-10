#!/usr/bin/env python3

from collections import defaultdict

def main():
    with open("10.txt") as joltage_file:
        joltages = sorted([0] + [int(line) for line in joltage_file])
    joltages.append(joltages[-1] + 3)
    
    differences = defaultdict(int)

    for i, joltage in enumerate(joltages[1:]):
        differences[joltage - joltages[i]] += 1
    
    print("1-jolt * 3-jolt differences =", differences[1] * differences[3])

if __name__ == "__main__":
    main()