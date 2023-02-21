# Function to print binary number using recursionn

def convertToBinary(n):
    if n > 1:
        convertToBinary(n//2)
    print(n % 2, end='')


# decimal number
dec=int(input('Enter a binay number: '))

convertToBinary(dec)
print()