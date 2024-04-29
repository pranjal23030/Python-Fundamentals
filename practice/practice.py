# from prettytable import PrettyTable
#
# myTable = PrettyTable(["Student Name", "Class", "Section", "Percentage"])
#
# myTable.add_row(['Pranjal', '12', 'Mardi', '69%'])
# print(myTable)

class Car:
    def __init__(self, w, d):
        self.wheels = w
        self.doors = d
        self.color = ""

    def paint(self, c):
        self.color = c

    def __eq__(self, other):
        if self.wheels == other.wheels and \
                self.color == other.color and \
                self.doors == other.doors:
            return True
        else:
            return False

    def __str__(self):
        return f"Wheels:{self.wheels}\ndoors:{self.doors}\nColor:{self.color}"


mycar = Car(4, 2)
mycar.paint("red")
print(mycar)
yourcar = Car(4, 2)
print(mycar == yourcar)
print(yourcar)
