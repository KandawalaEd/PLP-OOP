class train:
    def move(self):
        return "CHUG chug"
    
class bus:
    def move(self):
        return "Vuuuuuu"
    
class F1:
    def move(self):
        return "Vroooooom"
    

for vehicle in [train, bus, F1]:
    vehicle_type = vehicle()
    print (vehicle_type.move())