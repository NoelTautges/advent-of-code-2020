#!/usr/bin/env python3

def main():
    valid = 0

    with open("02.txt") as passwords:
        for line in passwords:
            positions, letter, password = line.strip().split(" ")
            first, second = [int(val) - 1 for val in positions.split("-")]
            letter = letter[0]
            
            if (password[first] == letter) ^ (password[second] == letter):
                valid += 1
    
    print(f"{valid} valid passwords")

if __name__ == "__main__":
    main()