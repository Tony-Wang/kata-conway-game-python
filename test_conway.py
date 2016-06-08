from conway import Game


def test_init_4x8_game():
    # ........
    # ....*...
    # ...**...
    # ........
    # arrange
    game = Game(8, 4)

    # act
    game.get(5, 2).live()
    game.get(4, 3).live()
    game.get(5, 3).live()

    # assert
    assert game.get(1, 1).isdie()
    assert game.get(5, 2).islive()
    assert game.get(4, 3).islive()
    assert game.get(5, 3).islive()


def test_less_2_neighbours_will_die():
    # ........
    # ....*...
    # ....*...
    # ........

    # arrange
    game = Game(8, 4)

    game.get(5, 2).live()
    game.get(5, 2).live()

    # act
    game.update()

    # assert
    assert game.get(5, 2).isdie()
    assert game.get(5, 3).isdie()

def test_count_cell_neighbours():
    # ........
    # ..***...
    # ...**...
    # ........
    # arrang
    game = Game(8, 4)
    game.get(3, 2).live()
    game.get(4, 2).live()
    game.get(5, 2).live()
    game.get(4, 3).live()
    game.get(5, 3).live()
    # act
    # assert
    assert game.count_neighbout(3, 2) == 2
    assert game.count_neighbout(4, 2) == 4
    assert game.count_neighbout(5, 2) == 3
    assert game.count_neighbout(4, 3) == 4
    assert game.count_neighbout(5, 3) == 3


def test_more_3_neighbours_will_die():
    # ........
    # ..***...
    # ...**...
    # ........
    # arrange
    game = Game(8, 4)
    game.get(3, 2).live()
    game.get(4, 2).live()
    game.get(5, 2).live()
    game.get(4, 3).live()
    game.get(5, 3).live()

    # arrange
    game = Game(8, 4)
    game.get(3, 2).live()
    game.get(4, 2).live()
    game.get(5, 2).live()
    game.get(4, 3).live()
    game.get(5, 3).live()

    # act
    game.update()

    # assert
    assert game.get(4, 2).isdie() == True
    assert game.get(4, 3).isdie() == True
