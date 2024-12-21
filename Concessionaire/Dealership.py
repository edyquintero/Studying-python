class Dealership:
    def __init__(self):
        self.cars = []
        self.drivers = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"El vehículo {car.model} ha sido agregado al inventario.")

    def register_driver(self, driver):
        self.drivers.append(driver)
        print(f"El cliente {driver.name} ha sido registrado.")

    def show_available_cars(self):
        print("Vehículos disponibles:")
        for car in self.cars:
            if car.available:
                print(f"{car.model} por ${car.price}")