# WordleClone
Implementation of a Wordle clone in Python

To run the game, copy the wordle.py and the sgb-words.txt files into a directory. Type `python3 wordle.py` in the command line after changing directory into the folder, into which you have copied the files. 

The basis for my version of Wordle is the file sgb-words.txt. It contains more than 5.700 five letter words. This file is accessible at https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt

- word_list() reads the sgb-words.txt file and returns a list of the words in the file.
- random_word() takes a list of words as a parameter and returns a random word from this list.
- is_real_word() takes two parameters, a guess and a word list and returns True if the word is in the word list and False otherwise.
- check_guess() takes two parameters. The first is the guessed word and the second is the word the user has to find. check_guess() returns a string containing the following characters:
  - X for each character in the guess that is at the correct position.
  - O for each character in the guess that is in the word but not at the correct position.
  - _ for each character in the guess that is not part of the word. For example, check_guess("birds", "words") should return __XXX.
  - If a letter is used twice in the guessed word and exists only once in the word to be found, then only one letter in the return string is marked. In case one of the two letters is positioned correctly, then this letter is marked with an X in the return string. For example, check_guess("carat", "train") should return _OO_O. Another example, check_guess("taunt", "train") should return XO_O_
- next_guess() takes a word list as a parameter. The function asks the user for a guess, converts the guess to lower case and checks if the guess is in the word list. If this is the case, the guess is returned. Otherwise, the function asks the user for another guess.

source: https://open.sap.com/courses/python1/items/6LfO9XYCGrjzx4WcDPTGYJ
