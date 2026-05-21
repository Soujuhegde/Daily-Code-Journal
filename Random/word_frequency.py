# word frequency

text = "python is easy python is powerful"

words = text.split()

freq = {}

for word in words:

    if word in freq:
        freq[word] += 1

    else:
        freq[word] = 1

print(freq)