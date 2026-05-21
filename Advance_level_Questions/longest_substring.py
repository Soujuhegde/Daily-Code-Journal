# longest substring without repeating characters

text = "abcabcbb"

longest = 0

for i in range(len(text)):

    seen = ""

    for j in range(i, len(text)):

        if text[j] not in seen:

            seen += text[j]

            longest = max(longest, len(seen))

        else:
            break

print(longest)