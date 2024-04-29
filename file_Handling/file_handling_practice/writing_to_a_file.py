with open("test1.txt","a") as write_file:
    line1 = input('Fav sport?? ')
    write_file.write(" " + line1)
    print("Okay, enough")