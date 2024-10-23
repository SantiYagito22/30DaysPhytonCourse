#open python version: py --version

#Euclidean distance

import math
a = (2, 3)
b= (10, 8)

euclidianDistance = math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))

print('The Euclidian Distance between (' + str(a[0]) + ',' + str(a[1])+ ')' + ' and ('+ str(a[0]) + ',' +str(a[1])+ ')' +' is '+ str(euclidianDistance))

#The Euclidian Distance between (2,3) and (2,3) is 9.433981132056603