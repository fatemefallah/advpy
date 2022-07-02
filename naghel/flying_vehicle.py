from vehicle import Vehicle

class FlyingVehicle(Vehicle):
    def __init__(self, fuel, number_of_fins, **kwargs):
        self.fuel = fuel
        self.number_of_fins = number_of_fins
        super().__init__(**kwargs)

    '''def outp(self):
        print(self.name, self.number_of_seats, self.price, self.fuel, self.number_of_fins, self.max_speed)'''

'''v = FlyingVehicle(name="Airplane", price=500000, number_of_seats=300, max_speed=400, fuel="Oil",
                          number_of_fins=2)
v.outp()'''