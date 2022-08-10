

class Building:
    stairs = 0
    def openDoor(num_of_people):
        print(f'door was opened {num_of_people} times')

class HouseBuilding(Building):

    def __init__(self, num_of_appartments, stairs):
        self.stairs = stairs
        self.num_of_appartments = num_of_appartments

    def info(self):
       print(f'Number of stairs in the building: {self.stairs}; Number of appartments in the building: {self.num_of_appartments}') 

    def enterBuilding(self,num_of_people):
        self.openDoor(num_of_people)
        print(f'{num_of_people} people are in the House Building')

class OfficeBuilding(Building):
    
    def __init__(self, num_of_offices, stairs):
        self.stairs = stairs
        self.num_of_offices = num_of_offices

    def info(self):
        print(f'Number of stairs in the Office building: {self.stairs}; Number of offices in the building: {self.num_of_offices}')

    def enterBuilding(self, num_of_people):
        self.openDoor(num_of_people)
        print(f'{num_of_people} people are working in the Office building')

Building1 = Building()
Building2 = HouseBuilding(200, 40)
Building3 = OfficeBuilding(1000, 50)

num_of_HouseBuilding = 4
num_of_OfficeBuilding = 3

for_Houses = [(10,1), (100,4), (5, 2), (500, 20)]
for_Offices = [(3, 3), (2, 1), (40, 10)]

HouseBuildings = [HouseBuilding(for_Houses[a][0], for_Houses[a][1]) for a in range(num_of_HouseBuilding)]
OfficeBuildings = [OfficeBuilding(for_Offices[a][0], for_Offices[a][1]) for a in range(num_of_OfficeBuilding)]

buildings = []
buildings.extend(HouseBuildings)
buildings.extend(OfficeBuildings)

for building in buildings:
    building.info()




