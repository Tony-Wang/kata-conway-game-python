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
        if self.nextValue is not None:
            self.value = self.nextValue
        self.nextValue = None

    def __str__(self):
        return self.value


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
            elif count == 2:
                pass
            elif count == 3 and cell.isdie():
                cell.live(nextloop=True)

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

    def draw(self):
        import sys
        for y in range(1, self.height):
            for x in range(1, self.width):
                 sys.stdout.write(str(self.get(x, y)))
            sys.stdout.write('\n')
        pass


def main():
    game = Game(8, 8)
    import random
    for i in range(10):
        game.get(random.randrange(1, 8), random.randrange(1, 8)).live()
    while True:
        game.draw()
        c = raw_input()
        game.update()


if __name__ == '__main__':
    main()
