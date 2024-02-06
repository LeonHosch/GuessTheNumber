import random

class game:
    
    def __init__(self):
        self.wins = 0
        self.loses = 0

    def ranGame(self, maxnum, guesses):
        number = random.randint(0, maxnum)
        
        while guesses > 0:
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
    
if __name__ == "__main__":
    print("Welcome to GuessTheNumber PyObject Ed.")
    theGame = game()

    while True:
        try:
            userchoice = int(input("\nWhat do you want to do?\n1) Play the game standard edition\n2) Play the game with custom rules\n3) Print Statistics\n4) End the program\n\nInput: "))
        except:
            print("ERROR: Input not int")
        
        if userchoice == 1:
            theGame.standard()
        elif userchoice == 2:
            theGame.custom()
        elif userchoice == 3:
            print("You found a bug, this feature is not available yet")
        elif userchoice == 4:
            break
    
    print("Thank you for playing the game, see you next time :)")