import sqlite3 as sq

def login():
    user = input("Enter username : ")
    password = input("Enter your password : ")
    if user == '1234' and password == '1234' :
        pass
    else: print("wrong username or password")

class Package:
    def __init__(self,num,weight,destination,beginning):

        conn = sq.connect("Packages.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Packages (num int PRIMARY KEY, weight real, destination text, beginning text)''')
        cur.execute(f'''INSERT OR IGNORE INTO Packages VALUES ({num},{weight},'{destination}','{beginning}')''')
        conn.commit()
        conn.close()

    def editPackage(self,num,weight = "",destination = "",beginning = ""):
        conn = sq.connect("Packages.db")
        cur = conn.cursor()
        if weight != "":
            cur.execute(f'''UPDATE Packages SET weight={weight} WHERE num = {num}''') 
            
        if destination != "":
            cur.execute(f'''UPDATE Packages SET destination='{destination}' WHERE num = {num}''')
             
        if beginning != "":
            cur.execute(f'''UPDATE Packages SET beginning='{beginning}' WHERE num = {num}''')     
        conn.commit()
        conn.close()
        
    
    def removePackage(self,num):
        conn = sq.connect("Packages.db")
        cur = conn.cursor()
        cur.execute(f'''DELETE from P   ackages WHERE num = {num}''')
        conn.commit()
        conn.close()
   
   
    
class coldPackage:
    def __init__(self,num,weight,destination,beginning,min_temperature,property = ""):
        conn = sq.connect("coldPackages.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS coldPackages (num int PRIMARY KEY, weight real, destination text, beginning text,min_temperature int,property text )''')
        cur.execute(f'''INSERT OR IGNORE INTO coldPackages VALUES ({num}, {weight}, '{destination}', '{beginning}',{min_temperature},'{property}' )''')
        conn.commit()
        conn.close()
        
        
    def editcoldPackage(self,num,weight = "",destination = "",beginning = "",min_temperature = '',property = ''):
        conn = sq.connect("coldpackages.db")
        cur = conn.cursor()
        if weight != "":
            cur.execute(f'''UPDATE coldPackages SET weight={weight} WHERE num = {num}''') 
            
        if destination != "":
            cur.execute(f'''UPDATE coldPackages SET destination='{destination}' WHERE num = {num}''')
             
        if beginning != "":
            cur.execute(f'''UPDATE coldPackages SET beginning='{beginning}' WHERE num = {num}''')    
            
        if min_temperature != "":
             cur.execute(f'''UPDATE coldPackages SET min_temperature='{min_temperature}' WHERE num = {num}''') 
        
        if property != "":
            cur.execute(f'''UPDATE coldPackages SET property='{property}' WHERE num = {num}''') 
        conn.commit()
        conn.close()
    
    def removeColdPackage(self,num):
        conn = sq.connect("coldPackages.db")
        cur = conn.cursor()
        cur.execute(f'''DELETE from codlPackages WHERE num = {num}''')
        conn.commit()
        conn.close()
        
        
        
class breakablePackage():
        def __init__(self,num,weight,destination,beginning,property = ""):
            conn = sq.connect("breakablePackages.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS breakablePackages (num int PRIMARY KEY, weight real, destination text, beginning text , property text)''')
            cur.execute(f'''INSERT OR IGNORE INTO breakablePackages VALUES ({num},{weight},'{destination}','{beginning}','{property}')''')
            conn.commit()
            conn.close()
  
        def editbreakablePackage(self,num,weight = "",destination = "",beginning = "",property = ""):
            conn = sq.connect("breakablePackages.db")
            cur = conn.cursor()
            if weight != "":
                cur.execute(f'''UPDATE breakablePackages SET weight={weight} WHERE num = {num}''') 

            if destination != "":
                cur.execute(f'''UPDATE breakablePackages SET destination='{destination}' WHERE num = {num}''')

            if beginning != "":
                cur.execute(f'''UPDATE breakablePackages SET beginning='{beginning}' WHERE num = {num}''')    
            
            if property != "":
                cur.execute(f'''UPDATE breakablePackages SET property='{property}' WHERE num = {num}''') 
            conn.commit()
            conn.close()      

        def removebreakablePackage(self,num):
            conn = sq.connect("breakablePackages.db")
            cur = conn.cursor()
            cur.execute(f'''DELETE from breakablePackages WHERE num = {num}''')
            conn.commit()
            conn.close()
   
  
  
    
    # packages in container has a problem
class Container():
    def __init__(self,num,max_weight,max_package,packeges_in_container):
        conn = sq.connect("Container.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Container (num int PRIMARY KEY, max_weight real, max_packages int, packeges_in_container text)''')
        cur.execute(f'''INSERT OR IGNORE INTO Container VALUES ({num},{max_weight},{max_package},'{packeges_in_container}')''')
        conn.commit()
        conn.close()
        
        
    def editContainer(self,num,max_weight = "",max_package = "",packages_in_container = ""):
        conn = sq.connect("Container.db")
        cur = conn.cursor()
        if max_weight != "":
            cur.execute(f'''UPDATE Container SET max_weight={max_weight} WHERE num = {num}''') 
            
        if max_package != "":
            cur.execute(f'''UPDATE Container SET max_package='{max_package}' WHERE num = {num}''')
             
        if packages_in_container != "":
            cur.execute(f'''UPDATE Container SET packages_in_container='{packages_in_container}' WHERE num = {num}''')     
        conn.commit()
        conn.close() 
    
    
    def removeContainer(self,num):
        conn = sq.connect("Container.db")
        cur = conn.cursor()
        cur.execute(f'''DELETE from Container WHERE num = {num}''')
        conn.commit()
        conn.close()    
    
    
    
    
class freezerContainer():
    def __init__(self,num,max_weight,max_package,packeges_in_container,min_temp_produced_by_container):
        conn = sq.connect("freezerContainer.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS freezerContainer (num int PRIMARY KEY, max_weight real, max_packages int, packeges_in_container text,min_temp_produced_by_container int)''')
        cur.execute(f'''INSERT OR IGNORE INTO freezerContainer VALUES ({num},{max_weight},{max_package},'{packeges_in_container}',{min_temp_produced_by_container})''')
        conn.commit()
        conn.close()

    def editfreezerContainer(self,num,max_weight = "",max_package = "",packages_in_container = "",min_temp_produced_by_container = ''):
        conn = sq.connect("freezerContainer.db")
        cur = conn.cursor()
        if max_weight != "":
            cur.execute(f'''UPDATE freezerContainer SET max_weight={max_weight} WHERE num = {num}''') 
            
        if max_package != "":
            cur.execute(f'''UPDATE freezerContainer SET max_package='{max_package}' WHERE num = {num}''')
             
        if packages_in_container != "":
            cur.execute(f'''UPDATE freezerContainer SET packages_in_container='{packages_in_container}' WHERE num = {num}''')   
            
        if min_temp_produced_by_container != "":
            cur.execute(f'''UPDATE freezerContainer SET min_temp_produced_by_container='{min_temp_produced_by_container}' WHERE num = {num}''')                
        conn.commit()
        conn.close() 
          


class breakableContainer():
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
        
class carWithRoom():
    def __init__(self,max_weight_tolerable,max_number_tolerable,property = ''):
        super().__init__()
        self.max_weight_tolerable = max_weight_tolerable
        self.max_number_tolerable = max_number_tolerable
        self.property = property
        
        
class containerCar():
    def __init__(self,max_container_can_be_connected,property = ''):
        super().__init__()
        self.max_container_can_be_connected = max_container_can_be_connected
        self.property = property
        
        
x1 = breakablePackage(1,6,"hmd","tehran")
x2 = coldPackage(2,3,"azar","canada",0)
x3 = Package(4,9,"america","turkey")
x4 = Container(3,1500,100,[x3,x2,x1])
