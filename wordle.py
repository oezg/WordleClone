from random import choice

def word_list():
    """
    Read the sgb-words.txt file and return a list of the words in the file
    """
    words = []
    with open("sgb-words.txt") as sgb:
        for line in sgb:
            words.append(line.strip())
    return words

def random_word(words):
    """
    Take a list of words as a parameter and return a random word from this list
    """
    return choice(words)

def is_real_word(word, words):
    """
    Take two parameters, a guess and a word list and return True
    if the word is in the word list and False otherwise
    """
    return word in words

def check_guess(guess, word):
    """
    Take two parameters. The first is the guessed word and the second
    is the word the user has to find. Return a string containing the
    following characters:
        X for each character in the guess that is at the correct position.
        O for each character in the guess that is in the word
            but not at the correct position.
        _ for each character in the guess that is not part of the word.
            For example, check_guess("birds", "words") should return __XXX.
        If a letter is used twice in the guessed word and exists only once
            in the word to be found, then only one letter in the return
            string is marked. In case one of the two letters is positioned
            correctly, then this letter is marked with an X in the return
            string. For example, check_guess("carat", "train") should return
            _OO_O. Another example, check_guess("taunt", "train") should
            return XO_O_
    """
    checker = {}.fromkeys(range(len(guess)), '_')
    for i in checker:
        g = guess[i] 
        if g == word[i]:
            checker[i] = 'X'
        elif g in word:
            if guess.count(g) <= word.count(g):
                checker[i] = 'O'
            else:
                checker[i] ='#'

    for i, v in checker.items():
        if v == '#':
            g = guess[i]
            indexes = [j for j in range(len(guess)) if guess[j] == g]
            number_cross = sum(word[j] == g for j in indexes)
            if len(indexes) > number_cross + 1:
                checker[i] = 'O'
                for index in indexes:
                    if index != i and word[index] != g:
                        checker[index] = '_'
            else:
                checker[i] = '_'
                
    return ''.join(checker.values())

def next_guess(words):
    """
    Take a word list as a parameter. Ask the user for a guess,
    convert the guess to lower case and check if the guess is
    in the word list. If this is the case, the guess is returned.
    Otherwise, ask the user for another guess.
    """
    guess = input("Please enter a guess: ").lower()
    while guess not in words:
        print("That's not a real word!")
        guess = input("Please enter a guess: ").lower()
    return guess

def play():
    """
    Use the functions word_list and random_word to select a random 5 letter word.
    Ask the user for a guess using the next_guess function.
    Check each guess using the check_guess function and shows the result to the user.
    Check if the users guessed the right word with six guesses or less.
        If yes, the user wins and the function prints You won!.
        Otherwise the user loses and the function prints You lost!
        as well as The word was: followed by word the user had to find.

    """
    words = word_list()
    word = random_word(words)
    for _ in range(6):
        guess = next_guess(words)
        check = check_guess(guess, word)
        print(check)
        if check == 'XXXXX':
            print('You won!')
            break
    else:
        print("You lost!")
        print(f"The word was: {word}")

play()