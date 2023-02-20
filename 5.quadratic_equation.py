# Solve the quadratic equation ax**2 +bx+c=0

# import complex math module
import cmath

a = int(input('Enter a first number: '))
b = int(input('Enter a second number: '))
c = int(input('Enter a third number: '))

# Calculate the discriminant
d = (b**2)-(4*a*c)

if d < 0:
    print('Imaginary')
else:
    # find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    print('The solution are {0} and {1}'.format(sol1, sol2))
