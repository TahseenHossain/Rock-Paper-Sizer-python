from random import choice

options = list(range(1,4))

play = True
while play:
    print("1 for Rock")
    print("2 for Paper")
    print("3 for Scissors")
    player = int(input("Enter your choice: "))
    while player not in options:
        print("Wrong Input\nInput has to be between (1-3)")
        player = int(input("Enter your choice: "))
    computer = choice(options)
    if(computer == player):
        print("It's a tie")
    elif(computer == 1 and player == 2):
        print("You win \nComputer: Rock\nPlayer: Paper")
    elif(computer == 2 and player == 3):
        print("You win \nComputer: Paper\nPlayer: Scissors")
    elif(computer == 3 and player == 1):
        print("You win \nComputer: Scissors\nPlayer: Rock")
    else:
        print("You lost")

    playing = input("Play again?(y/n):")
    if(playing == 'n'):
        play = False