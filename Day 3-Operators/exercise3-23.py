for x in range(1, 6):
  print(str(x), end= " ")
  for y in range(4):
    print(str(pow(x, y)), end= " ")
  print('')

'''
Output: 
1 1 1 1 1 
2 1 2 4 8 
3 1 3 9 27 
4 1 4 16 64 
5 1 5 25 125 
'''