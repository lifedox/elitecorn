from io import StringIO

from elite_corn import DirectionGroup, FromDirection, Grid


def test_11211() -> None:
    data = StringIO(
        """
11111
11111
11211
11111
11111
""".strip()
    )
    grid = Grid(data)

    assert (
        grid.show_is_visible(FromDirection.EAST)
        == """
____X
____X
__X_X
____X
____X
""".strip()
    )
    assert (
        grid.show_is_visible(FromDirection.WEST)
        == """
X____
X____
X_X__
X____
X____
""".strip()
    )
    assert (
        grid.show_is_visible(FromDirection.NORTH)
        == """
XXXXX
_____
__X__
_____
_____
""".strip()
    )
    assert (
        grid.show_is_visible(FromDirection.SOUTH)
        == """
_____
_____
__X__
_____
XXXXX
""".strip()
    )
    assert (
        grid.show_is_visible(DirectionGroup.ROW)
        == """
X___X
X___X
X_X_X
X___X
X___X
""".strip()
    )
    assert (
        grid.show_is_visible(DirectionGroup.COLUMN)
        == """
XXXXX
_____
__X__
_____
XXXXX
""".strip()
    )
    assert (
        grid.show_is_visible(DirectionGroup.ALL)
        == """
XXXXX
X___X
X_X_X
X___X
XXXXX
""".strip()
    )

    assert grid.count_visible_plants(FromDirection.EAST) == grid.show_is_visible(FromDirection.EAST).count("X")
    assert grid.count_visible_plants(FromDirection.WEST) == grid.show_is_visible(FromDirection.WEST).count("X")
    assert grid.count_visible_plants(FromDirection.NORTH) == grid.show_is_visible(FromDirection.NORTH).count("X")
    assert grid.count_visible_plants(FromDirection.SOUTH) == grid.show_is_visible(FromDirection.SOUTH).count("X")
    assert grid.count_visible_plants(DirectionGroup.ROW) == grid.show_is_visible(DirectionGroup.ROW).count("X")
    assert grid.count_visible_plants(DirectionGroup.COLUMN) == grid.show_is_visible(DirectionGroup.COLUMN).count("X")
    assert grid.count_visible_plants(DirectionGroup.ALL) == grid.show_is_visible(DirectionGroup.ALL).count("X")

    assert (
        grid.show_elite_scores(DirectionGroup.ALL)
        == """
0|0|0|0|0
0|1|1|1|0
0|1|16|1|0
0|1|1|1|0
0|0|0|0|0
""".strip()
    )


def test_41214() -> None:
    data = StringIO(
        """
44444
41114
41214
41114
44444
""".strip()
    )
    grid = Grid(data)

    assert (
        grid.show_is_visible(FromDirection.EAST)
        == """
____X
____X
____X
____X
____X
""".strip()
    )
    assert (
        grid.show_is_visible(FromDirection.WEST)
        == """
X____
X____
X____
X____
X____
""".strip()
    )
    assert (
        grid.show_is_visible(FromDirection.NORTH)
        == """
XXXXX
_____
_____
_____
_____
""".strip()
    )
    assert (
        grid.show_is_visible(FromDirection.SOUTH)
        == """
_____
_____
_____
_____
XXXXX
""".strip()
    )
    assert (
        grid.show_is_visible(DirectionGroup.ROW)
        == """
X___X
X___X
X___X
X___X
X___X
""".strip()
    )
    assert (
        grid.show_is_visible(DirectionGroup.COLUMN)
        == """
XXXXX
_____
_____
_____
XXXXX
""".strip()
    )
    assert (
        grid.show_is_visible(DirectionGroup.ALL)
        == """
XXXXX
X___X
X___X
X___X
XXXXX
""".strip()
    )

    assert grid.count_visible_plants(FromDirection.EAST) == grid.show_is_visible(FromDirection.EAST).count("X")
    assert grid.count_visible_plants(FromDirection.WEST) == grid.show_is_visible(FromDirection.WEST).count("X")
    assert grid.count_visible_plants(FromDirection.NORTH) == grid.show_is_visible(FromDirection.NORTH).count("X")
    assert grid.count_visible_plants(FromDirection.SOUTH) == grid.show_is_visible(FromDirection.SOUTH).count("X")
    assert grid.count_visible_plants(DirectionGroup.ROW) == grid.show_is_visible(DirectionGroup.ROW).count("X")
    assert grid.count_visible_plants(DirectionGroup.COLUMN) == grid.show_is_visible(DirectionGroup.COLUMN).count("X")
    assert grid.count_visible_plants(DirectionGroup.ALL) == grid.show_is_visible(DirectionGroup.ALL).count("X")

    assert (
        grid.show_elite_scores(DirectionGroup.ALL)
        == """
0|0|0|0|0
0|1|1|1|0
0|1|16|1|0
0|1|1|1|0
0|0|0|0|0
""".strip()
    )

    assert grid.get_greatest_elite_score(DirectionGroup.ALL) == 16


def test_example_test() -> None:
    data = StringIO(
        """
41484
36623
76443
44650
46401
""".strip()
    )
    grid = Grid(data)

    assert (
        grid.show_is_visible(DirectionGroup.ALL)
        == """
XXXXX
XXX_X
XX_XX
X_XXX
XXXXX
""".strip()
    )

    assert grid.count_visible_plants(DirectionGroup.ALL) == grid.show_is_visible(DirectionGroup.ALL).count("X")

    assert (
        grid.show_elite_scores(DirectionGroup.ALL)
        == """
0|0|0|0|0
0|1|4|1|0
0|6|1|2|0
0|1|8|3|0
0|0|0|0|0
""".strip()
    )

    assert grid.get_greatest_elite_score(DirectionGroup.ALL) == 8


def test_rectangle_test() -> None:
    data = StringIO(
        """
41484
36623
76443
44650
""".strip()
    )
    grid = Grid(data)

    assert (
        grid.show_is_visible(DirectionGroup.ALL)
        == """
XXXXX
XXX_X
XX_XX
XXXXX
""".strip()
    )

    assert grid.count_visible_plants(DirectionGroup.ALL) == grid.show_is_visible(DirectionGroup.ALL).count("X")

    assert (
        grid.show_elite_scores(DirectionGroup.ALL)
        == """
0|0|0|0|0
0|1|4|1|0
0|3|1|2|0
0|0|0|0|0
""".strip()
    )

    assert grid.get_greatest_elite_score(DirectionGroup.ALL) == 4


def test_random_case() -> None:
    data = StringIO(
        """
86386627
40136979
14950332
64647604
60877611
10876009
60773195
07028411
""".strip()
    )
    grid = Grid(data)

    assert (
        grid.show_is_visible(DirectionGroup.ALL)
        == """
XXXXXXXX
X___XXXX
XXXX__XX
X___XX_X
X_X_XX_X
X_X____X
X_XX__XX
XXXXXXXX
""".strip()
    )

    assert grid.count_visible_plants(DirectionGroup.ALL) == grid.show_is_visible(DirectionGroup.ALL).count("X")

    assert (
        grid.show_elite_scores(DirectionGroup.ALL)
        == """
0|0|0|0|0|0|0|0
0|1|2|3|8|60|5|0
0|2|100|16|1|2|4|0
0|4|4|1|36|4|1|0
0|1|20|4|9|6|4|0
0|1|20|4|6|1|1|0
0|1|2|3|2|2|36|0
0|0|0|0|0|0|0|0
""".strip()
    )

    assert grid.get_greatest_elite_score(DirectionGroup.ALL) == 100


def test_peak_test() -> None:
    data = StringIO(
        """
6666666
6777776
6788876
6789876
6788876
6777776
6666666
""".strip()
    )
    grid = Grid(data)

    assert (
        grid.show_is_visible(DirectionGroup.ALL)
        == """
XXXXXXX
XXXXXXX
XXXXXXX
XXXXXXX
XXXXXXX
XXXXXXX
XXXXXXX
""".strip()
    )

    assert grid.count_visible_plants(DirectionGroup.ALL) == grid.show_is_visible(DirectionGroup.ALL).count("X")

    assert (
        grid.show_elite_scores(DirectionGroup.ALL)
        == """
0|0|0|0|0|0|0
0|1|1|1|1|1|0
0|1|4|2|4|1|0
0|1|2|81|2|1|0
0|1|4|2|4|1|0
0|1|1|1|1|1|0
0|0|0|0|0|0|0
""".strip()
    )

    assert grid.get_greatest_elite_score(DirectionGroup.ALL) == 81
