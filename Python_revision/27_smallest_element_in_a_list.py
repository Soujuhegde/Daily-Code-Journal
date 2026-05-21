# finding smallest element

numbers = [10, 45, 2, 78, 12]

smallest = numbers[0]

for num in numbers:

    if num < smallest:
        smallest = num

print(smallest)