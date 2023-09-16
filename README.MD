 # Scrabble

 This is a suite of python classes designed to help with playing the popular word game. The program makes use of dictionaryapi.com to retrieve word definitions,

 It is made up of the following classes:

 - `Tile`: The base of the entire program which represents a letter tile comprised of it's character, score and distribution.
 - `Rack`: a container for tiles
 - `Word`: A combination of tiles that provides the complete score, length and definition (if found) of the word. 
 - `Dictionary`: A container of all legal words that can be searched.

 # Set Up

1. Use pipenv to install the dependencies with `python3 -m pipenv install`. 
2. run the app with `python3 pipenv run start`