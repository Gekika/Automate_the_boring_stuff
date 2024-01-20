#we import the module random to help use randomize our numbers
import random
#we initialize our secret number and provide a range there
Secret_number = random.randint(1,30)
print("I am thinking of a number between 1 and 30")

for guess_times in range(1,8):
    guess = int(input())
    print("Guess a number")
    
    if guess < Secret_number:
        print("Your Guess is too low, give it another try")
    elif guess >Secret_number:
        print("Your Guess is too high, give it another try")
    else:
      break    
    
#now he have the input and we compare to see if the number is guessed correctly
if guess == Secret_number:
    print("You are correct after "+str(guess_times)+ " guesses") 
else:
    print("You got it wrong my number was "  + str(Secret_number) + " have fun")  
    
print(f"Secret_number: {Secret_number}")    
     