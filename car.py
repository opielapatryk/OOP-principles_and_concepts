from abc import abstractmethod, ABC

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def numberOfWheels(self):
        pass

class Keys(ABC):
    @abstractmethod
    def open_vehicle(self):
        pass


class CarKeys(Keys):
    def __init__(self) -> None:
        self.is_open = False
        self.wireless = True
    
    def open_vehicle(self):
        self.is_open = True

class BikeKeys(Keys):
    def __init__(self) -> None:
        self.is_open = False
        self.wireless = False
    
    def open_vehicle(self):
        self.is_open = True

class Car(Vehicle):
    def __init__(self, model: str, keys: Keys, running: bool = False) -> None:
        self.model = model
        self.keys = keys
        self.running = running

    def start_engine(self):
        if not self.keys.is_open:
            raise Exception("No keys")
        print('Engine started')
        self.running = True
    
    def numberOfWheels(self):
        print('Car have 4 wheels')

class Motorbike(Vehicle):
    def __init__(self, model: str, keys: Keys, running: bool = False) -> None:
        self.model = model
        self.keys = keys
        self.running = running

    def start_engine(self):
        if not self.keys.is_open:
            raise Exception("No keys")
        print('Engine started')
        self.running = True

    def numberOfWheels(self):
        print('Motorbike have 4 wheels')


def create_vehicle(vehicle_type, model, keys):
    if vehicle_type == "car":
        return Car(model, keys)
    elif vehicle_type == "motorbike":
        return Motorbike(model, keys)
    else:
        raise ValueError("Invalid vehicle type")

# Usage:
# Car
carkeys = CarKeys()
carkeys.open_vehicle()
car = create_vehicle("car", "Toyota", carkeys)
car.start_engine()
print(carkeys.wireless)

# Bike
bikekeys = BikeKeys()
bikekeys.open_vehicle()
bike = create_vehicle("motorbike", "Yamaha", bikekeys)
bike.start_engine()
print(bikekeys.wireless)