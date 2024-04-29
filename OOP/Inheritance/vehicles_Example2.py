import vehicles


def main():
    car = vehicles.Car('BMW', 2001, 70000, 1500.0, 4)
    truck = vehicles.Truck('Toyota', 2002, 40000, 1200.0, '4WD')
    suv = vehicles.SUV('Volvo', 2000, 30000, 18500.0, 5)

    print('Just printing some things: ')
    print('Make: ', car.get_make())
    print('Doors: ', car.get_doors())
    print('Drive Type: ', truck.get_drive_type())
    print('Passenger: ', suv.get_passenger_capacity())


if __name__ == '__main__':
    main()
