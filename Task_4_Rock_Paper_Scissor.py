import random

def rock_logic(n):
    if n == 1:
        print('''Computer Choice is Rock and You choose Rock
        So No one Wins
        It's a Tie''')
    elif n == 2:
        print('''Computer Choice is Scissors and You choose Rock
        So You Win
        Congratulations, You Are the Winner''')
    else:
        print('''Computer Choice is Paper and You choose Rock
        So You Lose
        Better Luck Next Time''')

def scissor_logic(n):
    if n == 2:
        print('''Computer Choice is Scissors and You choose Scissors
        So No one Wins
        It's a Tie''')
    elif n == 3:
        print('''Computer Choice is Paper and You choose Scissors
        So You Win
        Congratulations, You Are the Winner''')
    else:
        print('''Computer Choice is Rock and You choose Scissors
        So You Lose
        Better Luck Next Time''')

def paper_logic(n):
    if n == 3:
        print('''Computer Choice is Paper and You choose Paper
        So No one Wins
        It's a Tie''')
    elif n == 1:
        print('''Computer Choice is Rock and You choose Paper
        So You Win
        Congratulations, You Are the Winner''')
    else:
        print('''Computer Choice is Scissors and You choose Paper
        So You Lose
        Better Luck Next Time''')

def play_game():
    n = random.randint(1, 3)
    ch = int(input('''Enter an operation you want to perform:
    Press 1 for Rock
    Press 2 for Scissors
    Press 3 for Paper
    \n'''))

    if ch == 1:
        rock_logic(n)
    elif ch == 2:
        scissor_logic(n)
    elif ch == 3:
        paper_logic(n)
    else:
        print("Invalid Input")

while True:
    play_game()
    again = input("Do you want to play again? Press Y to continue, or any other key to exit.\n")
    if again.lower() != 'y':
        break



    

        




    