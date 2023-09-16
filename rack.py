from dataclasses import dataclass, field
from typing import List

from tile import Tile

@dataclass
class Rack:
    letters: List[str]
    tiles: List[Tile] = field(init=False)

    def __post_init__(self):
        self.tiles = [Tile(letter) if letter != "*" else Tile(letter, True) for letter in self.letters]

    def __str__(self):
        tile_strings = [str(tile) for tile in self.tiles]
        return str(tile_strings)
