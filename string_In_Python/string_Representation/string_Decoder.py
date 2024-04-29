print("This program helps to decode the unicode codes.")
s = input("Enter number codes: ")
message = ""
for num_str in s.split():
    code_num = int(num_str)
    message = message + chr(code_num)
print("The decoded text is:", message)