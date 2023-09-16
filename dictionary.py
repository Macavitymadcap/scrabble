from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Union
from random import randint

from word import Word
from rack import Rack
from word_checker import WordChecker

@dataclass
class Dictionary:
    words: List[Word]
    average_score: int = field(init=False)

    def __post_init__(self):
        self.average_score = sum([word.score for word in self.words]) / len(self)

    def __len__(self) -> int:
        return len(self.words)
        
    def search(self, search_word: str) -> Union[Word, str]:
        for word in self.words:
            if word.word == search_word:
                return word
        return f"'{search_word}' not found in ScrabbleDictionary"


    def get_random_word(self):
        index = randint(0, len(self.words))
        return self.words[index]
    

    def get_possible_words(self, letters: Rack) -> Dictionary:
        possible_words = []
        for word in self.words:
            if WordChecker(word.word, [letter for letter in letters]).word_in_letters:
                possible_words.append(word)
        return Dictionary(possible_words)
    

    def get_top_ten_words(self) -> List[Word]:
        high_scorers = [word for word in self.words if word.score >= self.average_score]
        high_scorers.sort(reverse=True)
        if len(high_scorers) > 10:
            return high_scorers[:10]
        return high_scorers

    @classmethod
    def get_dictionary(cls) -> Dictionary:
        words = []
        with open("./words.txt", "r") as file:
            for word in file.readlines():
                word = Word(word.strip())
                words.append(word)
    
        return Dictionary(words)