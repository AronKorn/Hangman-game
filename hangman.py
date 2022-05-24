def opening_screen():
    """Prints an opening screen
    :return: None"""
    HANGMAN_ASCII_ART = """
      _    _
     | |  | |
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |
                         |___/"""
    MAX_TRIES = 6
    print(HANGMAN_ASCII_ART, "\n", MAX_TRIES, "\n")


def choose_word(file_path, index):
    """Selects a word from a file by index number
    :parm file_path: The file that contains the words
    :parm index: Index number of the word
    :type file_path: str
    :type index: int
    :return: The word in the index position
    :rtype: str
    """
    file_open = open(file_path, "r")
    file_read = file_open.read()
    file_open.close()
    word_list = file_read.split()
    if index <= len(word_list):
        result = word_list[index - 1].lower()
    else:
        result = word_list[index % len(word_list) - 1].lower()
    return result


def print_hangman(num_of_tries):
    """Prints the picture of the hangman
    :parm num_of_tries: The amount of attempts by the player
    :type num_of_tries: int
    :return: None
    """
    HANGMAN_PHOTOS = {0: """
    x-------x""", 1: """
    x-------x
    |
    |
    |
    |
    |""", 2: """
    x-------x
    |       |
    |       0
    |
    |
    |""", 3: """
    x-------x
    |       |
    |       0
    |       |
    |
    |""", 4: """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", 5: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""", 6: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}
    print(HANGMAN_PHOTOS[num_of_tries], "\n")


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Checks if the guess is a correct character,
    If it is correct it adds the character to the guess list,
    and if not it prints X and the guess list
    :parm letter_gussed: the input of guessing letter
    :parm old_letters_guessed: list of previous guesses
    :type letter_gussed: str
    :type old_letters_guessed: list
    :return: True or False if Updated list
    :rtype: bool
    """
    # Calls a function that checks if the character is correct
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        print(" -> ".join(sorted(old_letters_guessed)))
        return False


def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks if the guess is a correct character
    :parm letter_gussed: the input of guessing
    :parm old_letters_guessed: list of previous guesses
    :type letter_gussed: str
    :type old_letters_guessed: list
    :return: What are the test results, true or false
    :rtype: bool
    """
    if (len(letter_guessed) == 1) and (letter_guessed.isalpha()) and (letter_guessed.lower() not in old_letters_guessed):
        return True
    else:
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    """Print the secret word, but only the letters guessed, the rest
    as underlines
    :parm secret_word: The word the player has to guess
    :parm old_letters_guessed: list of previous guesses
    :type secret_word: str
    :type old_letters_guessed: list
    :return: None
    """
    hidden_word_list = []
    for x in secret_word:
        if x in old_letters_guessed:
            hidden_word_list.append(x)
        else:
            hidden_word_list.append("_")
    hidden_word = " ".join(hidden_word_list)
    print(hidden_word, "\n")


def check_win(secret_word, old_letters_guessed):
    """Checks if the player has guessed the whole secret word and won
    :parm secret_word: The word the player has to guess
    :parm old_letters_guessed: list of previous guesses
    :type secret_word: str
    :type old_letters_guessed: list
    :return: Did he win yes or no
    :rtype: bool
    """
    win = True
    for x in secret_word:
        if x not in old_letters_guessed:
            win = False
    return win


def main():
    opening_screen()  # Prints an opening screen
    words_file = input("Enter file path: ")
    word_index = int(input("Enter index: "))
    print("\nLet’s start! \n")
    # Selects the secret word from the file
    secret_word = choose_word(words_file, word_index)
    num_of_tries = 0
    print_hangman(num_of_tries)  # Prints the Hangman image
    old_letters_guessed = []
    # Prints underlines as the number of characters of the secret word
    show_hidden_word(secret_word, old_letters_guessed)
    # Checks if the game is over, and if not the game is running
    while not check_win(secret_word, old_letters_guessed) and num_of_tries < 6:
        guess_letter = input("Guess a letter: ")
        # Checks if the input is a valid character םr already guessed
        if try_update_letter_guessed(guess_letter, old_letters_guessed):
            # Checks if the guess is incorrect
            if guess_letter.lower() not in secret_word:
                num_of_tries += 1
                print(":(")
                print_hangman(num_of_tries)  # Prints the Hangman image
            # Print the secret word, only the letters guessed, the rest as underlines
            show_hidden_word(secret_word, old_letters_guessed)
    # Checks if the player has won or lost the game
    if check_win(secret_word, old_letters_guessed):
        print("WIN")
    else:
        print("LOSE")

if __name__ == "__main__":
    main()
