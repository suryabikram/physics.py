# This is a sample Python script.
# defining Momentum(M= m*v)
def Momentum(m, v):
    return (float(m) * float(v))

# Defining kinetic energy
def KineticEnergy(m, v):
    return ( float(1/2) * float(m) * float(v) * float(v))
# KE = 1/2 mv^2

M = input("Please input the Mass of the object(in kg):")

V = input("Please input the Velocity of the object(in meter per second):")

print(" the mass is " + str(M))

print(" the velocity is " + str(V))

print(" the momentum is " + str(Momentum(M, V)), "kg*m/s")

print(" the kinetic energy is " + str(KineticEnergy(M, V)) , "Joules")
