Cat_Names = []#Initializes an empty list to store cat names
while True:#the main loop
    print('Enter the name of cat ' + str(len(Cat_Names) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == "":# if the name is empty we break out of the loop 
        break
    # if a name is added it is then concatenaed  on the list"Ctanames
    Cat_Names = Cat_Names +[name]
    print("The cat names are: ")
    # this loop iterates on each cat name in teh Catname list and prints it
    for name in Cat_Names:
        print(''+name)
        
        
        
        
        