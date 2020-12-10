#!/usr/bin/env python3

from collections import defaultdict

def main():
    with open("10.txt") as joltage_file:
        joltages = sorted([0] + [int(line) for line in joltage_file])
    joltages.append(joltages[-1] + 3)
    
    differences = defaultdict(int)

    for i, joltage in enumerate(joltages[1:]):
        differences[joltage - joltages[i]] += 1
    
    ways = defaultdict(int, {0: 1})

    for i, joltage in enumerate(joltages[:-1]):
        for dest in joltages[i + 1:i + 4]:
            if dest - joltage > 3:
                continue

            ways[dest] += ways[joltage]
    
    print("Ways to arrange adapters:", ways[joltages[-1]])

if __name__ == "__main__":
    main()