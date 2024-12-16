class Box:
    def __init__(self, position):
        self._position = position

    def in_position(self, position):
        if self._position == position or self._position == (position[0] - 1, position[1]):
            return True
        return False

    def graph(self, position):
        if self._position == position:
            return "["
        elif self._position == (position[0] - 1, position[1]):
            return "]"

    def get_box_score(self):
        return self._position[1]*100 + self._position[0]

    def _box_in_position(self, position, boxes):
        for box in boxes:
            if box.in_position(position):
                return box
        return False

    def can_move(self, position, direction, boxes, walls):
        new_pos = new_pos2 = False
        if direction[2] == "<":
            new_pos = (self._position[0] + direction[0], self._position[1] + direction[1])
        elif direction[2] == ">":
            new_pos = (self._position[0] + direction[0] + 1, self._position[1] + direction[1])
        elif direction[2] in ["^","v"]:
            new_pos = (self._position[0] + direction[0], self._position[1] + direction[1])
            new_pos2 = (self._position[0] + direction[0] + 1, self._position[1] + direction[1])

        if new_pos in walls or new_pos2 in walls:
            # print("false")
            return False
        box_in_pos = self._box_in_position(new_pos, boxes)
        box_in_pos2 = False
        if new_pos2:
            box_in_pos2 = self._box_in_position(new_pos2, boxes)
        if box_in_pos and box_in_pos2 and box_in_pos != box_in_pos2:
            return box_in_pos.can_move(new_pos, direction, boxes, walls) and box_in_pos2.can_move(new_pos2, direction, boxes, walls)
        elif box_in_pos:
            return box_in_pos.can_move(new_pos, direction, boxes, walls)
        elif box_in_pos2:
            return box_in_pos2.can_move(new_pos2, direction, boxes, walls)
        return True
        
    def move(self, direction, boxes):
        new_pos = new_pos2 = False
        if direction[2] == "<":
            new_pos = (self._position[0] + direction[0], self._position[1] + direction[1])
        elif direction[2] == ">":
            new_pos = (self._position[0] + direction[0] + 1, self._position[1] + direction[1])
        elif direction[2] in ["^","v"]:
            new_pos = (self._position[0] + direction[0], self._position[1] + direction[1])
            new_pos2 = (self._position[0] + direction[0] + 1, self._position[1] + direction[1])
        box_in_pos = self._box_in_position(new_pos, boxes)
        box_in_pos2 = False
        if new_pos2:
            box_in_pos2 = self._box_in_position(new_pos2, boxes)
        
        self._position = (self._position[0] + direction[0], self._position[1] + direction[1])

        if box_in_pos and box_in_pos2 and box_in_pos != box_in_pos2:
            box_in_pos.move(direction, boxes)
            box_in_pos2.move(direction, boxes)
        elif box_in_pos:
            box_in_pos.move(direction, boxes)
        elif box_in_pos2:
            box_in_pos2.move(direction, boxes)
        

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
        newmap = []
        for row in self._mapdata:
            newrow = ""
            for col in row:
                if col == ".":
                    newrow += ".."
                elif col == "#":
                    newrow += "##"
                elif col == "O":
                    newrow += "O."
                elif col == "@":
                    newrow += "@."
            newmap.append(newrow)
        self._mapdata = newmap
        self._max_y = len(self._mapdata) - 1
        self._max_x = len(self._mapdata[0]) - 1 if self._max_y >= 0 else -1

        for y,row in enumerate(self._mapdata):
            for x,col in enumerate(row):
                if col == "#":
                    self._walls.append((x,y))
                elif col == "@":
                    self._robot = (x,y)
                elif col == "O":
                    self._boxes.append(Box((x,y)))
    
    # def _next_empty_position(self, direction):
    #     position = self._robot
    #     if direction == "^":
    #         for pos_y in range(position[1] - 1, -1, -1):
    #             if (position[0], pos_y) in self._walls:
    #                 return False
    #             elif not self._box_in_position((position[0], pos_y)):
    #                 return (position[0], pos_y)
    #     elif direction == "v":
    #         for pos_y in range(position[1] + 1, self._max_y + 1, 1):
    #             if (position[0], pos_y) in self._walls:
    #                 return False
    #             elif not self._box_in_position((position[0], pos_y)):
    #                 return (position[0], pos_y)
    #     elif direction == "<":
    #         for pos_x in range(position[0] - 1, - 1, -1):
    #             if (pos_x, position[1]) in self._walls:
    #                 return False
    #             elif not self._box_in_position((pos_x, position[1])):
    #                 return (pos_x, position[1])
    #     elif direction == ">":
    #         for pos_x in range(position[0] + 1, self._max_x + 1, 1):
    #             if (pos_x, position[1]) in self._walls:
    #                 return False
    #             elif not self._box_in_position((pos_x, position[1])):
    #                 return (pos_x, position[1])
    
    def _can_move(self, direction):
        position = self._robot
        if direction == "^":
            box_in_pos = self._box_in_position((position[0], position[1] - 1))
            if (position[0], position[1] - 1) in self._walls:
                return False
            elif box_in_pos:
                return box_in_pos.can_move((position[0], position[1] - 1), (0, -1, "^"), self._boxes, self._walls)
        elif direction == "v":
            box_in_pos = self._box_in_position((position[0], position[1] + 1))
            if (position[0], position[1] + 1) in self._walls:
                return False
            elif box_in_pos:
                return box_in_pos.can_move((position[0], position[1] + 1), (0, 1, "v"), self._boxes, self._walls)
        elif direction == "<":
            box_in_pos = self._box_in_position((position[0] - 1, position[1]))
            if (position[0] - 1, position[1]) in self._walls:
                return False
            elif box_in_pos:
                return box_in_pos.can_move((position[0] - 1, position[1]), (-1, 0, "<"), self._boxes, self._walls)
        elif direction == ">":
            box_in_pos = self._box_in_position((position[0] + 1, position[1]))
            if (position[0] + 1, position[1]) in self._walls:
                return False
            elif box_in_pos:
                return box_in_pos.can_move((position[0] + 1, position[1]), (1, 0, ">"), self._boxes, self._walls)
       
        return True

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
        
    def _box_in_position(self, position):
        for box in self._boxes:
            if box.in_position(position):
                return box
        return False

    def move_robot(self, direction):
        # print("robot:",self._robot)
        can_move = self._can_move(direction)
        # print("can_move", can_move)
        if can_move:
            next_space = self._get_next_space(direction)
            # print("goto",next_space,"move block", next_empty, "robot:",self._robot)
            box_in_pos = self._box_in_position(next_space)
            if box_in_pos:
                if direction == "^":
                    box_dir = (0,-1,"^")
                elif direction == "v":
                    box_dir = (0,1,"v")
                elif direction == "<":
                    box_dir = (-1,0,"<")
                elif direction == ">":
                    box_dir = (1,0,">")
                else:
                    box_dir = "issue"
                box_in_pos.move(box_dir, self._boxes)
            self._robot = next_space

    def get_GPS_sum(self):
        # print(self._boxes)
        result = 0
        for box in self._boxes:
            result += box.get_box_score()
        return result
    
    def print_map(self):
        graph = ""
        for row in range(self._max_y + 1):
            for col in range(self._max_x + 1):
                box_in_pos = self._box_in_position((col,row))
                if (col,row) == self._robot:
                    graph+="@"
                elif box_in_pos:
                    graph+=box_in_pos.graph((col,row))
                elif (col,row) in self._walls:
                    graph+="#"
                else:
                    graph+="."
            graph+="\n"
        # print(graph)
        return graph