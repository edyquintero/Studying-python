class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price
        self.available = True

    def sell(self):
        if self.available:
            self.available = False
            print(f"El vehículo {self.model} ha sido vendido.")
        else:
            print(f"El vehículo {self.model} no está disponible.")

    def enable(self):
        self.available = True
        print(f"El vehículo {self.model} está disponible para la venta nuevamente.")
