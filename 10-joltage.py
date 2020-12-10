#!/usr/bin/env python3

from collections import defaultdict

def main():
    with open("10.txt") as joltage_file:
        joltages = sorted([0] + [int(line) for line in joltage_file])
    joltages.append(joltages[-1] + 3)
    
    differences = defaultdict(int)
    ways = defaultdict(int, {0: 1})

    for i, joltage in enumerate(joltages):
        if i > 0:
            differences[joltage - joltages[i - 1]] += 1
        
        for dest in joltages[i + 1:i + 4]:
            if dest - joltage > 3:
                continue

            ways[dest] += ways[joltage]
    
    print("1-jolt * 3-jolt differences =", differences[1] * differences[3])
    print("Ways to arrange adapters:", ways[joltages[-1]])

if __name__ == "__main__":
    main()