from Car import Car
from Dealership import Dealership
from Driver import Driver

if __name__ == "__main__":
    # Crear el concesionario
    dealership = Dealership()

    # Crear algunos vehículos
    car1 = Car("Toyota Corolla", 20000)
    car2 = Car("Honda Civic", 22000)
    car3 = Car("Ford Focus", 18000)

    # Agregar los vehículos al concesionario
    dealership.add_car(car1)
    dealership.add_car(car2)
    dealership.add_car(car3)

    # Mostrar vehículos disponibles
    dealership.show_available_cars()

    # Crear un cliente (conductor)
    driver1 = Driver("Juan Pérez", "123456")

    # Registrar al cliente en el concesionario
    dealership.register_driver(driver1)

    # El cliente compra un vehículo
    driver1.buy_car(car1)

    # Mostrar nuevamente los vehículos disponibles
    dealership.show_available_cars()

    # El cliente devuelve el vehículo al concesionario
    driver1.return_car(car1, dealership)

    # Mostrar nuevamente los vehículos disponibles
    dealership.show_available_cars()
