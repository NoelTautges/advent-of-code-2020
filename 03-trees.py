#!/usr/bin/env python3

from functools import reduce

def count_trees(trees, right, down):
    width = len(trees[0])

    def filter_trees(pair):
        num, row = pair

        if num % down != 0:
            return False
        
        return row[int(num * right / down) % width] == "#"
    
    return len(list(filter(
        filter_trees,
        enumerate(trees)
    )))


def main():
    with open("03.txt") as trees_file:
        trees = trees_file.read().splitlines()
    
    combos = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees_hit = [count_trees(trees, *pair) for pair in combos]

    print(f"{trees_hit[1]} trees hit for right 3, down 1")
    print(f"{reduce(lambda a, b: a * b, trees_hit)} when multiplied")

if __name__ == "__main__":
    main()