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
'''What are the two values of the Boolean data type? How do you 
write them? True and  False....... 

2. What are the three Boolean operators?
or not and......

3. Write out the truth tables of each Boolean operator (that is, every 
possible combination of Boolean values for the operator and what 
they evaluate to).
4. What do the following expressions evaluate to?
(5 > 4) and (3 == 5) not (5 > 4) 
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
5. What are the six comparison operators?
6. What is the difference between the equal to operator and the assignment operator? 
7. Explain what a condition is and where you would use one.
8. Identify the three blocks in this code:
spam = 0
if spam == 10:
 print('eggs')
 if spam > 5:
 print('bacon')
 else:
 print('ham')
 print('spam')
print('spam')
9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is 
stored in spam, and prints Greetings! if anything else is stored in spam.
10. What keys can you press if your program is stuck in an infinite loop?
11. What is the difference between break and continue?
12. What is the difference between range(10), range(0, 10), and range(0, 10, 1)
in a for loop?
13. Write a short program that prints the numbers 1 to 10 using a for loop. 
Then write an equivalent program that prints the numbers 1 to 10 using 
a while loop.
14. If you had a function named bacon() inside a module named spam, how 
would you call it after importing spam?
 
'''