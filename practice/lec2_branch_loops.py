###################
# EXAMPLE: strings
###################
# hi = "hello there"
# name = "ana"
# greet = hi + name
# print(greet)
# greeting = hi + " " + name
# print(greeting)
# print(hi, name)
# silly = hi + (" " + name)*3
# print(silly)

####################
# EXAMPLE: output
####################
# x = 1
# print(x)
# x_str = str(x)
# print("my fav number is", x, ".", "x=", x)
# print("my fav number is", x_str + "." + "x=" + x_str)
# print("my fav number is" + x_str + "." + "x=" + x_str)


####################
# EXAMPLE: input
####################

# text = input("Type anything... ")
# print(5*text)
#
# num = int(input("Number: "))
# print(5 * num)


####################
# EXAMPLE: conditionals/branching
####################
# x = float(input("Enter a number for x: "))
# y = float(input("Enter a number for y: "))
# if x == y:
#     print("x and y are equal")
#     if y != 0:
#         print("therefore, x / y is", x / y)
# elif x < y:
#     print("x is smaller")
# elif x > y:
#     print("y is smaller")
# print("thanks!")

####################
# EXAMPLE: remainder
####################

# def is_even(n):
#     if n % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#
#
# is_even(12)

####################
# EXAMPLE: while loops
# Try expanding this code to show a sad face if you go right
# twice and flip the table any more times than that.
# Hint: use a counter
###################
# n = input("You are in the Lost Forest\n****************\n****************\n "
#           ":)\n****************\n****************\nGo left or right? ")
# while n == "right" or n == "Right":
#     n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ "
#               "┻━┻\n****************\n****************\nGo left or right? ")
# print("\nYou got out of the Lost Forest!\n")

# n = 0
# while n < 5:
#     print(n)
#     n = n + 1

####################
# EXAMPLE: for loops
####################
# for n in range(5):
#     print(n)

sum1 = 0
for i in range(10):
    sum1 += i
print(sum1)

sum2 = 0
for i in range(7, 10):
    sum2 += i
print(sum2)

sum3 = 0
for i in range(5, 11, 2):
    sum3 += i
    if sum3 == 5:
        break
    sum3 += 1
print(sum3)

