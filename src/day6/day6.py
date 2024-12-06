class Area:
    def __init__(self, maparea):
        self._maparea = maparea
        self._mapbounds = (len(maparea[0]) -1 if len(maparea)>0 else 0, len(maparea) - 1)
        self._guard_coverage_area = set()
        self._guard_position = self._find_guard_position()
        self._guard_direction = self._maparea[self._guard_position[1]][self._guard_position[0]]

    def _find_guard_position(self):
        for y, row in enumerate(self._maparea):
            for x, col in enumerate(row):
                if col in ["^", ">", "<", "v"]:
                    return (x,y)
        return None
    
    def _is_out_of_bounds(self, position):

        return position[0] > self._mapbounds[0] or position[1] > self._mapbounds[1]

    def _get_next_guard_position(self):
        if self._guard_direction == "^":
            return (self._guard_position[0], self._guard_position[1] - 1)
        elif self._guard_direction == "v":
            return (self._guard_position[0],self._guard_position[1] + 1)
        elif self._guard_direction == ">":
            return (self._guard_position[0] + 1 ,self._guard_position[1])
        elif self._guard_direction == "<":
            return (self._guard_position[0] - 1 ,self._guard_position[1])
        raise ValueError(f"Incorrect direction value {self._guard_direction}")

    def _can_guard_move_to_position(self, position):
        #print(self._maparea[position[1]][position[0]], position)
        return self._maparea[position[1]][position[0]] != "#"
    
    def _guard_turn_right(self):
        if self._guard_direction == "^":
            self._guard_direction = ">"
        elif self._guard_direction == "v":
            self._guard_direction = "<"
        elif self._guard_direction == ">":
            self._guard_direction = "v"
        elif self._guard_direction == "<":
            self._guard_direction = "^"
        else:
            raise ValueError(f"Incorrect direction value {self._guard_direction}")

    def get_guard_position(self):
        return self._guard_position
    
    def get_guard_direction(self):
        return self._guard_direction

    def move_guard(self):
        self._guard_coverage_area.add(self._guard_position)
        next_guard_position = self._get_next_guard_position()
        if self._is_out_of_bounds(next_guard_position):
            return False
        if self._can_guard_move_to_position(next_guard_position):
            self._guard_position = next_guard_position
        else:
            self._guard_turn_right()

        return True
    
    def get_guard_coverage_area(self):
        return len(self._guard_coverage_area)


def readFile(file_path):
    maparea = []
    with open(file_path, 'r') as file:
        for row in file:
            maparea.append(row.replace("\n", ""))   
    return maparea

def main():
    #maparea = readFile("./test_input.txt")
    maparea = readFile("./input.txt")
    area = Area(maparea)
    print(area.get_guard_position())
    print(area.get_guard_direction())
    # for _ in range(10):
    #     area.move_guard()
    #     print(area.get_guard_position())
    #     print(area.get_guard_direction())
    while area.move_guard():
        pass
    print(area.get_guard_coverage_area())
    

if __name__ == "__main__":
    main()
