Animals = ['cat','dogs','monkey','horses','buffaloes']
k = 'cat' in Animals# here I use in and not in to search for values in the list

print(k)
for i in range (len(Animals)):
    print('index '+ str(i) + ' in animals is : ' + Animals[i])

cat = ['Loud','Black','Loud']
size , color ,disposition = cat
print(cat)