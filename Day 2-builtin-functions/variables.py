'''Rules to define variables in Python:
-It must start with a lowercase letter
-It cannot start with a number
-It can only contain alpha-numeric characters and underscores(A-z, 0-9 and _)
-They are case-sensitive(firstname !== Firstname)
'''

pet_name = "Sasha"
age = 2
is_beautiful= True

#print function can take unlimited parameters
print('VSCode', ',', len('Hello friend')) 

#Print the value of a variable
print('Name: ', pet_name) 
print('Name length: ', len(pet_name))

#Declaring multiple variables in the same line
pet_type, weight, diseases = 'Cat', 5, False 

print(pet_type, weight, diseases)

