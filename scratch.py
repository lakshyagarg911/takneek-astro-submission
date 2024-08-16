import math

semi_major = 1.5 * (10.0**11)
grav_constant = 6.674 * 10.0 ** (-11)
mass = 1.989 * 10.0 ** 30

time = 2 * math.pi * math.sqrt(semi_major ** 3 / (grav_constant * mass))
print(time, "seconds")