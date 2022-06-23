#Input
num1 = input('Enter value of first number (num1): ')
num2 = input('Enter value of second number (num2): ')

# create a temporary variable and swap the values
temp = num1
num1 = num2
num2 = temp

#Output
print('The value of num1 after swapping: {}'.format(num1))
print('The value of num2 after swapping: {}'.format(num2))