"""
    A module demonstrating vowel and consonants count 
"""

import string

vowels = "aeiou"

cons = []


# print(type(string.ascii_lowercase))
for _char in string.ascii_lowercase:
    # if _char not in "aeiou":
    if _char not in vowels:
        cons.append(_char)

        

print(cons)

##_consonants = "".join(cons)
### print(_consonants)
###print(_consonants)
######
##
##vowel_count = 0
##consonant_count = 0
##sentence = input("Please enter a sentence: ")
##
##for char in sentence.lower():
##    if char == " " or char == "." or char == '_':
##        print("Specials")
##
##    if char in vowels:
##        vowel_count += 1
##    if char in _consonants:
##        consonant_count += 1
##    
##print("Vowel count: ", vowel_count)
##print("Consonants count: ", consonant_count)
####        
##
