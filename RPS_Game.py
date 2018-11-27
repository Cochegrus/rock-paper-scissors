## Program to simulate a game of rock, paper, scissors between computer and user
## Code written by Jordi A. Cochegrus

import random

print('Let\'s play "Rock, Paper, Scissors"!'
      '\nEnter "rock", "paper" or "scissors" to pick your hand.'
      '\nYou are playing for best out of three!')
start = input('Press "Enter" to start. Enter any key to quit. ')
playerWins = 0  # records number of games won by user
cpuWins = 0  # records number of games won by computer

while start == "":
    while not playerWins == 2 and not cpuWins == 2:
        tie = 1  # lets program repeat the round until either user or computer wins
        while tie == 1 and start == "":
            cpu = random.randint(1,3) #1 = scissors, 2 = rock, 3 = paper
            userString = input("\nROCK!\nPAPER!\nSCISSORS!\n")
            userString = userString.lower()

            if userString == "rock":
                if cpu == 1: #scissors
                    print("YOU WIN!")
                    tie = 0
                    playerWins += 1
                elif cpu == 2: #rock
                    print("TIE!\n")
                else: #paper
                    print("YOU LOSE!")
                    tie = 0
                    cpuWins += 1

            elif userString == "paper":
                if cpu == 2: #rock
                    print("YOU WIN!")
                    tie = 0
                    playerWins += 1
                elif cpu == 3: #paper
                    print("TIE!\n")
                else: #scissors
                    print("YOU LOSE!")
                    tie = 0
                    cpuWins += 1

            elif userString == "scissors":
                if cpu == 3: #paper
                    print("YOU WIN!")
                    tie = 0
                    playerWins += 1
                elif cpu == 1: #scissors
                    print("TIE!\n")
                else: #rock
                    print("YOU LOSE!")
                    tie = 0
                    cpuWins += 1

            else:
                print("That's a weird hand...\nYou can only use rock, paper or scissors!")
                start = input('Press "Enter" if you want to keep playing. If you want to quit, enter any other key.')
                if not start == "":  # ends game
                    print("\nThanks for playing my game!")
                    exit(0)

    if cpuWins == 2:
        print("\nGood game. Better luck next time!")
        start = input('Press "Enter" if you want play again. If you want to quit, enter any other key. ')

    else:  # playerWins == 2:
        print("\nGood game. I'll get you next time!")
        start = input('Press "Enter" if you want to play again. If you want to quit, enter any other key. ')

    cpuWins = 0
    playerWins = 0

print("\nThanks for playing my game!")
