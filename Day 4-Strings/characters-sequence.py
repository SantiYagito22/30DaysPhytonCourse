language = 'English'
a,b,c,d,e,f,g = language #unpacking sequence characters into variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

subject = 'Maths'
first_letter = subject[0]
print(f'First letter of {subject}: {first_letter}')

last_index = len(subject) - 1
last_letter = subject[last_index]
print(f'Last letter of {subject}: {last_letter}')

#Negative index to start from right to left
city = 'Granada'
last_letter = city[-1]
print(f'Last letter of {city}: {last_letter}')

#Slicing
food = 'Spaghetti'
first_four_letters = food[0:4] #Start at index 0 til index 4 without including it
print(f'First four letters of {food}: {first_four_letters}')
last_five_letters = food[-5:] #Start at index -5 since right and finish at the end because we don't specify other index.
print(f'Last five letters of {food}: {last_five_letters}')

print(food[0:len(food):2]) #This show the even letters of the string

#To reverse strin use [::-1]
message = 'I\'m 24 years old'
print(f'This is the reversed message of \"{message}\":  {message[::-1]}')