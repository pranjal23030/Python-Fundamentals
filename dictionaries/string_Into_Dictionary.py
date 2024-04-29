word = input("Enter a name: ")

d = {}

for ch in word:
    if ch not in d:
        d[ch] = 1
    else:
        d[ch] += 1

print(d)