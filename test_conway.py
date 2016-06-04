from conway import Game, Cell
import unittest

def test_init_4x8_game():
    # ........
    # ....*...
    # ...**...
    # ........
    # arrange
    game = Game()
    # act
    game.live(Cell(5, 2))
    game.live(Cell(4, 3))
    game.live(Cell(5, 3))
    # assert
    assert game.get(1, 1) == '.'
    assert game.get(5, 2) == '*'
    assert game.get(4, 3) == '*'
    assert game.get(5, 3) == '*'

def test_less_2_neighbours_will_die():
    # ........
    # ....*...
    # ....*...
    # ........
    # arrange
    game = Game()

    game.live(Cell(5, 2))
    game.live(Cell(5, 2))

    # act
    game.update()

    # assert
    assert game.get(5, 2) == '.'
    assert game.get(5, 3) == '.'
