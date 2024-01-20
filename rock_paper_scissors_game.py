# we import the required modules
import random, sys
print("WELCOME TO ROCK, PAPER, SCISSORS")
#initialize what we are to use in the game
wins = 0
loses = 0
ties = 0
#her is the main loop of the game(Anything within this loop repeats unless broken)
while True:
    print(f"{wins} Wins: ,{loses} Loses: ,{ties}Ties: ")
    
    
#here is the players input loop(after input is read we get out of this loop)
    while True:
        print("Enter move:(r)ock (p)aper (s)cissors or (q)uit")
        playermove = input()
        if playermove == 'q':
            sys.exit()#this makes the program to terminate when 'q' is pressed 
        if playermove == 'r' or playermove == 'p' or playermove == 's':
         break#(here we break the input loop)
        else:
            print("Type one of r, p, s, or q")
            
            
#we print out the users input choice
    if playermove == 'r':
         print('ROCK versus...')
    elif playermove == 'p':
        print('PAPER versus...')
    elif playermove == 's':
        print('SCISSORS versus...')
        
        
#The computers move and its displayed
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')
        
        
#how we will handle the outcomes
    if playermove == computerMove:
        print("Its a tie")
        ties += 1
    elif (playermove == 'r' and computerMove == 's') or (playermove == 'p' and computerMove == 'r') or (playermove == 's' and computerMove == 'p'):
        print('You win!')
        wins += 1
    else:
        print("You lose")
        loses += 1

        
     
               