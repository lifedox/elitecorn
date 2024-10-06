from io import StringIO

from elite_corn import DirectionGroup, FromDirection, Grid


def test_11211_returns_3() -> None:
    data = StringIO("11211")
    grid = Grid(data)

    assert grid.show_elite_scores(FromDirection.EAST) == "0|1|2|1|1"
    assert grid.show_elite_scores(FromDirection.WEST) == "1|1|2|1|0"
    assert grid.show_elite_scores(DirectionGroup.ROW) == "0|1|4|1|0"

    assert grid.get_greatest_elite_score(FromDirection.EAST) == 2
    assert grid.get_greatest_elite_score(FromDirection.WEST) == 2
    assert grid.get_greatest_elite_score(DirectionGroup.ROW) == 4

    assert grid.show_is_visible(FromDirection.EAST) == "__X_X"
    assert grid.show_is_visible(FromDirection.WEST) == "X_X__"
    assert grid.show_is_visible(DirectionGroup.ROW) == "X_X_X"

    assert grid.count_visible_plants(FromDirection.EAST) == 2
    assert grid.count_visible_plants(FromDirection.WEST) == 2
    assert grid.count_visible_plants(DirectionGroup.ROW) == 3


def test_41214_returns_3() -> None:
    data = StringIO("41214")
    grid = Grid(data)

    assert grid.show_elite_scores(FromDirection.EAST) == "0|1|2|1|4"
    assert grid.show_elite_scores(FromDirection.WEST) == "4|1|2|1|0"
    assert grid.show_elite_scores(DirectionGroup.ROW) == "0|1|4|1|0"

    assert grid.get_greatest_elite_score(FromDirection.EAST) == 4
    assert grid.get_greatest_elite_score(FromDirection.WEST) == 4
    assert grid.get_greatest_elite_score(DirectionGroup.ROW) == 4

    assert grid.show_is_visible(FromDirection.EAST) == "____X"
    assert grid.show_is_visible(FromDirection.WEST) == "X____"
    assert grid.show_is_visible(DirectionGroup.ROW) == "X___X"

    assert grid.count_visible_plants(FromDirection.EAST) == 1
    assert grid.count_visible_plants(FromDirection.WEST) == 1
    assert grid.count_visible_plants(DirectionGroup.ROW) == 2
