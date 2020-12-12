#!/usr/bin/env python3

class Navigator:
    def __init__(self, waypoint=False):
        self.x = 0
        self.y = 0
        self.angle = 0
        self.wx = 10
        self.wy = 1
        self.waypoint = waypoint
    
    def update(self, instruction):
        command = instruction[0]
        num = int(instruction[1:].strip())

        if self.waypoint:
            if command == "N": self.wy += num
            elif command == "S": self.wy -= num
            elif command == "E": self.wx += num
            elif command == "W": self.wx -= num
            elif command in ["L", "R"]:
                for _ in range(int(num / 90)):
                    if command == "L": self.wx, self.wy = -self.wy, self.wx
                    else: self.wx, self.wy = self.wy, -self.wx
            elif command == "F":
                self.x += self.wx * num
                self.y += self.wy * num
        else:
            if command == "F":
                if self.angle == 0: command = "E"
                elif self.angle == 90: command = "S"
                elif self.angle == 180: command = "W"
                elif self.angle == 270: command = "N"
            
            if command == "N": self.y += num
            elif command == "S": self.y -= num
            elif command == "E": self.x += num
            elif command == "W": self.x -= num
            elif command == "L": self.angle = (self.angle - num) % 360
            elif command == "R": self.angle = (self.angle + num) % 360

    def get_manhattan_distance(self):
        return abs(self.x) + abs(self.y)

def main():
    absolute = Navigator()
    waypoint = Navigator(waypoint=True)

    with open("12.txt") as directions_file:
        for line in directions_file:
            absolute.update(line)
            waypoint.update(line)
    
    print("Absolute Manhattan distance:", absolute.get_manhattan_distance())
    print("Waypoint Manhattan distance:", waypoint.get_manhattan_distance())

if __name__ == "__main__":
    main()