#!/usr/bin/env python3

from bitstring import BitArray
from itertools import product

def main():
    value_mem = {}
    value_mask = [[], []]
    address_mem = {}
    address_mask = []

    with open("14.txt") as mask_file:
        for line in mask_file:
            command, value = line.strip().split(" = ")

            if command.find("mask") != -1:
                value_mask = [[], []]
                address_mask = []

                for i, c in enumerate(value):
                    if c == "X":
                        address_mask.append(i)
                        continue

                    value_mask[int(c)].append(i)
            else:
                value_bits = BitArray(uint=int(value), length=36)
                address_value = value_bits.uint
                for i, bits in enumerate(value_mask):
                    value_bits.set(i, bits)

                address = BitArray(uint=int(command[4:-1]), length=36)
                value_address = address.uint
                address.set(1, value_mask[1])
                address_format = "".join(c if i not in address_mask else "X" for i, c in enumerate(address.bin)).replace("X", "{}")

                value_mem[value_address] = value_bits.uint
                for prod in product("01", repeat=len(address_mask)):
                    address_mem[int(address_format.format(*prod), 2)] = address_value
    
    print("Value sum:", sum(value_mem.values()))
    print("Address sum:", sum(address_mem.values()))

if __name__ == "__main__":
    main()