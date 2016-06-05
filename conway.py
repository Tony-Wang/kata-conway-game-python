
DEAD_VALUE = '.'
LIVE_VALUE = '*'


class Cell(object):
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.neighbours = []

    def add_neighbour(self, neighbour):
        if neighbour is not None:
            self.neighbours.append(neighbour)

    def count_neighbout(self):
        count = 0
        for neighbour in self.neighbours:
            if neighbour.islive():
                count += 1
        return count

    def live(self):
        self.value = LIVE_VALUE

    def die(self):
        self.value = DEAD_VALUE

    def isdie(self):
        return self.value == DEAD_VALUE

    def islive(self):
        return self.value == LIVE_VALUE


class Game(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = {}
        # todo: bad smell
        for x in range(self.width):
            for y in range(self.height):
                self.grid[(x+1, y+1)] = Cell(x, y, DEAD_VALUE)
        for x in range(1, self.width+1):
            for y in range(1, self.height+1):
                currentCell = self.get(x, y)
                currentCell.add_neighbour(self.get(x-1, y-1))
                currentCell.add_neighbour(self.get(x, y-1))
                currentCell.add_neighbour(self.get(x+1, y-1))
                currentCell.add_neighbour(self.get(x-1, y))
                currentCell.add_neighbour(self.get(x+1, y))
                currentCell.add_neighbour(self.get(x-1, y+1))
                currentCell.add_neighbour(self.get(x, y+1))
                currentCell.add_neighbour(self.get(x+1, y+1))

    def get(self, x, y):
        return self.grid.get((x, y), None)

    def update(self):
        # todo :refactor to common
        for pos, cell in self.grid.iteritems():
            if cell.count_neighbout() < 2:
                cell.die()

