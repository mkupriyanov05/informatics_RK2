"""task2"""
line = input('Enter a string: ')
COUNT = 0

with open("stdin.txt", 'w', encoding='utf-8') as file_in:
    file_in.write(line)

for symbol in line:
    if symbol in ('a', 'e', 'i', 'o', 'u'):
        COUNT += 1

with open("stdout.txt", 'w', encoding='utf-8') as file_out:
    file_out.write(str(COUNT))

with open("stdout.txt", 'r', encoding='utf-8') as file_out:
    print(file_out.read())
