class Robot:
    def __init__(self, position, velocity, map_boundaries):
        self._position = (int(position[0]), int(position[1]))
        self._velocity = (int(velocity[0]), int(velocity[1]))
        self._map_boundaries = map_boundaries

    def move(self, seconds=1):
        position_x = (self._position[0] + self._velocity[0] * seconds) % self._map_boundaries[0]
        position_y = (self._position[1] + self._velocity[1] * seconds) % self._map_boundaries[1]
        self._position = (position_x, position_y)

    def get_position(self):
        return self._position