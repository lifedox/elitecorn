from __future__ import annotations

import dataclasses
import enum
import typing as typ
import weakref
from functools import cache, cached_property
from itertools import accumulate, cycle, takewhile
from math import prod
from operator import attrgetter, methodcaller, truth

Height = typ.NewType("Height", int)


@dataclasses.dataclass(frozen=True, slots=True, eq=True)
class Coordinate:
    x: int
    y: int

    def __repr__(self) -> str:  # pragma: no cover
        return f"(x={self.x}, y={self.y})"

    def __add__(self, other: Coordinate) -> Coordinate:
        return Coordinate(self.x + other.x, self.y + other.y)


@enum.unique
class FromDirection(enum.Enum):
    NORTH = Coordinate(0, -1)
    SOUTH = Coordinate(0, 1)
    EAST = Coordinate(1, 0)
    WEST = Coordinate(-1, 0)

    def __repr__(self) -> str:  # pragma: no cover
        return self.__class__.__name__ + "." + self.name

    @cached_property
    def cycle(self) -> typ.Iterator[Coordinate]:
        return cycle([self.value])


flip = {
    FromDirection.NORTH: FromDirection.SOUTH,
    FromDirection.SOUTH: FromDirection.NORTH,
    FromDirection.EAST: FromDirection.WEST,
    FromDirection.WEST: FromDirection.EAST,
}


@enum.unique
class DirectionGroup(enum.Enum):
    ROW = (FromDirection.EAST, FromDirection.WEST)
    COLUMN = (FromDirection.NORTH, FromDirection.SOUTH)
    ALL = tuple(FromDirection)

    def __repr__(self) -> str:  # pragma: no cover
        return self.__class__.__name__ + "." + self.name


IterableDirections = FromDirection | DirectionGroup


@cache
def iterate_directions(value: IterableDirections) -> typ.Iterable[FromDirection]:
    if isinstance(value, DirectionGroup):
        return value.value
    else:
        return (value,)


@dataclasses.dataclass(frozen=True)
class Cell:
    coordinate: Coordinate
    height: Height
    _grid: weakref.ProxyType[Grid] = dataclasses.field(repr=False)

    def __get_heights_from_ray(self, from_coordinate: Coordinate, direction: FromDirection) -> typ.Iterator[Height]:
        return map(attrgetter("height"), self._grid._cast_incoming_ray(from_coordinate, direction))

    def __calculate_elite_score(self, direction: FromDirection) -> int:
        # Elite Score is calculating from the cell pointing outward. `FromDirection` is defined pointing inward.
        from_cell_direction = flip[direction]
        height = self.height
        count = 0
        for other_cell_height in self.__get_heights_from_ray(self.coordinate, from_cell_direction):
            count += 1
            if other_cell_height >= height:
                break
        return count

    def __is_visible(self, direction: FromDirection) -> bool:
        # Querying Cell Height > Other cells Heights
        return all(map(self.height.__gt__, self.__get_heights_from_ray(self.coordinate, direction)))

    def calculate_elite_score(self, directions: IterableDirections) -> int:
        return prod(map(self.__calculate_elite_score, iterate_directions(directions)))

    def is_visible(self, directions: IterableDirections) -> bool:
        return any(map(self.__is_visible, iterate_directions(directions)))


class Grid(dict[Coordinate, Cell]):
    def __init__(self, data: typ.TextIO) -> None:
        super().__init__()

        for y, line in enumerate(data):
            for x, value in enumerate(line.strip()):
                self._add_cell(Coordinate(x, y), Height(int(value)))

        self.size_y = y + 1
        self.size_x = x + 1

    def _add_cell(self, coordinate: Coordinate, height: Height) -> None:
        self[coordinate] = Cell(coordinate, height, weakref.proxy(self))

    def _cast_incoming_ray(self, from_coordinate: Coordinate, direction: FromDirection) -> typ.Iterator[Cell]:
        ray: typ.Iterator[Coordinate] = accumulate(direction.cycle, initial=from_coordinate)
        next(ray)  # pop starting coordinate
        return typ.cast(typ.Iterator[Cell], takewhile(truth, map(self.get, ray)))

    def count_visible_plants(self, directions: IterableDirections = DirectionGroup.ALL) -> int:
        return sum(map(methodcaller("is_visible", directions), self.values()))

    def get_greatest_elite_score(self, directions: IterableDirections = DirectionGroup.ALL) -> int:
        return max(map(methodcaller("calculate_elite_score", directions), self.values()))

    def show_elite_scores(self, directions: IterableDirections = DirectionGroup.ALL) -> str:
        def line(y: int) -> str:
            coors = (Coordinate(x, y) for x in range(self.size_x))
            cells = map(self.__getitem__, coors)
            per_cell_count = map(methodcaller("calculate_elite_score", directions), cells)
            return "|".join(map(str, per_cell_count))

        return "\n".join(map(line, range(self.size_y)))

    def show_is_visible(self, directions: IterableDirections = DirectionGroup.ALL) -> str:
        display = {True: "X", False: "_"}

        def line(y: int) -> str:
            coors = (Coordinate(x, y) for x in range(self.size_x))
            cells = map(self.__getitem__, coors)
            per_cell_count = map(display.__getitem__, map(methodcaller("is_visible", directions), cells))
            return "".join(map(str, per_cell_count))

        return "\n".join(map(line, range(self.size_y)))
