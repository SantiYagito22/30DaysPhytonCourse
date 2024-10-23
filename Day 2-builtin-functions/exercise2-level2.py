import math

num_one = 5
num_two = 4
print('Number one: ', num_one)
print('Number two: ', num_two)

total= num_one + num_two
print('Sum :', total)

diff= num_one - num_two
print('Diff :', diff)

product = num_one * num_two
print('Product :', product)

division = num_one / num_two
print('Division: ', division)

remainder = num_one % num_two
print('Remainder: ', remainder)

exp = pow(num_one, num_two)
print('Exponent: ', exp)

floor_division = num_one // num_two
print('Floor division: ', floor_division)

radius = int(input('Insert the radius of the circle: '))

area_of_circle = math.pi * pow(radius, 2)
print('Area of circle: ', area_of_circle)

circum_of_circle = 2 * math.pi * radius
print('Circumference of circle: ', circum_of_circle)