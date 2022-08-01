class Building:
    stairs = 0
    pass

class HouseBuilding(Building):
    
    def __init__(self, stairs, num_of_people):
        self.stairs = stairs
        self.num_of_people = num_of_people    

    def __str__(self):
       print(f'Number of stairs in the building: {Building2.stairs}; Number of householders in the building: {Building2.num_of_people}') 

Building1 = Building()
Building2 = HouseBuilding(21, 1000)

Building1.stairs = 3

Building2.__str__()

print("Hellow")

