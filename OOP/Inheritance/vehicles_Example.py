import vehicles


def main():
    # Create an object from the carr class.
    # The car is a 2007 Audi with 12,500 miles, prices
    # at $21,500.0, and has 5 doors.

    used_car = vehicles.Car('Audi', 2007, 12500, 21500.0, 4)
    used_car.set_doors(5)

    # Display the car's data.
    print('Make: ', used_car.get_make())
    print('Model: ', used_car.get_model())
    print('Mileage: ', used_car.get_mileage())
    print('Price: ', used_car.get_price())
    print('Doors: ', used_car.get_doors())

# Call the main function.


if __name__ == '__main__':
    main()
