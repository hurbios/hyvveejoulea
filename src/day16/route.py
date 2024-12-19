class Node:
    def __init__(self, position, direction, score, parent):
        self._position = position
        self._direction = direction
        self._children = []
        self._parents = [parent]
        self._score = score

    def get_next_nodes(self):
        allowed_directions = {"^":["^","<",">"],"<":["^","v","<"],">":["^","v",">"],"v":["v","<",">"]}
        directions = {"^":(0,-1), "v":(0,1), "<": (-1,0), ">":(1,0)}
        next_nodes = []
        for direction in allowed_directions[self._direction]:
            next_position = (self._position[0] + directions[direction][0], self._position[1] + directions[direction][1])
            next_score = (self._score + 1 if self._direction == direction else self._score + 1001)
            next_nodes.append((next_position, direction, next_score, self))
        return next_nodes
    
    def get_score(self):
        return self._score
    
    def update(self, score, parent):
        if self._score > score:
            self._parents = [parent]
            self._score = score
            self._children = []
            return self
        else:
            return False

    def add_child(self, node):
        self._children.append(node)

    def get_parents(self):
        return self._parents


class Nodes:
    def __init__(self, start_position, start_direction, area):
        self._nodes = {}
        self._add_node(start_position, start_direction, 0, None)
        self._area = area
        self._finish_node = None


    def _add_node(self, position, direction, score, parent):
        new_node = Node(position, direction, score, parent)
        self._nodes[(position, direction)] = new_node
        return new_node

    def _get_next_nodes(self):
        pass

    def _is_valid_position(self, node):
        # print("test",node)
        return False if self._area[node[0][1]][node[0][0]] == "#" else True

    def _is_finish_position(self, node):
        return True if self._area[node[0][1]][node[0][0]] == "E" else False

    def create_network(self, starting_point):
        next_nodes = self._nodes[starting_point].get_next_nodes()
        self.starting_node = self._nodes[starting_point]

        # while len(next_nodes) > 0:
        for next_node in next_nodes:
            if self._is_valid_position(next_node):
                new_node = updated = False
                if (next_node[0],next_node[1]) not in self._nodes:
                    new_node = self._add_node(next_node[0],next_node[1],next_node[2],next_node[3])
                else:
                    updated = self._nodes[(next_node[0],next_node[1])].update(next_node[2],next_node[3])
                
                temp_node = new_node or updated
                
                if self._is_finish_position(next_node):
                    self._finish_node = temp_node
                elif temp_node:
                    next_node[3].add_child(temp_node)
                    next_nodes += temp_node.get_next_nodes()

    def get_score(self):
        return self._finish_node.get_score()


