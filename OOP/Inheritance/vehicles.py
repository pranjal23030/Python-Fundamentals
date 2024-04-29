class Automobile:
    def __init__(self, make, model, mileage, price):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.price = price

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_mileage(self):
        return self.mileage

    def get_price(self):
        return self.price

    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_mileage(self, mileage):
        self.mileage = mileage

    def set_price(self, price):
        self.price = price


# The Car class represents a car. It is a subclass of the Automobile class.

class Car(Automobile):
    # The __init__ method accepts arguments for the car's make, model, mileage, price, and doors.

    def __init__(self, make, model, mileage, price, doors):
        # Call the superclasses __init__ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument

        Automobile.__init__(self, make, model, mileage, price)

        # Initialize the doors attribute
        self.doors = doors

    def get_doors(self):
        return self.doors

    def set_doors(self, doors):
        self.doors = doors


# The Truck class represents a pickup truck. It is a subclass of the Automobile class.

class Truck(Automobile):
    # The __init__ method accepts arguments for the truck's make, model, mileage, price, and drive type.

    def __init__(self, make, model, mileage, price, drive_type):
        # Call the superclasses __init__ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument

        Automobile.__init__(self, make, model, mileage, price)

        # Initialize the drive type
        self.drive_type = drive_type

    def get_drive_type(self):
        return self.drive_type

    def set_drive_type(self, drive_type):
        self.drive_type = drive_type


# The SUV class represents a utility vehicle. It is a subclass of the Automobile class.

class SUV(Automobile):
    # The __init__ method accepts arguments for the SUV's make, model, mileage, price, and passenger capacity.

    def __init__(self, make, model, mileage, price, passenger_capacity):
        # Call the superclasses __init__ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument

        Automobile.__init__(self, make, model, mileage, price)
        self.passenger_capacity = passenger_capacity

        # Initialize the passenger capacity attribute

    def get_passenger_capacity(self):
        return self.passenger_capacity

    def set_passenger_capacity(self, passenger_capacity):
        self.passenger_capacity = passenger_capacity
