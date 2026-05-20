# searching element using linear search

numbers = [10, 20, 30, 40]

target = 30

found = False

for num in numbers:

    if num == target:
        found = True
        break

print(found)