# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221]

# use anonymous function to filter
result = list(filter(lambda x: (x % 2 == 0), my_list))

# display the result
print('Number divisible by 2 are', result)
