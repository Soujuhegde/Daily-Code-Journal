# finding missing number in list

numbers = [1, 2, 3, 5]

n = 5

expected_sum = n * (n + 1) // 2

actual_sum = sum(numbers)

missing = expected_sum - actual_sum

print(missing)