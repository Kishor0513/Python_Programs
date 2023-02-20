# Python program to find te fators of a number

# This function computers the factor of the argument passed
def print_factors(x):
    print('The fatcors of', x, 'are:')
    for i in range(1, x+1):
        if x % i == 0:
            print(i)


num = int(input('Enter a number: '))

print_factors(num)
