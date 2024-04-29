
import random
random.seed(12)

##def square(num):
##    return num**2

nums = [random.randint(1, 100) for i in range(10)]
print("Nums:", nums)

##l = lambda x:x**2
##
##print(l(4))
##
##
##def even(num):
##    return num% 2 == 0
##
##even_nums = [] 
##for i in nums:
##     if even(i):
##         even_nums.append(i)
##
##print("Evens without lambda:", even_nums)


##even_numbers = list(filter(lambda x: x%2 == 0, nums))
##print("Evens with lambda:", even_numbers)


##squares = list(map(lambda x: x**2, nums))
##print("Map:", squares)

squares = [num**2 for num in nums]
print(squares)



