#!/usr/bin/env python3

def main():
    range_valid = 0
    position_valid = 0

    with open("02.txt") as passwords:
        for line in passwords:
            values, letter, password = line.strip().split(" ")
            first, second = [int(val) for val in values.split("-")]
            letter = letter[0]
            
            if (count := password.count(letter)) >= first and count <= second:
                range_valid += 1
            if (password[first - 1] == letter) ^ (password[second - 1] == letter):
                position_valid += 1
    
    print(range_valid, "valid passwords according to length policy")
    print(position_valid, "valid passwords according to position policy")

if __name__ == "__main__":
    main()