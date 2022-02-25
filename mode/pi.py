tolerance = float(input("Enter the tolerance: "))
pi = 0
i = 0
while 4 / (2 * i + 1) >= tolerance:
    pi += ((-1) ** i) * 4 / (2 * i + 1)
    i += 1
print("The approximation of pi is:", pi)