from pathlib import Path

from elite_corn import Grid

ASSET_PATH = Path(__file__).parent / "../input.txt"


def test_file() -> None:
    with ASSET_PATH.open() as fobj:
        grid = Grid(fobj)

    assert grid.get_greatest_elite_score() == 470596
    assert grid.count_visible_plants() == 1700
