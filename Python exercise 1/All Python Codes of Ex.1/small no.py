first = float(input('Enter first number: '))
second = float(input('Enter second number: '))

# Making decision and displaying
if first < second:
    small = first
else:
    small = second

print('Smallest = %d' %(small))