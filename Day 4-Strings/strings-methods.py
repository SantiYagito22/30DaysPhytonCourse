#capitalize -> Convert the first letter of the String to capital letter
sentence = "hello world!"
print(sentence.capitalize())

#count -> Return occurrences of substrings, 3 parameters: 1. substring, 2. start = starting indexing to count, 3. end = the last index to count
print(sentence.count('o')) # 2
print(sentence.count('o', 4, 7)) #1

#endswith -> check if a string ends with a specified ending
print(sentence.endswith('world!')) #True
print(sentence.endswith('world')) #False

#expandtabs -> replace tab character with spaces, we can pass the tab size by argument(default 8)
sentence_b = 'hello\tmy\tname\tis\tSantiago'
print(sentence_b.expandtabs())
print(sentence_b.expandtabs(20))

#find -> return the index of the first occurrence of a substring, if not exists return -1, same arguments as count
print(sentence.find('w')) # 6
print(sentence.find('x')) # -1

#rfind -> The same as find but it returnS the LAST occurrence, same arguments as count
print(sentence.rfind('o')) # 7
print(sentence.rfind('x')) # -1

#index -> The same as find, but it returns error if it doesn't find anything 
print(sentence.index('ll')) #2
#print(sentence.index('ll', 5)) #error

#rindex -> The same as rfind, but it returns error if it doesn't find anything 
print(sentence.rindex('ld')) #9
#print(sentence.rindex('ll', 6)) #error

#isalnum -> Checks if the string is alphanumeric
sentence_b = sentence_b = "I have twenty cats"
print(sentence_b.isalnum()) #False 
sentence_b = "Ihave20Cats"
print(sentence_b.isalnum()) #True

#isdecimal -> Checks if all characters are decimal(0-9)
sentence_b = "I have twenty cats"
print(sentence_b.isdecimal()) #False

#isdecimal -> Checks if all characters are decimal(0-9)
sentence_b = "12 3" 
print(sentence_b.isdecimal()) #False, spaces are not allowed
sentence_b = "123" 
print(sentence_b.isdecimal()) #True

#isdigit -> Checks if all characters are numbers(0-9 and some other unicode characters for numbers)
sentence_b = "12 3" 
print(sentence_b.isdigit()) #False, spaces are not allowed
sentence_b = "\u00B2" 
print(sentence_b.isdigit()) #True

#isnumeric -> The same as isdigit but it accepts more symbols
sentence_b = "12 3" 
print(sentence_b.isnumeric()) #False, spaces are not allowed
sentence_b = "\u00BD" 
print(sentence_b.isnumeric()) #True

#isidentifier -> Checks if a string is a correct variable name
sentence_b = "personal_name" 
print(sentence_b.isidentifier()) #True
sentence_b = "24_personal_name" 
print(sentence_b.isidentifier()) #False

#islower -> Checks if all characters are lowe case
sentence_b = "hello"
print(sentence_b.islower()) #True
sentence_b = "Hello"
print(sentence_b.islower()) #False

#isupper -> Checks if all characters are upper case
sentence_b = "HEllo"
print(sentence_b.isupper()) #False
sentence_b = "HELLO"
print(sentence_b.isupper()) #True

#join -> Returns a concatenated string
games = ['The Legend Of Zelda', 'The Last of Us', 'Lies of P']
result = '-'.join(games)
print(result)

#strip -> Remove al given characters
print(sentence.strip('hel')) #o world!

#replace -> Replace substrings with the given string
print(sentence.replace('hello', 'Hi')) #Hi world!

#split -> Split the string, the arguments has to be the separator(default is space)
sentence_b = 'My name is Santiago'
print(sentence_b.split()) # ['My', 'name', 'is', 'Santiago']
sentence_b = 'Water, meat, eggs, milk, candies'
print(sentence_b.split(', ')) # ['Water', 'meat', 'eggs', 'milk', 'candies']

#title -> Returns a title cased string
sentence_b = 'My name is Santiago'
print(sentence_b.title()) # My Name Is Santiago

# swapcase -> coverts uppercase to lowercase and vice versa 
sentence_b = "My name is Santiago Muñoz Castro"
print(sentence_b.swapcase()) # mY NAME IS sANTIAGO mUÑOZ cASTRO

#startswith -> Checks if a string starts with the specified string
print(sentence.startswith('o')) #False
print(sentence.startswith('h')) #True

