def login():
    flag = False
    user = input("Enter username : ")
    password = input("Enter your password : ")
    if user == '1234' and password == '1234' :
        pass
    else: print("wrong username or password")

class Package:
    def __init__(self,number,weight,destination,beginning):
        self.number = number
        self.weight = weight
        self.destination = destination
        self.beginning = beginning
        
    def addPackege():
        pass

    def editPackage():
        pass
    
    def removePackage():
        pass
   
   
    
class coldPackage(Package):
    def __init__(self,min_temperature,property = ""):
        super().__init__()
        self.min_temperature = min_temperature
        self.property = property
        
        
        
class breakablePackage(Package):
    def __init__(self,property):
        super().__init__()
        self.property = property
  
  
  
  
  
    
    
class Container():
    def __init__(self,number,max_weight,max_package,packeges_in_container):
        self.number = number
        self.max_waghit = max_weight
        self.max_package = max_package
        self.packeges_in_container = packeges_in_container
        
    def addConainrt():
        pass
    
    def editContainer():
        pass
    
    def removeContainer():
        pass
    
    
    
    
class freezerContainer(Container):
    def __init__(self,min_temp_produced_by_car,property = ''):
        super().__init__()
        self.min_temp_produced_by_car = min_temp_produced_by_car
        self.property = property    


class breakableContainer(Container):
    def __init__(self,max_speed_of_car,property = ''):
        super().__init__()
        self.max_speed_of_car = max_speed_of_car
        self.property = property
    
    
    
    
class Car():
    def __init__(self,number,max_weight):
        self.number = number
        self.max_weight = max_weight
        
    def addCar():
        pass
    
    def editCar():
        pass
    
    def removeCar():
        pass
        
class carWithRoom(Car):
    def __init__(self,max_weight_tolerable,max_number_tolerable,property = ''):
        super().__init__()
        self.max_weight_tolerable = max_weight_tolerable
        self.max_number_tolerable = max_number_tolerable
        self.property = property
        
        
class containerCar(Car):
    def __init__(self,max_container_can_be_connected,property = ''):
        super().__init__()
        self.max_container_can_be_connected = max_container_can_be_connected
        self.property = property