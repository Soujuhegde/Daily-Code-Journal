# binary search program

numbers = [10, 20, 30, 40, 50]

target = 40

low = 0
high = len(numbers) - 1

while low <= high:

    mid = (low + high) // 2

    if numbers[mid] == target:
        print("Found")
        break

    elif numbers[mid] < target:
        low = mid + 1

    else:
        high = mid - 1
