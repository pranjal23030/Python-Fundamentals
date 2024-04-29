
# Global vs local variables

##bla = 2# This is a global variable
##
##def somefunc(num):
##    # global bla
##    ## print(bla)
##    # bla = num + 4
##
##    x = 5
##
##    
##
##somefunc(5)
##print(x)

# print(bla)










# global variable



outer = 5
##
def total():
    # local variable / function scope
    inner = 4
    global outer
    outer = 7
    return inner + outer


inner = total()
print(inner)
# print(outer)


