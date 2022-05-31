from random import choice

def word_list():
    words = []
    with open("sgb-words.txt") as sgb:
        for line in sgb:
            words.append(line.strip())
    return words

def random_word(words):
    return choice(words)

def is_real_word(word, words):
    return word in words

def find_indexes(g, guess):
    indexes = []
    i = 0
    while i < len(guess):
        try:
            index = guess[i:].index(g)
        except:
            break
        else:
            indexes.append(index)
            i = i + 1
    return indexes
        
def find_matches(g, word):
    matches = []
    for i, w in enumerate(word):
        if w == g:
            matches.append(i)
    return matches

def check_guess(guess, word):
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
    guess = input("Please enter a guess: ").lower()
    while guess not in words:
        print("That's not a real word!")
        guess = input("Please enter a guess: ").lower()
    return guess

def play():
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