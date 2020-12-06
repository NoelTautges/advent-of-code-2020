#!/usr/bin/env python3

def main():
    anyone_group = set()
    anyone_sum = 0
    everyone_group = set()
    everyone_sum = 0
    first_person = True

    with open("06.txt") as questions_file:
        for line in questions_file:
            line = line.strip()

            if line == "":
                anyone_sum += len(anyone_group)
                anyone_group.clear()
                everyone_sum += len(everyone_group)
                everyone_group.clear()
                first_person = True

                continue

            anyone_group.update(line)
            everyone_group = set(line) if first_person else {q for q in everyone_group if q in line}
            first_person = False
        
    print(f"Anyone sum: {anyone_sum}")
    print(f"Everyone sum: {everyone_sum}")

if __name__ == "__main__":
    main()