# valid parentheses problem

text = "()[]{}"

stack = []

pairs = {
    ")": "(",
    "]": "[",
    "}": "{"
}

valid = True

for char in text:

    if char in "([{":
        stack.append(char)

    else:

        if not stack or stack[-1] != pairs[char]:
            valid = False
            break

        stack.pop()

print(valid)