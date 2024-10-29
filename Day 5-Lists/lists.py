# Lists are ordered, modifiable and allow duplicate members

# There are 2 ways to create a list, the next two lists are empty ones
list_1 = list()
list_2 = []

# len -> returns the size of the array
games = ['The Legend Of Zelda', 'The Last of Us', 'Lies of P']
print(games)
print(f'I have played {len(games)} games')

#List can have data of different data
list_1 = [30, True, "Hello", [1, 2, 3]]

# [index] to access the item in the given index,  0 is the start and len - 1 is the end of the array
games = ['The Legend Of Zelda', 'The Last of Us', 'Lies of P']
first_game = games[0]
last_game =  games[len(games) - 1]
print(f'Positive index: My first game is {first_game} and my last game is {last_game}')

# We can access with negative numbers as well, -1 is the last item, -len is the fist item
games = ['The Legend Of Zelda', 'The Last of Us', 'Lies of P']
first_game = games[-len(games)]
last_game =  games[-1]
print(f'Negative index: My first game is {first_game} and my last game is {last_game}')

# Unpacking 
games = ['The Legend Of Zelda', 'The Last of Us', 'Lies of P', 'Super Mario', 'League of Legends']
first_game, second_game, third_game, *rest = games
print(games)
print(f'First game: {first_game}, second game: {second_game}, third game: {third_game}, rest: {rest}')
first_game, second_game, *rest, last_game = games
print(games)
print(f'First game: {first_game}, second game: {second_game}, rest: {rest}, last game: {last_game}')

# Slicing
games = ['The Legend Of Zelda', 'The Last of Us', 'Lies of P']
second_game = games[1:2] #With negative index would be games[-2:-1]
all_games = games[0:] #With negative index would be games[-3:]
print(second_game)
print(all_games)

# Modifying 
games = ['The Legend Of Zelda', 'The Last of Us', 'Lies of P']
games[1]= 'Pokemon Red'
print(games)

# Checking if item exists
games = ['The Legend Of Zelda', 'The Last of Us', 'Lies of P']
does_exist = 'Lies of P' in games
print(does_exist)
does_exist = 'Super Mario Bros' in games
print(does_exist)

# Adding items -> append: add the item to end of the array
games = ['The Legend Of Zelda', 'The Last of Us', 'Lies of P']
games.append('Super Mario Bros')
print(games)

# Insert -> Add the item in the specified index
games = ['The Legend Of Zelda', 'The Last of Us', 'Lies of P']
games.insert(1, 'Super Mario Bros')
print(games)

# Removing items -> remove: delete a specified item from the list
games = ['The Legend Of Zelda', 'The Last of Us', 'Lies of P']
games.remove('The Legend Of Zelda')
print(games)

# Pop -> delete a item in the specified index (default delete the last item)
games = ['The Legend Of Zelda', 'The Last of Us', 'Lies of P']
games.pop()
print(games) 
games.pop(0)
print(games)

# Del -> Remove items in the specified index which can be a range, if we don't specify index the array will be completely deleted
games = ['The Legend Of Zelda', 'The Last of Us', 'Lies of P', 'Super Mario', 'League of Legends']
del games[1]
print(games)
del games[0:2]
print(games)
del games
#print(games) #Error because is not defined


# Clear -> Empties the list
games = ['The Legend Of Zelda', 'The Last of Us', 'Lies of P', 'Super Mario', 'League of Legends']
games.clear()
print(games)

# Copy a list, we can use the classic assignation: list1 = list2, list2 becomes a reference so any change will be reflected in list1

# To avoid the problem mentioned above, we use copy
games = ['The Legend Of Zelda', 'The Last of Us', 'Lies of P', 'Super Mario', 'League of Legends']
copy_games = games.copy()
copy_games.pop()
print(f'Original list: {games}')
print(f'Copy list: {copy_games}')

#Joining lists

# Plus operator(+)

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
zero = [0]
sequence = zero + list_1 + list_2
print(sequence)

# Extend method -> allow to append list in a list
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
zero = [0]
zero.extend(list_1)
zero.extend(list_2)
print(zero)

# Count -> Return the number of item apparitions 
list_1 = [22, 22, 3, 4, 22, 22, 5, 6]
print(list_1.count(1)) #0
print(list_1.count(22)) #4

# Index -> Return the index of a item in the list
list_1 = [22, 22, 3, 4, 22, 22, 5, 6]
print(f'Number 5 appears in the index number {list_1.index(5)}')

# Reverse -> Reverse the order of a list
list_1 = [1, 2, 3]
list_1.reverse()
print(list_1)

# Sort -> Reorder the list int ascending order modifying the original list, if the argument is true, the list will be arranged in descending order
list_1 = [22, 20, 3, 4, 2, 222, 5, 6]
list_1.sort()
print(f'List in ascending order: {list_1}')
list_1.sort(reverse=True)
print(f'List in descending order: {list_1}')
games = ['The Legend Of Zelda', 'The Last of Us', 'Lies of P', 'Super Mario', 'League of Legends']
games.sort()
print(f'Games in ascending order: {games}')

#Sorted -> The same as sort, but it doesn't modify the original list
list_1 = [22, 20, 3, 4, 2, 222, 5, 6]
print(sorted(list_1))
print(sorted(list_1, reverse=True))
print(list_1)