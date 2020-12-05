#!/usr/bin/env python3

valid_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def main():
    passport = set()
    valid = 0

    with open("04.txt") as passports_file:
        while True:
            line = passports_file.readline()

            if line in ["\n", ""]:
                for field in valid_fields:
                    if field not in passport:
                        break
                else:
                    valid += 1
                
                passport.clear()
                
                if line == "\n":
                    continue
                else:
                    break

            for pair in line.split(" "):
                passport.add(pair.split(":")[0])
    
    print(f"{valid} valid passports")

if __name__ == "__main__":
    main()