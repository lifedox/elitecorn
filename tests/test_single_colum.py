from io import StringIO

from elite_corn import DirectionGroup, FromDirection, Grid


def transpose(value: str) -> str:
    return "\n".join(value)


def test_11211_returns_3() -> None:
    data = StringIO(transpose("11211"))
    grid = Grid(data)

    assert grid.show_elite_scores(FromDirection.SOUTH) == transpose("01211")
    assert grid.show_elite_scores(FromDirection.NORTH) == transpose("11210")
    assert grid.show_elite_scores(DirectionGroup.COLUMN) == transpose("01410")

    assert grid.get_greatest_elite_score(FromDirection.SOUTH) == 2
    assert grid.get_greatest_elite_score(FromDirection.NORTH) == 2
    assert grid.get_greatest_elite_score(DirectionGroup.COLUMN) == 4

    assert grid.show_is_visible(FromDirection.SOUTH) == transpose("__X_X")
    assert grid.show_is_visible(FromDirection.NORTH) == transpose("X_X__")
    assert grid.show_is_visible(DirectionGroup.COLUMN) == transpose("X_X_X")

    assert grid.count_visible_plants(FromDirection.SOUTH) == 2
    assert grid.count_visible_plants(FromDirection.NORTH) == 2
    assert grid.count_visible_plants(DirectionGroup.COLUMN) == 3


def test_41214_returns_3() -> None:
    data = StringIO(transpose("41214"))
    grid = Grid(data)

    assert grid.show_elite_scores(FromDirection.SOUTH) == transpose("01214")
    assert grid.show_elite_scores(FromDirection.NORTH) == transpose("41210")
    assert grid.show_elite_scores(DirectionGroup.COLUMN) == transpose("01410")

    assert grid.get_greatest_elite_score(FromDirection.SOUTH) == 4
    assert grid.get_greatest_elite_score(FromDirection.NORTH) == 4
    assert grid.get_greatest_elite_score(DirectionGroup.COLUMN) == 4

    assert grid.show_is_visible(FromDirection.SOUTH) == transpose("____X")
    assert grid.show_is_visible(FromDirection.NORTH) == transpose("X____")
    assert grid.show_is_visible(DirectionGroup.COLUMN) == transpose("X___X")

    assert grid.count_visible_plants(FromDirection.SOUTH) == 1
    assert grid.count_visible_plants(FromDirection.NORTH) == 1
    assert grid.count_visible_plants(DirectionGroup.COLUMN) == 2
