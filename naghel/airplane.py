from ground_vehicle import GroundVehicle
from flyig_vehicle import FlyingVehicle


class Airplane(FlyingVehicle, GroundVehicle):
    def __init__(self, airline, number_of_crew, captain, **kwargs):
        self.airline = airline
        self.number_of_crew = number_of_crew
        self.captain = captain
        super().__init__(**kwargs)
        
    ''''def outp(self):
        print(self.name,self.airline, self.number_of_wheels, self.captain, self.price, self.fuel, self.number_of_fins, self.max_speed)'''


class B707(Airplane):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    '''def outp(self):
        print(self.name, self.airline, self.captain, self.number_of_wheels)'''


'''v = Airplane(name="Airplane", price=500000, number_of_seats=300, max_speed=400, number_of_wheels=10,
    steering_wheel="Manual", fuel="Oil", number_of_fins=2, airline="Quera Air", number_of_crew=65,
    captain="Bagher")
v = B707(name="SAliB", price=850000, number_of_seats=850, max_speed=500, number_of_wheels=18,
                 steering_wheel="Manual", fuel="Oil", number_of_fins=2, airline="Quera Air", number_of_crew=65,
                 captain="Bagher")'''
