'''the else statement
An if clause can be optionally followed with an else statment'''
# Structure -else keyword - colon -clause
name = input("Enter your name here")
if name == "George" :
    print("Welcome " + name )
#else:
#print("Who are You stranger")'''
    
elif name == "Karanja":
    print("I know you George")   

name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
    
#while loop