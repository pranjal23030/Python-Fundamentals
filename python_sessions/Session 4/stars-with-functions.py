
"""
    Prints different shapes using nested for loop and  functions
"""

def print_shape(num, pattern):
    for i in range(1, num+1):
        for j in range(0,i):
            print(pattern, end=" ")
        print()
        

def print_inverted(num, pattern):
    for i in range(num):
        for j in range(i, num):
            print(pattern, end=" ")
        print()

def print_another_shape(num, pattern):
    # First loop for row 
    for i in range(1, num+1):
        # Second loop for space
        for j in range(num - 1, i-1, -1):
            print(" ", end=" ")
        # Third loop for patten
        for k in range(0, i):
            print(pattern, end=" ")
        print()


def print_numbered_shape(num, pattern):
    for i in range(1, num+1):
        for j in range(1, 1+i):
            print(j, end=" ")
        print()
            
         
def main():
    print_another_shape(5, "*")


if __name__ == "__main__":
    main()
