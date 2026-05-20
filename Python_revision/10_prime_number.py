num = 7

count = 0

for i in range(1, num + 1):

    # Checking divisibility
    if num % i == 0:
        count += 1

# Prime numbers have exactly 2 factors
if count == 2:
    print("Prime")

else:
    print("Not Prime")