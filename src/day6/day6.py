class Area:
    def __init__(self, maparea):
        self._maparea = maparea
        self._mapbounds = (len(maparea[0]) -1 if len(maparea)>0 else 0, len(maparea) - 1)
        self._guard_coverage_area = set()
        self._guard_route = set()
        self._initial_guard_position = self._find_guard_position()
        self._guard_position = self._initial_guard_position
        self._initial_guard_direction = self._maparea[self._guard_position[1]][self._guard_position[0]]
        self._guard_direction = self._initial_guard_direction
        self._guard_eternal_loop = False
        self._new_block_position = None

    def _find_guard_position(self):
        for y, row in enumerate(self._maparea):
            for x, col in enumerate(row):
                if col in ["^", ">", "<", "v"]:
                    return (x,y)
        return None
    
    def _is_out_of_bounds(self, position):
        return position[0] > self._mapbounds[0] or position[1] > self._mapbounds[1] or position[0] < 0 or position[1] < 0

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
        return self._maparea[position[1]][position[0]] != "#" and self._new_block_position != position
    
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
        self._guard_route.add((self._guard_direction, self._guard_position))
        if self._can_guard_move_to_position(next_guard_position):
            if (self._guard_direction, next_guard_position) in self._guard_route:
                print(f"eternal {self._new_block_position}")
                self._guard_eternal_loop = True
                return False
            self._guard_position = next_guard_position
        else:
            #print(f"turn right: {self._guard_direction}{self._guard_position}, {self._new_block_position}")
            self._guard_turn_right()

        return True
    
    def get_guard_coverage_area(self):
        return len(self._guard_coverage_area)
    
    def _set_new_block_position(self, position):
        if position == self._initial_guard_position:
            return False
        if self._maparea[position[1]][position[0]] == "#":
            return False
        self._new_block_position = position
        return True

    def try_new_block_position(self):
        try_position = (0,0) if not self._new_block_position else self._new_block_position
        c = False
        while not c:
            if not self._new_block_position:
                pass
            elif try_position[0]+1 > self._mapbounds[0] and try_position[1]+1 > self._mapbounds[1]:
                return False
            elif try_position[0]+1 > self._mapbounds[0]:
                try_position = (0,try_position[1]+1)
            else:
                try_position = (try_position[0]+1,try_position[1])
            c = self._set_new_block_position(try_position)
        #print(f"try_position: {try_position}")
        return True

    def is_guard_eternal_loop(self):
        return self._guard_eternal_loop
    
    def reset_guard(self):
        self._guard_position = self._initial_guard_position
        self._guard_direction = self._initial_guard_direction
        self._guard_coverage_area = set()
        self._guard_route = set()
        self._guard_eternal_loop = False

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
    #print(area.get_guard_position())
    #print(area.get_guard_direction())
    # for _ in range(10):
    #     area.move_guard()
    #     print(area.get_guard_position())
    #     print(area.get_guard_direction())
    while area.move_guard():
        pass
    print(f"1st part, coverage area: {area.get_guard_coverage_area()}")
    
    eternal = []
    for y,row in enumerate(maparea):
        for x,col in enumerate(row):
            #print(f"row: {x},{y}")
            area.reset_guard()
            area.try_new_block_position()
            while area.move_guard():
                pass
            #print(area.is_guard_eternal_loop())
            if area.is_guard_eternal_loop():
                eternal.append((x,y))
    print(f"2nd part, 1 block eternal loop positions: {len(eternal)}")

if __name__ == "__main__":
    main()
