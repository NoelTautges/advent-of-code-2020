#!/usr/bin/env python3

import string

valid_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def digits_invalid(value, length, lower, upper):
    if len(value) != length:
        return True
    
    try:
        value = int(value)
    except:
        return True
    
    if value not in range(lower, upper + 1):
        return True
    
    return False

def main():
    passport = {}
    fields_valid = 0
    data_valid = 0

    with open("04.txt") as passports_file:
        while True:
            line = passports_file.readline()

            if line in ["\n", ""]:
                for _ in range(1):
                    for field in valid_fields:
                        if field not in passport:
                            break
                    else:
                        fields_valid += 1

                        if digits_invalid(passport["byr"], 4, 1920, 2002) \
                            or digits_invalid(passport["iyr"], 4, 2010, 2020) \
                            or digits_invalid(passport["eyr"], 4, 2020, 2030) \
                            or digits_invalid(passport["pid"], 9, 0, 999999999):
                            break
                        
                        hgt = passport["hgt"]
                        value, unit = hgt[:-2], hgt[-2:]
                        try:
                            value = int(value)
                        except ValueError:
                            break
                        if unit not in ["cm", "in"] \
                            or (unit == "cm" and value not in range(150, 194)) \
                            or (unit == "in" and value not in range(59, 77)):
                            break

                        if len((hcl := passport["hcl"])) != 7 \
                            or hcl[0] != "#":
                            break
                        try:
                            int(hcl[1:], 16)
                        except ValueError:
                            break

                        if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                            break

                        data_valid += 1
                
                passport.clear()
                
                if line == "\n":
                    continue
                else:
                    break

            for pair in line.strip().split(" "):
                key, value = pair.split(":")
                passport[key] = value
    
    print(f"{fields_valid} passports with valid fields")
    print(f"{data_valid} passports with valid data")

if __name__ == "__main__":
    main()