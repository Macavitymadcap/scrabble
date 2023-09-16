from __future__ import annotations

from dataclasses import dataclass, field
from typing import List
from string import ascii_lowercase

@dataclass(order=True)
class Tile:
    scores = {
    "a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1,
    "j": 8, "k": 5, "l": 1, "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
    "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8, "y": 4, "z": 10, "*": 0
    }
    tile_count = {
        "a": 9, "b": 2, "c": 2, "d": 4, "e": 12, "f": 2, "g": 3, "h": 2, "i": 9, 
        "j": 1, "k": 1, "l": 4, "m": 2, "n": 6, "o": 8, "p": 2, "q": 1, "r": 6, 
        "s": 4, "t": 6, "u": 4, "v": 2, "w": 2, "x": 1, "y": 2, "z": 1, "*": 2
    }
    substrings = {
        0: "\u2080", 1: "\u2081", 2: "\u2082", 3: "\u2083", 4: "\u2084", 
        5: "\u2085", 8: "\u2088", 10: "\u2081\u2080" 
    }
    sort_index: int = field(init=False, repr=False)
    symbol: str
    score: int = field(init=False)
    distribution: int = field(init=False)
    blank: bool = False
    substring: str = field(repr=False, init=False)

    def __post_init__(self):
        self.score = self.scores[self.symbol]
        self.sort_index = self.score
        self.substring = self.substrings[self.score]
        self.distribution = self.tile_count[self.symbol]


    def __str__(self):
        string = f"{self.symbol.upper()}{self.substring}"
        return string
    
    @classmethod
    def get_letters(cls) -> List[Tile]:
        letters = ascii_lowercase + "*"
        scrabble_letters = [Tile(letter) if letter != "*" else Tile(letter, True) for letter in letters]
        return scrabble_letters

    @classmethod
    def get_tiles(cls) -> List[Tile]:
        scrabble_letters = cls.get_letters()
        scrabble_tiles = []
        for letter in scrabble_letters:
            for _ in range(letter.distribution):
                scrabble_tiles.append(letter)
        return scrabble_tiles