class Trailmap:
    def __init__(self, trailmap):
        self._trailmap = trailmap
        self._y_max = len(self._trailmap) - 1
        self._x_max = len(self._trailmap[0]) - 1 if self._y_max >= 0 else -1

    def _valid_position(self, position):
        if self._y_max >= position[1] and self._x_max >= position[0] and 0 <= position[0] and 0 <= position[1]:
            return position
        else:
            return False

    def _get_new_position(self, current, direction):
        match direction:
            case "up":
                return self._valid_position((current[0], current[1] - 1))
            case "down":
                return self._valid_position((current[0], current[1] + 1))
            case "left":
                return self._valid_position((current[0] - 1, current[1]))
            case "right":
                return self._valid_position((current[0] + 1, current[1]))
            case _:
                return False

    def _find_route(self, position, trail_endings, prev_value=-1):
        current_value = self._trailmap[position[1]][position[0]]
        
        if (position[0], position[1]) in trail_endings:
            return 0
        if current_value != prev_value + 1:
            return 0
        if current_value == 9:
            trail_endings.append((position[0], position[1]))
            return 1
        
        
        routes = 0
        left = self._get_new_position(position,"left")
        right = self._get_new_position(position,"right")
        up = self._get_new_position(position,"up")
        down = self._get_new_position(position,"down")

        if left:
            routes += self._find_route(left, trail_endings, current_value)
        if right:
            routes += self._find_route(right, trail_endings, current_value)
        if up:
            routes += self._find_route(up, trail_endings, current_value)
        if down:
            routes += self._find_route(down, trail_endings, current_value)

        return routes

    def get_traihead_score(self, trailhead):
        trail_endings = []
        if self._trailmap[trailhead[1]][trailhead[0]] != 0:
            return 0
        return self._find_route(trailhead, trail_endings)
