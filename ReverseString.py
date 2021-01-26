inp = input("Enter a String: ")

newString = ""

for i in range(len(inp)):
    char = inp[len(inp) - i -1]
    newString+=char
    
print("This is your backwards string:", newString)
