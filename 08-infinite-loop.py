#!/usr/bin/env python3

from collections import defaultdict

def run_instructions(instructions):
    i = 0
    run = set()
    acc = 0

    while i not in run and i < len(instructions):
        run.add(i)
        ins, num = instructions[i]

        i += num if ins == "jmp" else 1
        acc += num if ins == "acc" else 0
    
    return acc, i == len(instructions)

def main():
    with open("08.txt") as instructions_file:
        instructions = [((split := ins.split())[0], int(split[1])) for ins in instructions_file.readlines()]
    
    print("Infinite loop accumulator:", run_instructions(instructions)[0])

    for i, (ins, num) in enumerate(instructions):
        if ins == "acc":
            continue

        instructions[i] = ("nop" if ins == "jmp" else "jmp", num)
        acc, terminated = run_instructions(instructions)

        if terminated:
            print("Termination accumulator:", acc)
            break
        else:
            instructions[i] = (ins, num)

if __name__ == "__main__":
    main()