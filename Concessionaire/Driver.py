class Driver:
    def __init__(self, name, id_driver):
        self.name = name
        self.driver= id_driver
        self.cars_purchased = []

    def buy_car(self, car):
        if car.available:
            car.sell()
            self.cars_purchased.append(car)
        else:
            print(f"El vehículo {car.model} no está disponible.")

    def return_car(self, car, dealership):
        if car in self.cars_purchased:
            car.enable()
            self.cars_purchased.remove(car)
            dealership.add_car(car)
        else:
            print(f"El vehículo {car.model} no está en la lista de comprados.")