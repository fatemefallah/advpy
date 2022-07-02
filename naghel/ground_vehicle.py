from vehicle import Vehicle

class GroundVehicle(Vehicle):
    def __init__(self, number_of_wheels, steering_wheel, **kwargs):
        self.number_of_wheels = number_of_wheels
        self.steering_wheel = steering_wheel
        super().__init__(**kwargs)
        
    '''def outp(self):
        print(self.name, self.number_of_wheels, self.price, self.max_speed)'''
        
        
        
'''v = GroundVehicle(name="Bicycle", price=100, number_of_seats=1, max_speed=60, number_of_wheels=2, steering_wheel="Manual")
v.outp()'''
