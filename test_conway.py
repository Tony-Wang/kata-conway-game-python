import conway


def test_init_4x8_game():
    # ........
    # ....*...
    # ...**...
    # ........
    game = conway.Game()
    assert game.get(1, 1) == '.'
    assert game.get(5, 2) == '*'
    assert game.get(4, 3) == '*'
    assert game.get(5, 3) == '*'

