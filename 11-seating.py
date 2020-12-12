#!/usr/bin/env python3

deltas = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if [dx, dy] != [0, 0]]

class SeatLayout:
    def __init__(self):
        with open("11.txt") as seats_file:
            string_layout = [line.strip() for line in seats_file.readlines()]
        
        self.width = len(string_layout[0])
        self.height = len(string_layout)
        self.seats = [(x, y) for x in range(self.width) for y in range(self.height) if string_layout[y][x] == "L"]
        self.layout = list([False] * self.width for y in range(self.height))
    
    def get_neighbors(self, x, y):
        neighbors = 0

        for dx, dy in deltas:
            if x + dx not in range(self.width) \
                or y + dy not in range(self.height):
                continue
            
            if self.layout[y + dy][x + dx]:
                neighbors += 1
            
            if neighbors == 4:
                break
        
        return neighbors
    
    def update(self):
        changes = []

        for x, y in self.seats:
            state = self.layout[y][x]
            neighbors = self.get_neighbors(x, y)

            if (not state and neighbors == 0) \
                or (state and neighbors > 3):
                changes.append((x, y))
        
        for x, y in changes:
            self.layout[y][x] = not self.layout[y][x]
        
        return len(changes)

def main():
    layout = SeatLayout()

    while layout.update():
        continue

    occupied = sum(1 for _ in filter(lambda coords: layout.layout[coords[1]][coords[0]], layout.seats))
    print(occupied, "seats occupied")

if __name__ == "__main__":
    main()