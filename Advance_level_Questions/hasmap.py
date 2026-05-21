# two sum problem

numbers = [2, 7, 11, 15]

target = 9

seen = {}

for i in range(len(numbers)):

    diff = target - numbers[i]

    if diff in seen:

        print(seen[diff], i)

    seen[numbers[i]] = i