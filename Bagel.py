"""
Description:
In Bagels, a deductive logic game, you
must guess a secret three-digit number
based on clues. The game offers one of
the following hints in response to your guess:
“Pico” when your guess has a correct digit in the
wrong place, “Fermi” when your guess has a correct
digit in the correct place, and “Bagels” if your guess
has no correct digits. You have 10 tries to guess the
secret number.
"""

try:
    import random
except ImportError as imp_err:
    print("Import Error..... Script Stopped; {}".format(imp_err))
    exit(1)


class Bagels:

    def __init__(self):
        self.NUM_DIGIT = 3
        self.MAX_GUESS = 10

    def main(self):
        """

        :return:
        """
        notes = """Bagels, a deductive logic game. 
        I am  thinking of a {}-digit number with no repeated digits.
        Try to guess what it is. Here are some clues:
        When I say: 
        That means:
        Pico One digit is correct but in the wrong position.
        Fermi One digit is correct and in the right position.
        Bagels No digit is correct.
        For example, if the secret number 
        was 248 and your guess was 843, the 26. clues would be Fermi Pico. 
        """.format(self.NUM_DIGIT)
        print(notes)

        while True:

            secretnum = self.getSecretNum()
            print("I have thought of number")
            print("you have {} guess to find it".format(self.MAX_GUESS))

            count = 1
            while count <= self.MAX_GUESS:
                guess = ''
                while len(guess) != self.NUM_DIGIT or not guess.isdecimal():
                    print("Guess#{}:".format(count))
                    guess = input(">")

                clues = self.getClues(guess, secretnum)
                print(clues)
                count += 1

                if guess == secretnum:
                    break
                elif count > self.MAX_GUESS:
                    print("You ran out of guesses")
                    print("Correct Answer is {}".format(secretnum))

            print("Do you want to play again ? (Y/N)")
            if not input(">").lower().startswith('y'):
                break

        print("Thank You")

    def getSecretNum(self):

        """
        return string made up of NUM_DIGIT unique random numbers.

        :return:str secretnumber
        """
        numbers = list('0123456789')
        random.shuffle(numbers)
        secretnum = ''
        for i in range(self.NUM_DIGIT):
            secretnum += numbers[i]

        return secretnum

    def getClues(self, guess, secretnum):

        if guess == secretnum:
            return 'You got It!!'

        clues = []

        for i in range(len(guess)):
            if guess[i] == secretnum[i]:
                clues.append("Fermi")
            elif guess[i] in secretnum:
                clues.append('Pico')
        if len(clues) == 0:
            return 'Bagels'
        else:
            clues.sort()
            return " ".join(clues)


if __name__ == '__main__':
    obj = Bagels()
    obj.main()
