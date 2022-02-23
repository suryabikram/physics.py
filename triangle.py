# This is a sample Python script.
# to import math  value
import math


# to check if  triangle is equilateral or not
def is_valid_triangle(a, b, c):
    if a == b == c:
        return True
    else:
        return False


# to verify triangle is rather equilateral or right triangle
def type_of_triangle(a, b, c):
    if a == b and b == c:
        print('this is an equilateral triangle')
    else:
        print("this is not an equilateral triangle.")
        print("this is right triangle.")


# Reading Three Sides ( to get the input of the length of triangle sides.)
a = float(input(' please enter side a: '))
b = float(input(' please enter side b: '))
c = float(input(' please enter side c: '))

print("True", a == b == c)
print("Hypotenuse is", math.sqrt(a ** 2 + b ** 2))  # using  simple Pythagorean theorem
if is_valid_triangle(a, b, c):
    type_of_triangle(a, b, c)
else:
    print('this is not an equilateral triangle \
               this is right triangle ')