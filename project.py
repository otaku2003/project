import sqlite3 as sq

def login():
    user = input("Enter username : ")
    password = input("Enter your password : ")
    if user == '1234' and password == '1234' :
        pass
    else: print("wrong username or password")

class Package:
    def __init__(self,num,weight,destination,beginning):

        conn = sq.connect("coldPackages.db")
        cur = conn.cursor()
        if (cur.execute(f'''SELECT EXISTS(SELECT * FROM coldPackages WHERE num="{num}" )''' )):
            print("this number exists in coldpackages")
            
        conn = sq.connect("breakablePackages.db")
        cur = conn.cursor()
        if (cur.execute(f'''SELECT EXISTS(SELECT * FROM breakablePackages WHERE num="{num}" )''')):
            print("this number exixts in breakable packages ")
        else:
            conn = sq.connect("Packages.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS Packages (num int PRIMARY KEY AUTOINCREMENT, weight real, destination text, beginning text)''')
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
        conn = sq.connect("Packages.db")
        cur = conn.cursor()
        if (cur.execute(f'''SELECT EXISTS(SELECT * FROM Packages WHERE num="{num}" )''' )):
            print("this number exists in packages")
            
        conn = sq.connect("breakablePackages.db")
        cur = conn.cursor()
        if (cur.execute(f'''SELECT EXISTS(SELECT * FROM breakablePackages WHERE num="{num}" )''')):
            print("this number exixts in breakable packages ")
        else:
            conn = sq.connect("coldPackages.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS coldPackages (num int PRIMARY KEY AUTOINCREMENT, weight real, destination text, beginning text,min_temperature int,property text )''')
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
    def __init__(self,num,max_weight,max_package,packeges_in_container,property = ""):
        conn = sq.connect("Container.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Container (num int PRIMARY KEY, max_weight real, max_package int, packeges_in_container text,property text)''')
        cur.execute(f'''INSERT OR IGNORE INTO Container VALUES ({num},{max_weight},{max_package},'{packeges_in_container}','{property}')''')
        conn.commit()
        conn.close()
        
        
    def editContainer(self,num,max_weight = "",max_package = "",packages_in_container = "",property = ''):
        conn = sq.connect("Container.db")
        cur = conn.cursor()
        if max_weight != "":
            cur.execute(f'''UPDATE Container SET max_weight={max_weight} WHERE num = {num}''') 
            
        if max_package != "":
            cur.execute(f'''UPDATE Container SET max_package='{max_package}' WHERE num = {num}''')
             
        if packages_in_container != "":
            cur.execute(f'''UPDATE Container SET packages_in_container='{packages_in_container}' WHERE num = {num}''')     
            
        if packages_in_container != "":
            cur.execute(f'''UPDATE Container SET property='{property}' WHERE num = {num}''')  
        conn.commit()
        conn.close() 
    
    
    def removeContainer(self,num):
        conn = sq.connect("Container.db")
        cur = conn.cursor()
        cur.execute(f'''DELETE from Container WHERE num = {num}''')
        conn.commit()
        conn.close()    
        

    
    
    
class freezerContainer():
    def __init__(self,num,max_weight,max_package,packeges_in_container,min_temp_produced_by_container,property = ""):
        conn = sq.connect("freezerContainer.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS freezerContainer (num int PRIMARY KEY, max_weight real, max_packages int, packeges_in_container text,min_temp_produced_by_container int,property text)''')
        cur.execute(f'''INSERT OR IGNORE INTO freezerContainer VALUES ({num},{max_weight},{max_package},'{packeges_in_container}',{min_temp_produced_by_container},'{property}')''')
        conn.commit()
        conn.close()

    def editfreezerContainer(self,num,max_weight = "",max_package = "",packages_in_container = "",min_temp_produced_by_container = '',property = ''):
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
                           
        if property != "":
            cur.execute(f'''UPDATE freezerContainer SET oroperty='{property}' WHERE num = {num}''') 

        conn.commit()
        conn.close() 
          
    def removefreezerContainer(self,num):
        conn = sq.connect("freezerContainer.db")
        cur = conn.cursor()
        cur.execute(f'''DELETE from freezerContainer WHERE num = {num}''')
        conn.commit()
        conn.close()  
        
       

class breakableContainer():
    def __init__(self,num,max_weight,max_package,packeges_in_container,max_speed_of_car,property = ""):
        conn = sq.connect("breakableContainer.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS breakableContainer (num int PRIMARY KEY, max_weight real, max_packages int, packeges_in_container text,max_speed_of_car int,property text)''')
        cur.execute(f'''INSERT OR IGNORE INTO breakableContainer VALUES ({num},{max_weight},{max_package},'{packeges_in_container}',{max_speed_of_car},'{property}')''')
        conn.commit()
        conn.close()

    def editbreakableContainer(self,num,max_weight = "",max_package = "",packages_in_container = "",max_speed_of_car = '',property = ''):
        conn = sq.connect("breakableContainer.db")
        cur = conn.cursor()
        if max_weight != "":
            cur.execute(f'''UPDATE breakableContainer SET max_weight={max_weight} WHERE num = {num}''') 
            
        if max_package != "":
            cur.execute(f'''UPDATE breakableContainer SET max_package='{max_package}' WHERE num = {num}''')
             
        if packages_in_container != "":
            cur.execute(f'''UPDATE breakableContainer SET packages_in_container='{packages_in_container}' WHERE num = {num}''')     
            
        if packages_in_container != "":
            cur.execute(f'''UPDATE breakableContainer SET property='{property}' WHERE num = {num}''')  
            
        if max_speed_of_car != '':
            cur.execute(f'''UPDATE breakableContainer SET max_speed_of_car='{max_speed_of_car}' WHERE num = {num}''') 
            
        conn.commit()
        conn.close() 
        
    def removebreakableContainer(self,num):
        conn = sq.connect("breakableContainer.db")
        cur = conn.cursor()
        cur.execute(f'''DELETE from breakableContainer WHERE num = {num}''')
        conn.commit()
        conn.close()  
    
    
    
class Car():
    def __init__(self,num,max_weight):
        conn = sq.connect("Car.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Car (num int PRIMARY KEY, max_weight real)''')
        cur.execute(f'''INSERT OR IGNORE INTO Car VALUES ({num},{max_weight})''')
        conn.commit()
        conn.close()
        
    
    def editCar(self,num,max_weight_tolerable):
        conn = sq.connect("Car.db")
        cur = conn.cursor()
        if max_weight_tolerable != "":
            cur.execute(f'''UPDATE Car SET max_weight_tolerable={max_weight_tolerable} WHERE num = {num}''') 
        conn.commit()
        conn.close() 
    
    def removeCar(self,num):
        conn = sq.connect("Car.db")
        cur = conn.cursor()
        cur.execute(f'''DELETE from Car WHERE num = {num}''')
        conn.commit()
        conn.close() 
        
        
class carWithRoom():
    def __init__(self,num,max_weight_tolerable,max_number_tolerable,packages,property = ''):
        conn = sq.connect("carWithRoom.db")
        cur = conn.cursor()                                                                                          # list packages
        cur.execute('''CREATE TABLE IF NOT EXISTS carWithRoom (num int PRIMARY KEY, max_weight_tolerable real,max_number_tolerable int,packages text,property text)''')
        cur.execute(f'''INSERT OR IGNORE INTO carWithRoom VALUES ({num},{max_weight_tolerable},{max_number_tolerable},'{packages}',{max_number_tolerable},'{property}')''')
        conn.commit()
        conn.close()
    
    def editcarWithRoom(self,num,max_weight_tolerable='',max_number_tolerable = '',packages = '',property = ''):
        conn = sq.connect("carWithRoom.db")
        cur = conn.cursor()
        if max_weight_tolerable != "":
            cur.execute(f'''UPDATE carWithRoom SET max_weight_tolerable={max_weight_tolerable} WHERE num = {num}''') 
            
        if max_number_tolerable != "":
            cur.execute(f'''UPDATE carWithRoom SET max_number_tolerable={max_number_tolerable} WHERE num = {num}''')
                     
        if packages != "":
            cur.execute(f'''UPDATE carWithRoom SET packages={packages} WHERE num = {num}''')  
                       
        if property != "":
            cur.execute(f'''UPDATE carWithRoom SET property={property} WHERE num = {num}''') 
                                    
        conn.commit()
        conn.close()
        
    def removecarWithRoom(self,num):
        conn = sq.connect("carWithRoom.db")
        cur = conn.cursor()
        cur.execute(f'''DELETE from carWithRoom WHERE num = {num}''')
        conn.commit()
        conn.close() 
        
        
class containerCar():
    def __init__(self,num,max_weight_tolerable,max_container_can_be_connected,property = ''):
        conn = sq.connect("containerCar.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS containerCar (num int PRIMARY KEY, max_weight_tolerable real,max_container_can_be_connected int,property text)''')
        cur.execute(f'''INSERT OR IGNORE INTO containerCar VALUES ({num},{max_weight_tolerable},{max_container_can_be_connected},'{property}')''')
        conn.commit()
        conn.close()
        
    def editcontainerCar(self,num,max_weight_tolerable = "",max_container_can_be_connected = '',property = ''):
        conn = sq.connect("containerCar.db")
        cur = conn.cursor()
        if max_weight_tolerable != "":
            cur.execute(f'''UPDATE containerCar SET max_weight_tolerable={max_weight_tolerable} WHERE num = {num}''') 
            
        if max_container_can_be_connected != "":
            cur.execute(f'''UPDATE containerCar SET max-container_can_be_connedcted={max_container_can_be_connected} WHERE num = {num}''') 
            
        if property != "":
            cur.execute(f'''UPDATE containerCar SET property={property} WHERE num = {num}''')                         
        conn.commit()
        conn.close() 
        
        
    def removecontainerCar(self,num):
        conn = sq.connect("containerCar.db")
        cur = conn.cursor()
        cur.execute(f'''DELETE from containerCar WHERE num = {num}''')
        conn.commit()
        conn.close()         
    
def showallPackages():
    conn = sq.connect('Packages.db')
    cur = conn.cursor()
    print("normal packages\nnumber - weight - destination - beginning") 
    for row in cur.execute('''SELECT * FROM Packages '''):
        print(row)
        
    conn = sq.connect('coldPackages.db')
    cur = conn.cursor()
    print("cold packages\n number - weight - destination - beginning - minimum tempreture - property") 
    for row in cur.execute('''SELECT * FROM coldPackages '''):
        print(row)   
    
    conn = sq.connect('breakablePackages.db')
    cur = conn.cursor()
    print("breakable packages\n number - weight - destination - beginning - property")
    for row in cur.execute('''SELECT * FROM breakablePackages '''):
        print(row)
    
def showallcontainers():
    conn = sq.connect('container.db')
    cur = conn.cursor()
    print("normal container")
    for row in cur.execute('''SELECT * FROM Container '''):
        print(row)
        
    conn = sq.connect('freezercontainer.db')
    cur = conn.cursor()
    print('freezer containers')
    for row in cur.execute('''SELECT * FROM freezerContainer '''):
        print(row)
         
    conn = sq.connect('breakablecontainer.db')
    cur = conn.cursor()        
    for row in cur.execute('''SELECT * FROM breakableContainer '''):
        print(row)  
        
        
def showallCars():
    conn = sq.connect("Car.db")     
    cur = conn.cursor()    
    print("normal cars")
    for row in cur.execute('''SELECT * FROM Car '''):
        print(row)
        
    conn = sq.connect("carWithRoom.db")     
    cur = conn.cursor()    
    print("cars with room")
    for row in cur.execute('''SELECT * FROM carWithRoom '''):
        print(row)
    
    conn = sq.connect("containerCar.db")     
    cur = conn.cursor() 
    print("container cars")
    for row in cur.execute('''SELECT * FROM containerCar '''):
        print(row)              

# def addPackageToCantainer(p_num,c_num,type_package,type_container):##3 type : normal_cold_breakable
#     conn = sq.connect("Container_Package.db")
#     cur= conn.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS Container_Package (num_package int PRIMARY KEY, num_container int PRIMARY KEY , type_package txt , type_container txt)''')
#     cur.execute(f'''INSERT OR IGNORE INTO Packages VALUES ({p_num},{c_num},{type_package},{type_container})''')
#     conn.commit()
#     conn.close()
        
def addPackageTocarWithRoom(p_num,c_num):
    conn = sq.connect("carWithRoom_Package.db")
    cur= conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS carWithRoom_Package (num_package int PRIMARY KEY,num_container int PRIMARY KEY)''')
    cur.execute(f'''INSERT OR IGNORE INTO carWithRoom VALUES ({p_num},{c_num})''')
    conn.commit()
    conn.close()

def addContainertoCar(container_num,car_num):
    conn = sq.connect("contianer_car.db")## this
    cur= conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS container_car (container_num int PRIMARY KEY,car_num int PRIMARY KEY)''')
    cur.execute(f'''INSERT OR IGNORE INTO container_car VALUES ({container_num},{car_num})''')
    conn.commit()
    conn.close()


def addPackageToCantainer(container_num):
    conn = sq.connect("Container.db")
    cur= conn.cursor()
    if (cur.execute(f'''SELECT EXISTS(SELECT 1 FROM Container WHERE num="{container_num}")''')):
        conn = sq.connect('Packages.db')
        cur = conn.cursor()
        print("normal packages\nnumber - weight - destination - beginning") 
        for row in cur.execute('''SELECT * FROM Packages '''):
            print(row)
        package_num = int(input("Enter package number : "))
        conn = sq.connect("Container_Package.db")
        cur= conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Container_Package (num_package int PRIMARY KEY, num_container int PRIMARY KEY , type_package txt , type_container txt)''')
        cur.execute(f'''INSERT OR IGNORE INTO Container_Package VALUES ({package_num},{container_num},"normal","normal")''')
        conn.commit()
        conn.close()
    
    elif (cur.execute(f'''SELECT EXISTS(SELECT 1 FROM freezerContainer WHERE num="{container_num}")''')):
        conn = sq.connect('coldPackages.db')
        cur = conn.cursor()
        print("cold packages\n number - weight - destination - beginning - minimum tempreture - property") 
        for row in cur.execute('''SELECT * FROM coldPackages '''):
            print(row) 
        package_num = int(input("Enter package number : "))
        conn = sq.connect("Container_Package.db")
        cur= conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Container_Package (num_package int PRIMARY KEY, num_container int PRIMARY KEY , type_package txt , type_container txt)''')
        cur.execute(f'''INSERT OR IGNORE INTO Container_Package VALUES ({package_num},{container_num},"cold","freezer")''')
        conn.commit()
        conn.close()
    
    elif (cur.execute(f'''SELECT EXISTS(SELECT 1 FROM breakableContainer WHERE num="{container_num}")''')):
        conn = sq.connect('breakablePackages.db')
        cur = conn.cursor()
        print("breakable packages\n number - weight - destination - beginning - property")
        for row in cur.execute('''SELECT * FROM breakablePackages '''):
            print(row)
        package_num = int(input("Enter package number : "))
        conn = sq.connect("Container_Package.db")
        cur= conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Container_Package (num_package int PRIMARY KEY, num_container int PRIMARY KEY , type_package txt , type_container txt)''')
        cur.execute(f'''INSERT OR IGNORE INTO Container_Package VALUES ({package_num},{container_num},"normal","normal")''')
        conn.commit()
        conn.close()



# x5 = Package(1,6,"hmd","tehran")
# x1 = breakablePackage(1,6,"hmd","tehran")
x2 = coldPackage(1,3,"azar","canada",0)
# x3 = Package(4,9,"america","turkey")


conn = sq.connect("Container_Package.db")
cur= conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Container_Package (num_package int PRIMARY KEY, num_container int PRIMARY KEY , type_package txt , type_container txt)''')
cur.execute(f'''INSERT OR IGNORE INTO Packages VALUES ({package_num},{container_num},{type_package},{type_container})''')
conn.commit()
conn.close()