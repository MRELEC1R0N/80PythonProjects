"""A deductive Lotgic game where you must guess a number based on clues."""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.
 
    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True:
        secretNum = getSecretNum()
        print("I have thought up a number")
        print("You have {} guesses to get it.".format(MAX_GUESSES))

        numGuess = 1
        while numGuess <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuess))
                guess = input("> ")

            clues = getClue(guess,secretNum)
            print(clues)
            numGuess += 1

            if guess == secretNum:
                break

            if numGuess > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break

    print("Thanks for playing!")



def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list("0123456789")
    random.shuffle(numbers)

    secretNum = ''
    for  i in random(NUM_DIGITS):
        secretNum += str(numbers[i])

    return secretNum




def getClue(guess , secretNum):
    "Return a string with the pico, femi , bagels clues for a guess and secret number pair"
    if guess == secretNum:
        return 'You got it '

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')

        elif guess[i] in secretNum:
            clues.append("Pico")

        if len(clues) ==0:
            return 'Bagels'

        else:
            clues.sort()
            return ''.join(clues)




if __name__ == "__main__":
    main()