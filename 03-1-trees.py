#!/usr/bin/env python3

def main():
    with open("03.txt") as trees_file:
        trees = trees_file.read().splitlines()
    
    width = len(trees[0])
    trees_hit = len(list(filter(
        lambda pair: pair[1][(pair[0] * 3) % width] == "#",
        enumerate(trees)
    )))
    print(f"{trees_hit} trees hit")

if __name__ == "__main__":
    main()