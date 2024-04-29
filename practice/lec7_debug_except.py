# ########################################
# ## EXAMPLE: Buggy code to reverse a list
# ## Try to debug it! (fixes needed are explained below)
# ########################################
#
# def rev_list_buggy(L):
#     """
#    input: L, a list
#    Modifies L such that its elements are in reverse order
#    returns: nothing
#    """
#     for i in range(len(L)):
#         j = len(L) - i
#         L[i] = temp
#         L[i] = L[j]
#         L[j] = L[i]


# ## FIXES: --------------------------
# ## temp unknown
# ## list index out of range -> sub 1 to j
# ## get same list back -> iterate only over half
# ## --------------------------
# def rev_list(L):
#     """
#     input: L, a list
#     Modifies L such that its elements are in reverse order
#     returns: nothing
#     """
#     for i in range(len(L) // 2):
#         j = len(L) - i - 1
#         temp = L[i]
#         L[i] = L[j]
#         L[j] = temp
#
#
# L = [1, 2, 3, 4]
# rev_list(L)
# print(L)

# ######################################
# # EXAMPLE: Exceptions and input
# ######################################
# a = int(input("Tell me one number: "))
# b = int(input("Tell me another number: "))
# print("a/b = ", a / b)
# print("a+b = ", a + b)
#
# try:
#     a = int(input("Tell me one number: "))
#     b = int(input("Tell me another number: "))
#     print("a/b = ", a / b)
# except:
#     print("Bug in user input.")
#
# try:
#     a = int(input("Tell me one number: "))
#     b = int(input("Tell me another number: "))
#     print("a/b = ", a / b)
#     print("a+b = ", a + b)
# except ValueError:
#     print("Could not convert to a number.")
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except:
#     print("Something went very wrong.")

#
# ######################################
# # EXAMPLE: Raising your own exceptions
# ######################################
# def get_ratios(L1, L2):
#     """ Assumes: L1 and L2 are lists of equal length of numbers
#         Returns: a list containing L1[i]/L2[i] """
#     ratios = []
#     for index in range(len(L1)):
#         try:
#             ratios.append(L1[index] / L2[index])
#         except ZeroDivisionError:
#             ratios.append(float('nan'))  # nan = Not a Number
#         except:
#             raise ValueError('get_ratios called with bad arg')
#         else:
#             print("success")
#         finally:
#             print("executed no matter what!")
#     return ratios
#
#
# print(get_ratios([1, 4], [2, 4]))


# #######################################
# ## EXAMPLE: Exceptions and lists
# #######################################
def get_stats(class_list):
    new_stats = []
    for person in class_list:
        new_stats.append([person[0], person[1], avg(person[1])])
    return new_stats
