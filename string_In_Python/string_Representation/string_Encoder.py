print("This program prints the ASCII representation of the input text")
message = input("Enter text: ")

for ch in message:
    print(ord(ch), end=" ")
print()