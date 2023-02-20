# Python program to find the H.C.F of two numbers

# define a function
def computer_hcf(x, y):

# choose the smaller number

    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if((x%i==0)and (y%i==0)):
            hcf=i
    return hcf

num1=int(input('Enter first number: '))
num2=int(input('Enter second number: '))

print('The H.C.F. is',computer_hcf(num1,num2))