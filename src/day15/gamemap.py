class GameMap:
    def __init__(self, mapdata):
        self._mapdata = mapdata
        self._max_y = len(mapdata) - 1
        self._max_x = len(mapdata[0]) - 1 if self._max_y >= 0 else -1
        self._boxes = []
        self._walls = []
        self._robot = ()
        self._setup()

    def _setup(self):
        for y,row in enumerate(self._mapdata):
            for x,col in enumerate(row):
                if col == "#":
                    self._walls.append((x,y))
                elif col == "@":
                    self._robot = (x,y)
                elif col == "O":
                    self._boxes.append((x,y))
    
    def _next_empty_position(self, direction):
        position = self._robot
        if direction == "^":
            for pos_y in range(position[1] - 1, -1, -1):
                if (position[0], pos_y) in self._walls:
                    return False
                elif (position[0], pos_y) not in self._boxes:
                    return (position[0], pos_y)
        elif direction == "v":
            for pos_y in range(position[1] + 1, self._max_y + 1, 1):
                if (position[0], pos_y) in self._walls:
                    return False
                elif (position[0], pos_y) not in self._boxes:
                    return (position[0], pos_y)
        elif direction == "<":
            for pos_x in range(position[0] - 1, - 1, -1):
                if (pos_x, position[1]) in self._walls:
                    return False
                elif (pos_x, position[1]) not in self._boxes:
                    return (pos_x, position[1])
        elif direction == ">":
            for pos_x in range(position[0] + 1, self._max_x + 1, 1):
                if (pos_x, position[1]) in self._walls:
                    return False
                elif (pos_x, position[1]) not in self._boxes:
                    return (pos_x, position[1])
       
        return False

    def _get_next_space(self, direction):
        if direction == "^":
            return (self._robot[0], self._robot[1] - 1)
        elif direction == "v":
            return (self._robot[0], self._robot[1] + 1)
        elif direction == "<":
            return (self._robot[0] - 1, self._robot[1])
        elif direction == ">":
            return (self._robot[0] + 1, self._robot[1])
        else:
            return False

    def move_robot(self, direction):
        # print("robot:",self._robot)
        next_empty = self._next_empty_position(direction)
        if next_empty:
            next_space = self._get_next_space(direction)
            # print("goto",next_space,"move block", next_empty, "robot:",self._robot)
            if next_space in self._boxes:
                self._boxes.remove(next_space)
                self._boxes.append(next_empty)
            self._robot = next_space

    def get_GPS_sum(self):
        # print(self._boxes)
        result = 0
        for box in self._boxes:
            result += box[1]*100 + box[0]
        return result
    
    def print_map(self):
        graph = ""
        for row in range(0,self._max_y + 1):
            graph+="#"
            for col in range(1,self._max_y):
                if (col,row) == self._robot:
                    graph+="@"
                elif (col,row) in self._boxes:
                    graph+="O"
                elif (col,row) in self._walls:
                    graph+="#"
                else:
                    graph+="."
            graph+="#"
            graph+="\n"
        print(graph)