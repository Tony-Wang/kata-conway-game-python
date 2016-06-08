DEAD_VALUE = '.'
LIVE_VALUE = '*'


class Cell(object):
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.nextValue = None

    def live(self, nextloop=False):
        if nextloop:
            self.nextValue = LIVE_VALUE
        else:
            self.value = LIVE_VALUE

    def die(self, nextloop=False):
        if nextloop:
            self.nextValue = DEAD_VALUE
        else:
            self.value = DEAD_VALUE

    def isdie(self):
        return self.value == DEAD_VALUE

    def islive(self):
        return self.value == LIVE_VALUE

    def update(self):
        self.value = self.nextValue


class Game(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = {}
        for x in range(self.width):
            for y in range(self.height):
                self.grid[(x, y)] = Cell(x, y, DEAD_VALUE)

    def get(self, x, y):
        return self.grid.get((x, y), None)

    def update(self):
        # todo :refactor to common
        for pos, cell in self.grid.iteritems():
            count = self.count_neighbout(*pos)
            if count < 2 or count > 3:
                cell.die(nextloop=True)

        for pose, cell in self.grid.iteritems():
            cell.update()

    def count_neighbout(self, x, y):
        count = 0
        if self.get(x - 1, y - 1) is not None and self.get(x - 1, y - 1).islive():
            count += 1
        if self.get(x, y - 1) is not None and self.get(x, y - 1).islive():
            count += 1
        if self.get(x + 1, y - 1) is not None and self.get(x + 1, y - 1).islive():
            count += 1
        if self.get(x - 1, y) is not None and self.get(x - 1, y).islive():
            count += 1
        if self.get(x + 1, y) is not None and self.get(x + 1, y).islive():
            count += 1
        if self.get(x - 1, y + 1) is not None and self.get(x - 1, y + 1).islive():
            count += 1
        if self.get(x, y + 1) is not None and self.get(x, y + 1).islive():
            count += 1
        if self.get(x + 1, y + 1) is not None and self.get(x + 1, y + 1).islive():
            count += 1
        return count
