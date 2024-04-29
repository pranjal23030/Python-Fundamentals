
numbers = []
for i in range(1, 30):
    if i % 3 == 0:
        numbers.append(i)
    else:
        numbers.append(0)

##print(numbers)

numbers = [i if i % 3 == 0 else 0 for i in range(1, 30)]










# Odd numbers in range(1, 30)

odd_nums = []

for num in range(1, 30):
    if num%2 != 0:
        odd_nums.append(num)

print(odd_nums)


odd_nums = [num for num in range(1, 30) if num%2 != 0]
print(odd_nums)
##
##even_nums = [num for num in range(1, 30) if num%2 == 0]
##
##
##numbers2 = [i if i % 3 == 0 else 0  for i in range(1, 30) if i % 2 == 0]


### dictionary comprehension
print({k: k ** 2 for k in range(1, 9)})

### set comprehension
#print({i % 3 for i in range(1, 9)})
##
