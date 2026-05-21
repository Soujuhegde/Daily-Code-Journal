# writing data into file

file = open("sample.txt", "w")

file.write("Python practice programs")

file.close()

# reading data from file

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()