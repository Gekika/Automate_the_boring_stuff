Create_Names = input("Enter Your name: ")
Pass = input("Enter a password: ")
Confirm_Pass = input("Confirm your password: ")
if Confirm_Pass == Pass :
  print(f"Welcome, {Create_Names}!, Account Succesfully created")
elif Confirm_Pass!= Pass:
  print("Failed!, Check your Password again")
  
  
while   Confirm_Pass == Pass:
  print("To login to your account, Enter your name ")
  Name = input("Enter Name here : ")
  break
if Name == Create_Names:
    print(f"Welcome {Name}, Enter your password")
    pass2 = input("Enter your password here!")
    if pass2 == Pass:
      print(f"{Name}, Welcome onboard feel at home")
      
else:
    print(f"No account for username,{Name}")
    