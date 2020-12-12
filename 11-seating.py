#!/usr/bin/env python3

from functools import reduce

deltas = [(-1, 1), (0, 1), (1, 1), (1, 0)]

class SeatLayout:
    def __init__(self, unlimited=False):
        with open("11.txt") as layout_file:
            string_layout = [line.strip() for line in layout_file.readlines()]
        
        self.width = len(string_layout[0])
        self.height = len(string_layout)
        self.seats = [
            (x, y)
            for x in range(self.width)
            for y in range(self.height)
            if string_layout[y][x] == "L"
        ]
        self.neighbors = [[[] for x in range(self.width)] for y in range(self.height)]
        self.layout = [[False] * self.width for y in range(self.height)]
        self.max_neighbors = 4 if unlimited else 3

        for x, y in self.seats:
            for dx, dy in deltas:
                cur_x = x + dx
                cur_y = y + dy

                while cur_x in range(self.width) \
                    and cur_y in range(self.height):
                    if string_layout[cur_y][cur_x] == "L":
                        self.neighbors[y][x].append((cur_x, cur_y))
                        self.neighbors[cur_y][cur_x].append((x, y))
                        break

                    if not unlimited:
                        break

                    cur_x += dx
                    cur_y += dy
    
    def get_neighbors(self, x, y):
        neighbors = 0

        for nx, ny in self.neighbors[y][x]:
            if self.layout[ny][nx]:
                neighbors += 1
            
            if neighbors > self.max_neighbors:
                break
        
        return neighbors
    
    def update(self):
        changes = []

        for x, y in self.seats:
            state = self.layout[y][x]
            neighbors = self.get_neighbors(x, y)

            if (not state and neighbors == 0) \
                or (state and neighbors > self.max_neighbors):
                changes.append((x, y))
        
        for x, y in changes:
            self.layout[y][x] = not self.layout[y][x]
        
        return len(changes)
    
    def get_occupied(self):
        return reduce(lambda total, row: total + row.count(True), self.layout, 0)

def main():
    limited_layout = SeatLayout()
    while limited_layout.update():
        continue
    print(limited_layout.get_occupied(), "seats occupied with limited sight")

    unlimited_layout = SeatLayout(unlimited=True)
    while unlimited_layout.update():
        continue
    print(unlimited_layout.get_occupied(), "seats occupied with unlimited sight")


if __name__ == "__main__":
    main()