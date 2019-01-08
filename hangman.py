# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string (of lowercase English letters), the word the user 
    is guessing;
    letters_guessed: list (of lowercase English letters), set of letters 
    that have been guessed so far;
    returns: bool, True if all the letters of secret_word are in 
    letters_guessed, and False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    for j in secret_word:
        if j not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    
    '''
    secret_word: string (of lowercase English letters), the word the user 
    is guessing;
    letters_guessed: list (of lowercase English letters), set of letters 
    that have been guessed so far;
    returns: string, a sequence of lowercase letters, and '_ ' (underscore
    followed by a single space) representing a partially guessed secret
    word. 
    '''
    
    string1 = ""
    for i in secret_word:
        if i in letters_guessed:
            string1 += i
        else:
            string1 += "_ "
    return string1    
    
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of lowercase English letters), set of letters 
    that have been guessed so far;
    returns: string, a set of lowecase letters which have not 
    yet been guessed in alphabetical order.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    string2 = "abcdefghijklmnopqrstuvwxyz"
    temporary = ""
    for i in string2:
        if i not in letters_guessed:
            temporary += i
    return temporary    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Plays an interactive game of Hangman according to the rules
    defined in the assignment brief.
    
    Returns: tuple of boolean, integer, and string; 
    (True, number of remaining guesses, string of 
    lowecase letters still available) if
    the secret word was guessed;
    (False, number of remaining guesses, string of lowercase 
    letters still available) if
    the secret word was not guessed.
    '''
    
    print ("Welcome to the game, Hangman!")
    print ("I'm thinking of a word that is " + str(len(secret_word)) + " letters long.")
    letters_guessed = ''
    guessesLeft = 6
    print ("------------")
    while True:
        print ("You have " + str(guessesLeft) + " guess left.")
        print ("Available letters: " + get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ")
        #check if letter is valid
        if guess in string.ascii_lowercase and guess != '':
            if guess in secret_word and guess not in letters_guessed:
                letters_guessed += guess
                print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            elif guess in letters_guessed:
                print ("Oops! You've already guessed that letter: " + get_guessed_word(secret_word, letters_guessed))
            else:
                letters_guessed += guess
                print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                guessesLeft -= 1
        else:
            print ("Oops! That is not a valid letter: " + get_guessed_word(secret_word, letters_guessed))
        print ("------------")
        
        if guessesLeft <= 0:
            print ("Sorry, You've ran out of guesses. The word was " + secret_word + ".")
            t = ('False',guessesLeft,get_available_letters(letters_guessed))
            print (t)
            break
        if is_word_guessed(secret_word, letters_guessed):
            print ("Congratulations! You've won!")
            t = ('True',guessesLeft,get_available_letters(letters_guessed))
            print (t)
            break


    # FILL IN YOUR CODE HERE AND DELETE "pass"
    




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)

if __name__ == "__main__":
    #pass

    # To test your impelementation, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)