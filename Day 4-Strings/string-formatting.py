# %s -> String
console = 'Nintendo'
game = 'Super Mario'
fav_game = 'League of Legends'
formatted_string = 'I have a %s console with the %s game, but my favorite game is %s' %(console, game, fav_game)
print(formatted_string)

# %d - Integers
num_games = 30
formatted_string = 'I have %d games' %(num_games)
print(formatted_string)

# %f - Float
# %.number of float digits
degree = 100.5
formatted_string = 'The temperature reach %.2f degrees' %(degree)
print(formatted_string)

#It works with list as well
games = ['The Legend Of Zelda', 'The Last of Us', 'Lies of P']
formatted_string = 'My most played games are: %s' %(games)
print(formatted_string)