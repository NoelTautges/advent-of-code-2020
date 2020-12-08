#!/usr/bin/env python3

def main():
    with open("08.txt") as instructions_file:
        instructions = instructions_file.readlines()

    i = 0
    run = set()
    acc = 0
    
    while i not in run:
        run.add(i)

        ins, num = instructions[i].strip().split(" ")
        num = int(num)

        i += num if ins == "jmp" else 1
        acc += num if ins == "acc" else 0
    
    print(f"Value in accumulator: {acc}")

if __name__ == "__main__":
    main()