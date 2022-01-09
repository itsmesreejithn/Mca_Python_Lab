#area of square
areaSquare = lambda s : s * s

#area of rectangel
areaRectangle = lambda l, b: l * b

#area of trinagle
areaTriangle = lambda b, h: (b * h)/2

#getting input from user
sideOfSquare = int(input("Enter the side of square: "))
print('Area of square is', areaSquare(sideOfSquare))

length = int(input("Enter the length of rectangle: "))
breadth = int(input("Enter the breadth of rectangle: "))
print('Area of rectangle',areaRectangle(length, breadth))

base = int(input("Enter the base of triangle: "))
height = int(input('Enter the height of tirangle: '))
print('Area of triangle', areaTriangle(base, height))
