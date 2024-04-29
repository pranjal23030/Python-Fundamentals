# Write a program which takes dividend and divisor and outputs quotient and remainder

def quotient_remainder_finder(a, b):
    quotient = a // b
    remainder = a % b
    print("Quotient:", quotient)
    print("Remainder:", remainder)


dividend = eval(input("Dividend: "))
divisor = eval(input("Divisor: "))

quotient_remainder_finder(dividend,divisor)