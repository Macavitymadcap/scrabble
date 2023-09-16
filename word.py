from tile import Tile

import requests
from typing import List
from dataclasses import dataclass, field

@dataclass(order=True)
class Word:
    sort_index: int = field(init=False, repr=False)
    word: str
    score: int = field(init=False)
    length: int = field(init=False)
    tiles: List[Tile] = field(init=False)

    def __post_init__(self):
        self.length = len(self.word)
        self.tiles = [Tile(letter) if letter != "*" else Tile(letter, True) for letter in self.word]
        self.score = sum([letter.score for letter in self.tiles])
        self.sort_index = self.score
    
    def __str__(self):
        definitions = self.get_definitions()
        string = f"{self.word} ({self.score}) {[str(letter) for letter in self.tiles]}\n{definitions[0]}"
        return string

    def get_definitions(self):
        request = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + self.word)
        if request.status_code != 200:
            return [f"No definition for {self.word} found."]

        dictionary = request.json()[0]
        meanings = []
        for meaning in dictionary['meanings']:
            for definition in meaning["definitions"]:
                meanings.append(definition["definition"])
        return meanings