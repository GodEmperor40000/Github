class Building:
    stairs = 0
    pass

class HouseBuilding(Building):
    num_of_pepople = 0

    def info(self):
       print(f'Number of stairs in the building: {Building2.stairs}; Number of householders in the building: {Building2.num_of_pepople}') 

Building1 = Building()
Building2 = HouseBuilding()

Building1.stairs = 3
Building2.stairs = 21
Building2.num_of_pepople = 1000

Building2.info()