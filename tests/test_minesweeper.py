import minesweeper

def test_minesweeper():
    assert minesweeper


def test_place_mines():
    game = minesweeper.Minesweeper(3, 3, 2)
    assert len(game.mines) == 2


def test_fail():
    assert False
