from rich.console import Console
error_console = Console(stderr=True, style="bold red")

from dictionary import Dictionary

console = Console()

def go_again(prompt: str) -> bool:
    go_again = input(f"{prompt} [Y/n] ")

    if go_again.lower() == "n":
        return False
    return True

def check_rack(dictionary: Dictionary) -> None:
    run = True
    while run:
        stack = input("Enter Stack (7 letters) > ")
        if len(stack) != 7:
            error_console.print("ERROR! Stack must be 7 letters")
            check_rack(dictionary)
        letters = [letter for letter in stack]
        console.print(f"Your Tiles: {letters}\nHigh scoring possibilities:\n")
        possible_words = dictionary.get_possible_words(letters)
        for word in possible_words.get_top_ten_words():
            console.print(str(word) + "\n")

        run = go_again("Check another rack?")
    
def check_word(dictionary: Dictionary) -> None:
    run = True
    while run:
        print()
        word = input("Type word to check > ")
        result = dictionary.search(word.lower())
        console.print(str(result) + "\n")

        run = go_again("Check another word?")

def main() -> None:
    run = True
    dictionary = Dictionary.get_dictionary()
    while run:
        console.print("Check [0] word or [1] stack?", end="")
        choice = int(input(" > "))
        if choice == 0:
            check_word(dictionary)
        else:
            check_rack(dictionary)
        
        run = go_again("Check something else?")

if __name__ == "__main__":
    main()