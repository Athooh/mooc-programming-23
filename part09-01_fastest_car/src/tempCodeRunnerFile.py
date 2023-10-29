def fastest_car(cars: list):
    for car in sorted(cars[1]):
        return car[-1]
