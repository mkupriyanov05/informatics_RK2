"""task1"""
line = input('Enter a string: ')
COUNT = 0

for symbol in line:
    if symbol in ('a', 'e', 'i', 'o', 'u'):
        COUNT += 1

print(COUNT)
