# the 1st function which will do the calculations
def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else :
        result = 3* number + 1
    print(result)
    return result

# This is teh main function that other functions will be called through 

def main():
    while True:
        try :
             E_number = int(input("Enter a number"))
             while E_number != 1:              
                E_number = collatz(E_number)
             break 
        except ValueError:
            print("Invalid number")
            
if __name__ =="__main__":
    main()

      

