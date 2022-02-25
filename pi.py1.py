import math
#  Enter the tolerance: .0001
# The approximation of pi is: 3.141592654

# obtain the value from the user
tolerance = float(input("Enter the tolerance: "))
# initial vlue of pi
pi = 0
i = 0
while 4 / (2 * i + 1) >= tolerance:
    pi += ((-1) ** i) * 4 / (2 * i + 1)
    i += 1
print("The approximation of pi is:", pi)