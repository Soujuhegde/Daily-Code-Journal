s = "soujanya"

count = 0

for i in s:

    if i.isalpha() and i.lower() not in "aeiou":
        count += 1

print(count)