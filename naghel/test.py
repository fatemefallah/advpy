class Polygon:
    
    def __init__(self,name,age,job):
        self.name = name
        self.age = age
        self.job = job
        
    def inputSides(self):
        print("hi inputSides")

    def dispSides(self):
        print("hi dispSides")


class Triangle(Polygon):
    def __init__(self,last_name,**kwargs):
        self.last_name = last_name
        super().__init__(**kwargs)
        

    def get_name(self):
        print(self.last_name,self.name,self.age,self.job)

    def findArea(self):
        print("hi")

t = Triangle(last_name = "reis",name = "sadegh", age = 23,  job ="comp")
t.get_name()