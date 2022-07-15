HANGMAN_ASCII_ART = """ 
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                        __/ |
                       |___/
"""
MAX_TRIES = 6

HANGMAN_PHOTOS = {
    0: """x-------x""",
    1: """    x-------x
    |
    |
    |
    |
    |""",
    2: """    x-------x
    |       |
    |       0
    |
    |
    |""",
    3: """    x-------x
    |       |
    |       0
    |       |
    |
    |""",
    4: """x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    5: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / 
    |""",
    6: """x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}


def check_win(secret_word, old_letters_guessed):
    """
    This function check if there a win
    :param secret_word: the secret word
    :param old_letters_guessed: the letters that guessed 
    :type secret_word: str
    :type old_letters_guessed: str
    :return: if there is a win
    :rtype: bool
    """
    guessed_letters = []
    for char in secret_word:
        if old_letters_guessed.count(char) >= 1:
            guessed_letters.append(char)

    if len(guessed_letters) == len(secret_word):
        return True
    else:
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    """
    This function print the hidden word with the letters that guessed
    :param secret_word: the secret word
    :param old_letters_guessed: the letters that guessed 
    :type secret_word: str
    :type old_letters_guessed: str
    :return: the hidden word
    :rtype: str
    """
    hidden_word = []
    for char in secret_word:
        if old_letters_guessed.count(char) >= 1:
            hidden_word.append(char)
        else:
            hidden_word.append("_")
    return " ".join(hidden_word)


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    This function get letter and list of guessed letters and return true if this valid and false either
    :param letter_guessed:
    :param old_letters_guessed:
    :type letter_guessed: str
    :type old_letters_guessed: list of str
    :return: True/False
    :rtype: bool
    """
    if not letter_guessed.isalpha() or len(letter_guessed) > 1:
        return False
    elif letter_guessed in old_letters_guessed:
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    :param letter_guessed:
    :param old_letters_guessed:
    :type letter_guessed: str
    :type old_letters_guessed: list of str
    :return: True/False
    :rtype: bool
    """
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print("X")
        print(" -> ".join(sorted(old_letters_guessed)))
        return False
    else:
        old_letters_guessed.append(letter_guessed)
        return True


def choose_word(file_path, index):
    """
    This function get 2 params the first file path where the file is and the second is the index num
    it's return a tuple the has:
    1. the num of word (non duplicates)
    2. guessed word by the provided index
    :param file_path: the file path
    :param index: the number of the word to be guessed
    :type file_path: str
    :type index: int
    :return: a tuple with the num of word (non duplicates) and the guessed word
    :rtype: tuple
    """
    file = open(file_path, "r")
    results_tuple = ()
    for line in file:
        num_of_words = len(list(dict.fromkeys(line.split())))
        while index > len(line.split()):
            index = index - len(line.split())
        results_tuple = (num_of_words, line.split()[index - 1])

    return results_tuple


def print_hangman(num_of_tries):
    """
    This function gets number of tries and print the hangman according to the level
    :param num_of_tries: The number of tries (means num of fails)
    :type num_of_tries: int
    :return: none
    """
    print(HANGMAN_PHOTOS[num_of_tries])


def is_letter_in_secret(letter_guessed, secret_word):
    """
    This function get letter and check if the letter in the secret word
    :param letter_guessed: the letter that guessed
    :param secret_word: the secret word
    :type letter_guessed: str
    :type secret_word: str
    :return: letter in or not
    :rtype: bool
    """
    if letter_guessed not in secret_word:
        print(":(")
        return False
    else:
        return True


def main():
    print(HANGMAN_ASCII_ART)
    file_path = input("Enter file path: ")
    word_index = int(input("Enter index: "))
    secret_word = choose_word(file_path, word_index)[1]
    old_letters_guessed = []
    num_of_tries = 0

    print("Let's Start!")
    print_hangman(0)
    print(show_hidden_word(secret_word, old_letters_guessed))

    while not num_of_tries == MAX_TRIES and not check_win(secret_word, old_letters_guessed):
        letter_guessed = input("Guess a letter: ").lower()
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if not is_letter_in_secret(letter_guessed, secret_word):
                num_of_tries += 1
                print_hangman(num_of_tries)
                print(show_hidden_word(secret_word, old_letters_guessed))
            else:
                print(show_hidden_word(secret_word, old_letters_guessed))

    if check_win(secret_word, old_letters_guessed):
        print("WIN")
    else:
        print("LOSE")


if __name__ == "__main__":
    main()