MAP_WIDTH = 10
MAP_HEIGHT = 10

START_POS = (0, 0)
GOAL_POS = (9, 9)

INITIAL_OBSTACLES = [
    (2, 0), (3, 3), (5, 4),
    (6, 5), (6, 9), (9, 7)
]

class GridMap:
    def __init__(self, width=MAP_WIDTH, height=MAP_HEIGHT):
        self.width = width
        self.height = height
        self.obstacles = set(INITIAL_OBSTACLES)

    def is_valid(self, pos):
        x, y = pos
        in_bounds = 0 <= x < self.width and 0 <= y < self.height
        is_free = pos not in self.obstacles
        return in_bounds and is_free

    def add_obstacle(self, pos):
        if 0 <= pos[0] < self.width and 0 <= pos[1] < self.height:
            self.obstacles.add(pos)
            return True
        return False

    def get_neighbors(self, pos):
        x, y = pos
        candidates = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        return [p for p in candidates if self.is_valid(p)]