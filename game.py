import random
import time

class game:
    
    def __init__(self):
        self.wins = 0
        self.loses = 0

    def ranGame(self, maxnum, guesses):
        number = random.randint(0, maxnum)
        
        while guesses > 0:
            print(f"You have {guesses} guess/es left")
            while True:
                try:
                    userGuess = int(input("Which number do you think I chose?\nInput: "))
                    break
                except:
                    print("ERROR: Input not int")
            
            if userGuess == number:
                print(f"Wow you won, the number indeed was {number}!")
                self.wins += 1
                return
            elif userGuess > number:
                print("Nope, the number is lower than your guess")
            else:
                print("Number is higher than the guessed number")

            guesses -= 1

        print(f"Seems like you lost, sorry :(\nNumber was: {number}")
        self.loses += 1
        return

    def standard(self):
        self.ranGame(100, 5)
        return

    def custom(self):
        while True:
            try:
                maxnum = int(input("What is the highest number I should be able to choose?\nInput: "))
                guesses = int(input("How many guesses do you want to have?\nInput: "))
                break
            except:
                print("ERROR: Last input not int")
        self.ranGame(maxnum, guesses)
        return
    
    def stats(self):
        print(f"\nYOUR GAMESTATS:\nWins:\t{self.wins}\nLoses:\t{self.loses}\n")
        return
    
    def turnaround(self):
        while True:
            try:
                number = 101
                while number > 100 or number < 0:
                    number = int(input("What is your secret number? (Must be between 0 and 100)\nInput: "))
                break
            except:
                print("ERROR: Input not int")

        guesses = 6
        maxguess = 100
        lowguess = 0

        while guesses > 0:
            print(f"Computer has {guesses} guess/es left")
            guess = random.randint(lowguess, maxguess)
            time.sleep(2)

            print(f"\nComputer guessed {guess}")
            time.sleep(2.5)
            if guess == number:
                print("It was your number! Computer won!")
                time.sleep(2)
                self.loses += 1
                return
            elif guess > number:
                print("It's higher than your number")
                maxguess = guess - 1
            else:
                print("It'S lower than your number")
                lowguess = guess + 1

            guesses -= 1
        
        self.wins += 1
        return
    
if __name__ == "__main__":
    print("Welcome to GuessTheNumber PyObject Ed.")
    theGame = game()

    while True:
        try:
            userchoice = int(input("\nWhat do you want to do?\n1) Play the game standard edition\n2) Play the game with custom rules\n3) Print Statistics\n4) Computer guesses your number\n5) End the program\n\nInput: "))
        except:
            print("ERROR: Input not int")
        
        if userchoice == 1:
            theGame.standard()
        elif userchoice == 2:
            theGame.custom()
        elif userchoice == 3:
            theGame.stats()
        elif userchoice == 4:
            theGame.turnaround()
        elif userchoice == 5:
            break
    
    theGame.stats()
    print("Thank you for playing the game, see you next time :)")