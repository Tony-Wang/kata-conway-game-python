import conway
import unittest

def test_init_4x8_game():
    # ........
    # ....*...
    # ...**...
    # ........
    # arrange
    game = conway.Game()
    # act
    game.set(5, 2, '*')
    game.set(4, 3, '*')
    game.set(5, 3, '*')
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
    game = conway.Game()
    game.set(5, 2, '*')
    game.set(5, 2, '*')

    # act
    game.update()

    # assert
    assert game.get(5, 2) == '.'
    assert game.get(5, 3) == '.'
