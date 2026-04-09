class Tires:
    def __init__(self, size):
        self.size = size

    def get_pressure(self):
        pass

    def pump(self): 
        pass


class Engine:
    def __init__(self, fuel, type):
        self.fuel = fuel
        self.type = type

    def start():
        pass

    def stop():
        pass

    def get_state():
        pass


class Vehicle:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires

city_tires = Tires(15)
off_road_tires = Tires(18)

electric_engine = Engine("electicity", "electric")
petrol_engine = Engine("petrol", "petrol")

city_car = Vehicle(1, electric_engine, city_tires)
all_terrain_car = Vehicle(2, petrol_engine, off_road_tires)
    