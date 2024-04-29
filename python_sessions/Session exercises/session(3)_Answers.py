# Display all prime numbers from 1 to 100:

# print("Prime numbers from 1 to 100:")
# for num in range(2, 101):
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=" ")


# Checking a palindrome

# def check_palindrome(string):
#     string = string.replace(" ", '').lower()
#     return string == string[::-1]
#
#
# user_string = input("Enter string: ")
# if check_palindrome(user_string):
#     print("User string is pal")
# else:
#     print("User string is not pal")

# Count lowercase, uppercase, digits, and special symbols in a string:

def count_characters(string):
    lowercase = 0
    uppercase = 0
    digits = 0
    special_symbols = 0

    for character in string:
        if character.islower():
            lowercase += 1
        elif character.isdigit():
            digits += 1
        elif character.isupper():
            uppercase += 1
        else:
            special_symbols += 1
    return lowercase, uppercase, digits, special_symbols


user_string = input("String: ")
lowercase, uppercase, digits, special_symbols = count_characters(user_string)
print(f"Lowercase: {lowercase} Uppercase: {uppercase} Digits: {digits}, Special Symbols: {special_symbols}")

# Display n terms of harmonic series and their sum:

# def harmonic_sum(n):
#     harmonic_sum = 0
#     for i in range(1, n + 1):
#         harmonic_sum += 1 / i
#         print(f"1/{i}", end=" + " if i < n else " = ")
#     return harmonic_sum
#
#
# n = int(input("Enter the number of terms: "))
# result = harmonic_sum(n)
# print(f"{result:.6f}")

# Display the pattern with different rows:

# rows = int(input("Enter the number of rows: "))
# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "*" * i)

# Create a dictionary with letters and their occurrences in a string:

# def count_letters(string):
#     letter_counts = {}
#     for char in string:
#         if char.isalpha():
#             letter_counts[char.lower()] = letter_counts.get(char.lower(), 0) + 1
#     return letter_counts
#
#
# user_string = input("Enter a string: ")
# result = count_letters(user_string)
# print(result)

# user_string = input("Enter: ")
# d = {}
#
# for ch in user_string:
#     if ch not in d:
#         d[ch] = 1
#     else:
#         d[ch] += 1
# print(d)
