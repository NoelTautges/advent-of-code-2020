#!/usr/bin/env python3

def main():
    x = 0
    y = 0
    angle = 0

    with open("12.txt") as directions_file:
        for line in directions_file:
            command = line[:1]
            num = int(line[1:].strip())

            if command == "F":
                if angle == 0: command = "E"
                elif angle == 90: command = "S"
                elif angle == 180: command = "W"
                elif angle == 270: command = "N"

            if command == "N": y += num
            elif command == "S": y -= num
            elif command == "E": x += num
            elif command == "W": x -= num
            elif command == "L": angle = (angle - num) % 360
            elif command == "R": angle = (angle + num) % 360
    
    print("Manhattan distance:", abs(x) + abs(y))

if __name__ == "__main__":
    main()