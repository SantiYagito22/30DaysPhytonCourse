# Tuples are ordered and unchangeable(immutable), we cannot change its values

# There are 2 ways to create a Tuple
empty_tuple = ()
empty_tuple = tuple()
games = ('The Legend Of Zelda', 'The Last of Us', 'Lies of P')

# Len -> Return the size of the tuple
games = ('The Legend Of Zelda', 'The Last of Us', 'Lies of P')
print(f'I have played {len(games)} games')

# [index] to access the item in the given index,  0 is the start and len - 1 is the end of the array
games = ('The Legend Of Zelda', 'The Last of Us', 'Lies of P')
first_game = games[0]
last_game =  games[len(games) - 1]
print(f'Positive index: My first game is {first_game} and my last game is {last_game}')

# We can access with negative numbers as well, -1 is the last item, -len is the fist item
games = ('The Legend Of Zelda', 'The Last of Us', 'Lies of P')
first_game = games[-len(games)]
last_game =  games[-1]
print(f'Negative index: My first game is {first_game} and my last game is {last_game}')

# Slicing
games = ('The Legend Of Zelda', 'The Last of Us', 'Lies of P')
second_game = games[1:2] #With negative index would be games[-2:-1]
all_games = games[0:] #With negative index would be games[-3:]
print(second_game)
print(all_games)

# Change tuple to list
games = ('The Legend Of Zelda', 'The Last of Us', 'Lies of P')
games = list(games)
games.append('Super Mario Bros')
print(f'Games as list: {games}')

# Checking if item exists
games = ('The Legend Of Zelda', 'The Last of Us', 'Lies of P')
does_exist = 'Lies of P' in games
print(does_exist)
does_exist = 'Super Mario Bros' in games
print(does_exist)

#Joining tuples

# Plus operator(+)

tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
zero = ( 0, ) #In this way, you can create a tuple with unique value. If we dont use comma, it will be interpreted as a int
sequence = zero + tuple_1 + tuple_2
print(sequence)

# Del -> Unlike a list, we cannot remove a specified item, however, we can delete the whole tuple
games = ('The Legend Of Zelda', 'The Last of Us', 'Lies of P', 'Super Mario', 'League of Legends')
del games
