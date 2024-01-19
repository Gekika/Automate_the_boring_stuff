while True:#keeps the loop running until the name Joe is typedJoe
      print('Who are you?')
      name = input()
      if name != 'Joe':
        continue # gets back to the loop above
      print('Hello, Joe. What is the password? (It is a fish.)')
      password = input()
      if password == 'swordfish':
         break
      print('Access granted.')   