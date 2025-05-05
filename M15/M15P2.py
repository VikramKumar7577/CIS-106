class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price

    def discount_price(self):
        return self.sticker_price * 0.90

    def show_info(self):
        print(f"{self.make} {self.model}")
        print(f"Sticker Price: ${self.sticker_price}")
        print(f"Discount Price: ${self.discount_price()}")


class SportCar(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.sport_wheels = False
        self.sport_engine = False
        self.sport_interior = False

    def SportWheels(self, option):
        self.sport_wheels = (option == 'Y')

    def SportEngine(self, option):
        self.sport_engine = (option == 'Y')

    def SportInterior(self, option):
        self.sport_interior = (option == 'Y')

    def updated_price(self):
        price = self.discount_price()
        if self.sport_wheels:
            price += 1000.00
        if self.sport_engine:
            price += 3000.00
        if self.sport_interior:
            price += 2000.00
        return price

    def show_info(self):
        print(f"{self.make} {self.model} (SportCar)")
        print(f"Base Discount Price: ${self.discount_price()}")
        print("Options Included:")
        if self.sport_wheels: print("- Sport Wheels ($1000)")
        if self.sport_engine: print("- Sport Engine ($3000)")
        if self.sport_interior: print("- Sport Interior ($2000)")
        print(f"Updated Price: ${self.updated_price()}")


print("\n---- Cars ----")
car1 = Car("Toyota", "Camry", 25000)
car2 = Car("Honda", "Civic", 22000)
car1.show_info()
print()
car2.show_info()

print("\n---- SportCars ----")
sport1 = SportCar("Ford", "Mustang", 30000)
sport1.SportWheels("Y")
sport1.SportEngine("Y")
sport1.SportInterior("N")
sport1.show_info()

print()
sport2 = SportCar("Chevy", "Camaro", 35000)
sport2.SportWheels("Y")
sport2.SportEngine("Y")
sport2.SportInterior("Y")
sport2.show_info()