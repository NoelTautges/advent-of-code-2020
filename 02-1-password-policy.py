#!/usr/bin/env python3

def main():
    valid = 0

    with open("02.txt") as passwords:
        for line in passwords:
            occurrence_range, letter, password = line.strip().split(" ")
            lower, upper = [int(val) for val in occurrence_range.split("-")]
            letter = letter[0]
            
            if (count := password.count(letter)) >= lower and count <= upper:
                valid += 1
    
    print(f"{valid} valid passwords")

if __name__ == "__main__":
    main()