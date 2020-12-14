#!/usr/bin/env python3

from bitstring import BitArray

def main():
    mem = [0] * 65535
    mask = [[], []]

    with open("14.txt") as mask_file:
        for line in mask_file:
            command, value = line.strip().split(" = ")

            if command.find("mask") != -1:
                mask = [[], []]

                for i, c in enumerate(value):
                    if c == "X":
                        continue

                    mask[int(c)].append(i)
            else:
                bitarray = BitArray(uint=int(value), length=36)
                for i, bits in enumerate(mask):
                    bitarray.set(i, bits)
                mem[int(command[4:-1])] = bitarray.uint
    
    print("Sum:", sum(mem))

if __name__ == "__main__":
    main()