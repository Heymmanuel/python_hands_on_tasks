import math
rad = float(input("Enter radius of circle: "))
pi = 3.141

dia = rad * 2
print(f'Diameter of circle = {dia}')

circum = (2 * pi * rad)
circumference = round(circum, 2)
print(f'Circumference of circle = {circumference}')

area = pi * rad ** 2
print(f'Area of circle = {area}')
