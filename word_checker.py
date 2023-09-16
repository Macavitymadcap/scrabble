from typing import Dict, List

class WordChecker:
    def __init__(self, word: str, letters: List[str]):
        self.word = word
        self.letters = letters

    @property
    def word_dict(self) -> Dict[str, int]:
        dict = {}
        for letter in str(self.word):
            dict[letter] = dict.get(letter, 0) + 1
        return dict

    @property
    def word_in_letters(self) -> bool:
        flag = 1
        for item in self.word_dict:
            if item not in self.letters:
                flag = 0
            else:
                if self.letters.count(item) != self.word_dict[item]:
                    flag = 0
        if flag == 1:
            return True
        return False
