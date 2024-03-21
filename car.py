from abc import abstractmethod, ABC

class Vehicle(ABC):
    @abstractmethod
    def startEngine(self):
        pass

    @abstractmethod
    def numberOfWheels(self):
        pass

class Keys(ABC):
    @abstractmethod
    def openVehicle(self):
        pass

class Car(Vehicle):
    def __init__(self, model: str, keys: Keys, running: bool) -> None:
        self.model = model
        self.keys = keys
        self.running = False

    def startEngine(self):
        if not self.keys.is_open:
            raise Exception("No keys")
        print('Engine started')
    
    def numberOfWheels(self):
        print('Car have 4 wheels')

class Motorbike(Vehicle):
    def __init__(self, model: str, keys: Keys, running: bool = False) -> None:
        self.model = model
        self.keys = keys
        self.running = running

    def startEngine(self):
        if not self.keys.is_open:
            raise Exception("No keys")
        print('Engine started')
        self.running = True

    def numberOfWheels(self):
        print('Motorbike have 4 wheels')

class BikeKeys(Keys):
    def __init__(self) -> None:
        self.is_open = False
    
    def openVehicle(self):
        self.is_open = True

keys = BikeKeys()
keys.openVehicle()

cycle = Motorbike('Yamaha', keys)
print('Is open:', keys.is_open)
print('Engine running:', cycle.running)
cycle.startEngine()
print('Engine running:', cycle.running)
