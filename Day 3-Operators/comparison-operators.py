print(4 >= 3) #True
print(4 >= 4) #True
print(4 < 3) #False
print(len('chips') == len('fish')) #False
print(len('chip') == len('fish')) #True
print(len('Nintendo') != len('Sony')) #True
print(True == True) #True
print(True == False) #False

print('1 is 1', 1 is 1) #True... is-> Both objects are equal, the same as ==
print('1 is not 2', 1 is not 2) #True... is not-> Both objects are not equal, the same as !=
print('8 is 2 ** 3', 8 is 2 ** 3) #True

# in-> If the list contains the certain item
print('a in Santiago', 'a' in 'Santiago') #True
print('s in Santiago', 's' in 'Santiago') #False
print('Hello in Hello world!', 'Hello' in 'Hello world!') #True
print('1 in [1, 2, 3]', 1 in [1, 2, 3]) #True
print('1 in [1, 2, 3]', 1 in [0, 2, 3]) #False

#logical operators
print(2 > 1 and 10 > 9) #And -> Both statements true...Result:True
print(2 > 1 or 1 > 2) #Or -> Both or one statement true... Result:True
print(not 2 > 1) #Negate the result... Result:False

'''
False * False = True
False * True = False
''' 