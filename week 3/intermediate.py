class Vehicle:
    def __init__(self, make, model):
        self.__make = make  
        self.__model = model  

    def describe(self):
        return f"Vehicle Make: {self.__make}, Model: {self.__model}"

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.__num_doors = num_doors 

    def describe(self):
        base_description = super().describe()
        return f"{base_description}, Number of Doors: {self.__num_doors}"

    def get_num_doors(self):
        return self.__num_doors


class Bike(Vehicle):
    def __init__(self, make, model, bike_type):
        super().__init__(make, model)
        self.__bike_type = bike_type  

    def describe(self):
        base_description = super().describe()
        return f"{base_description}, Bike Type: {self.__bike_type}"

    def get_bike_type(self):
        return self.__bike_type


# Demonstrating polymorphism
def vehicle_description(vehicle):
    print(vehicle.describe())


# Creating instances
car = Car("Toyota", "Camry", 4)
bike = Bike("Yamaha", "MT-07", "Sport")

# Using polymorphism
vehicle_description(car)  
vehicle_description(bike) 