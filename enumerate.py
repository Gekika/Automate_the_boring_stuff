# instead of using the range in the for loop we can use this 
Grades = ['12','13','14','15','16','17']
for index ,item in enumerate(Grades):
    print("Index " +str(index)+' in supplies is : '+item)
print(id(Grades))    