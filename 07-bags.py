#!/usr/bin/env python3

from collections import defaultdict
from functools import reduce

bags = {}

def retrieve_bags():
    with open("07.txt") as bags_file:
        for line in bags_file:
            container, contained = line.split(" bags contain ")
            contained_parts = contained.split(", ")
            
            if contained_parts[0] == "no other bags.\n":
                continue

            contained_bags = {}

            for part in contained_parts:
                split = part.split(" ")
                contained_bags[" ".join(split[1:3])] = int(split[0])
            
            bags[container] = contained_bags

def memoize(get_bag_contents):
    memo = {}

    def helper(bag, num):
        if bag not in memo:
            memo[bag] = get_bag_contents(bag)
        
        return {sub_bag: sub_num * num for sub_bag, sub_num in memo[bag].items()}
    
    return helper

def get_single_contents(bag):
    bag_contents = defaultdict(int)
    bag_contents[bag] = 1

    for sub_bag, sub_num in bags.get(bag, {}).items():
        for returned_bag, returned_num in get_single_contents(sub_bag).items():
            bag_contents[returned_bag] += returned_num * sub_num
    
    return bag_contents

def memoize_bags():
    memo = {}

    def helper(bag, num):
        if bag not in memo:
            memo[bag] = get_single_contents(bag)
        
        return {sub_bag: sub_num * num for sub_bag, sub_num in memo[bag].items()}
    
    return helper
get_bag_contents = memoize_bags()

def main():
    retrieve_bags()
    bag_contents = {bag: get_bag_contents(bag, 1) for bag in bags}

    shiny_gold_containers = len([bag for bag, contents in bag_contents.items() if bag != "shiny gold" and "shiny gold" in contents])
    print(f"{shiny_gold_containers} bags holding a shiny gold one")
    shiny_gold_contained = reduce(lambda one, two: one + two, bag_contents["shiny gold"].values()) - 1
    print(f"{shiny_gold_contained} bags in a shiny gold one")

if __name__ == "__main__":
    main()