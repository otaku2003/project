import sqlite3 as sq

def login():
    user = input("Enter username : ")
    password = input("Enter your password : ")
    if user == '1234' and password == '1234' :
        pass
    else: print("wrong username or password")

class Package:
    def __init__(self,num,weight,destination,beginning):
        try:
            conn = sq.connect("Packages.db")
            cur = conn.cursor()    
            cur.execute(f'SELECT 1 FROM Packages WHERE num={num} ')
            data = cur.fetchone()
            if data is not None:
                print('this number exists in Packages')
        except:pass        
        
        try:
            conn = sq.connect("coldPackages.db")
            cur = conn.cursor()    
            cur.execute(f'SELECT 1 FROM coldPackages WHERE num={num} ')
            data = cur.fetchone()
            if data is not None:
                print('this number exists in coldpackages')
        except:pass
        try:    
            conn = sq.connect("breakablePackages.db")
            cur = conn.cursor()    
            cur.execute(f'SELECT 1 FROM breakablePackages WHERE num={num} ')
            data = cur.fetchone()
            if data is not None:
                print("this number exists in  breakable packages")
        except:pass    
            
        else:
            conn = sq.connect("Packages.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS Packages (num int PRIMARY KEY , weight real, destination text, beginning text)''')
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
        cur.execute(f'''DELETE from Packages WHERE num = {num}''')
        conn.commit()
        conn.close()


   
    
class coldPackage:
    def __init__(self,num,weight,destination,beginning,min_temperature,property = ""):
        try:
            conn = sq.connect("coldPackages.db")
            cur = conn.cursor()    
            cur.execute(f'SELECT 1 FROM coldPackages WHERE num={num} ')
            data = cur.fetchone()
            if data is not None:
                print('this number exists in coldpackages')
        except:pass        
        try:
            conn = sq.connect("Packages.db")
            cur = conn.cursor()    
            cur.execute(f'SELECT 1 FROM Packages WHERE num={num} ')
            data = cur.fetchone()
            if data is not None:
                print("this number exists in packages")
        except:pass
        
        try:    
            conn = sq.connect("breakablePackages.db")
            cur = conn.cursor()    
            cur.execute(f'SELECT 1 FROM breakablePackages WHERE num={num} ')
            data = cur.fetchone()
            if data is not None:
                print("this number exists in breakable packages")
        except:pass
                
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
            try:    
                conn = sq.connect("breakablePackages.db")
                cur = conn.cursor()    
                cur.execute(f'SELECT 1 FROM breakablePackages WHERE num={num} ')
                data = cur.fetchone()
                if data is not None:
                    print("this number exists in breakable packages")
            except:pass
                
            try:
                conn = sq.connect("coldPackages.db")
                cur = conn.cursor()    
                cur.execute(f'SELECT 1 FROM coldPackages WHERE num={num} ')
                data = cur.fetchone()
                if data is not None:
                    print("this number exists in cold packages")
            except:pass

            try:
                conn = sq.connect("Packages.db")
                cur = conn.cursor()    
                cur.execute(f'SELECT 1 FROM Packages WHERE num={num} ')
                data = cur.fetchone()
                if data is not None:
                    print("this number exists in  packages") 
            except:pass

            else:
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
   

  
    

class Container():
    def __init__(self,num,max_weight,max_package,number_of_packages =0,weight = 0,property = ""):
        try:
            conn = sq.connect("Container.db")
            cur = conn.cursor()    
            cur.execute(f'SELECT 1 FROM Container WHERE num={num} ')
            data = cur.fetchone()
            if data is not None:
                print("this number exists in Container")
        except:pass        
        try:
            conn = sq.connect("freezerContainer.db")
            cur = conn.cursor()    
            cur.execute(f'SELECT 1 FROM freezerContainer WHERE num={num} ')
            data = cur.fetchone()
            if data is not None:
                print("this number exists in freezer containers")
        except:pass
        
        try:    
            conn = sq.connect("breakableContainer.db")
            cur = conn.cursor()    
            cur.execute(f'SELECT 1 FROM breakableContainer WHERE num={num} ')
            data = cur.fetchone()
            if data is not None:
                print("this number exists in breakable Container")
        except:pass
        
        else:
            conn = sq.connect("Container.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS Container (num int PRIMARY KEY, max_weight real, max_package int,number_of_packages int,weight real,property text)''')
            cur.execute(f'''INSERT OR IGNORE INTO Container VALUES ({num},{max_weight},{max_package},{number_of_packages},{weight},'{property}')''')
            conn.commit()
            conn.close()
        
        
    def editContainer(self,num,max_weight = "",max_package = "",property = ''):
        conn = sq.connect("Container.db")
        cur = conn.cursor()
        if max_weight != "":
            cur.execute(f'''UPDATE Container SET max_weight={max_weight} WHERE num = {num}''') 
            
        if max_package != "":
            cur.execute(f'''UPDATE Container SET max_package='{max_package}' WHERE num = {num}''')
             
        if property != "":
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
    def __init__(self,num,max_weight,max_package,min_temp_produced_by_container,number_of_packages=0,weight=0,property = ""):
        try:
            conn = sq.connect("freezerContainer.db")
            cur = conn.cursor()    
            cur.execute(f'SELECT 1 FROM freezerContainer WHERE num={num} ')
            data = cur.fetchone()
            if data is not None:
                print("this number exists in freezer containers")
        except:pass        
        try:
            conn = sq.connect("Container.db")
            cur = conn.cursor()    
            cur.execute(f'SELECT 1 FROM Container WHERE num={num} ')
            data = cur.fetchone()
            if data is not None:
                print("this number exists in Container")
        except:pass
        
        try:    
            conn = sq.connect("breakableContainer.db")
            cur = conn.cursor()    
            cur.execute(f'SELECT 1 FROM breakableContainer WHERE num={num} ')
            data = cur.fetchone()
            if data is not None:
                print("this number exists in breakable Containers")
        except:pass
        
        else:
            conn = sq.connect("freezerContainer.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS freezerContainer (num int PRIMARY KEY, max_weight real, max_package int,min_temp_produced_by_container int,number_of_packages int,weight real,property text)''')
            cur.execute(f'''INSERT OR IGNORE INTO freezerContainer VALUES ({num},{max_weight},{max_package},{min_temp_produced_by_container},{number_of_packages},{weight},'{property}')''')
            conn.commit()
            conn.close()

    def editfreezerContainer(self,num,max_weight = "",max_package = "",min_temp_produced_by_container = '',property = ''):
        conn = sq.connect("freezerContainer.db")
        cur = conn.cursor()
        if max_weight != "":
            cur.execute(f'''UPDATE freezerContainer SET max_weight={max_weight} WHERE num = {num}''') 
            
        if max_package != "":
            cur.execute(f'''UPDATE freezerContainer SET max_package='{max_package}' WHERE num = {num}''')
             
       
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
    def __init__(self,num,max_weight,max_package,max_speed_of_car,number_of_packages = 0,weight = 0,property = ""):
        try:    
            conn = sq.connect("breakableContainer.db")
            cur = conn.cursor()    
            cur.execute(f'SELECT 1 FROM breakableContainer WHERE num={num} ')
            data = cur.fetchone()
            if data is not None:
                print("this number exists in breakable Containers")
        except:pass        
        try:
            conn = sq.connect("Container.db")
            cur = conn.cursor()    
            cur.execute(f'SELECT 1 FROM Container WHERE num={num} ')
            data = cur.fetchone()
            if data is not None:
                print("this number exists in Container")
        except:pass
        
        try:    
            conn = sq.connect("freezerContainer.db")
            cur = conn.cursor()    
            cur.execute(f'SELECT 1 FROM freezerContainer WHERE num={num} ')
            data = cur.fetchone()
            if data is not None:
                print("this number exists in freezer container")
        except:pass
            
        else:
            conn = sq.connect("breakableContainer.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS breakableContainer (num int PRIMARY KEY, max_weight real, max_package int,max_speed_of_car int,number_of_packages int,weight real,property text)''')
            cur.execute(f'''INSERT OR IGNORE INTO breakableContainer VALUES ({num},{max_weight},{max_package},{max_speed_of_car},{number_of_packages},{weight},'{property}')''')
            conn.commit()
            conn.close()

    def editbreakableContainer(self,num,max_weight = "",max_package = "",max_speed_of_car = '',property = ''):
        conn = sq.connect("breakableContainer.db")
        cur = conn.cursor()
        if max_weight != "":
            cur.execute(f'''UPDATE breakableContainer SET max_weight={max_weight} WHERE num = {num}''') 
            
        if max_package != "":
            cur.execute(f'''UPDATE breakableContainer SET max_package={max_package} WHERE num = {num}''')

        if property != "":
            cur.execute(f'''UPDATE breakableContainer SET property='{property}' WHERE num = {num}''')  
            
        if max_speed_of_car != '':
            cur.execute(f'''UPDATE breakableContainer SET max_speed_of_car={max_speed_of_car} WHERE num = {num}''') 
            
        conn.commit()
        conn.close() 
        
    def removebreakableContainer(self,num):
        conn = sq.connect("breakableContainer.db")
        cur = conn.cursor()
        cur.execute(f'''DELETE from breakableContainer WHERE num = {num}''')
        conn.commit()
        conn.close()  
    
    
    
        
        
class carWithRoom():
    def __init__(self,num,max_weight,max_package,number_of_packages = 0,weight = 0,property = ''):
        try:        
            conn = sq.connect("carWithRoom.db")
            cur = conn.cursor()    
            cur.execute(f'SELECT 1 FROM carWithRoom WHERE num={num} ')
            data = cur.fetchone()
            if data is not None:
                print("this number exists in cars with room")                
        except:pass        
        try:
            conn = sq.connect("containerCar.db")
            cur = conn.cursor()    
            cur.execute(f'SELECT 1 FROM containerCar WHERE num={num} ')
            data = cur.fetchone()
            if data is not None:
                print("this number exists in container Cars")
        except:pass  
        else:
            conn = sq.connect("carWithRoom.db")
            cur = conn.cursor()                                                                                         
            cur.execute('''CREATE TABLE IF NOT EXISTS carWithRoom (num int PRIMARY KEY, max_weight real,max_package int,number_of_packages int,weight real,property text)''')
            cur.execute(f'''INSERT OR IGNORE INTO carWithRoom VALUES ({num},{max_weight},{max_package},{number_of_packages},{weight},'{property}')''')
            conn.commit()
            conn.close()
        
    def editcarWithRoom(self,num,max_weight_tolerable='',max_number_tolerable = '',property = ''):
        conn = sq.connect("carWithRoom.db")
        cur = conn.cursor()
        if max_weight_tolerable != "":
            cur.execute(f'''UPDATE carWithRoom SET max_weight_tolerable={max_weight_tolerable} WHERE num = {num}''') 
            
        if max_number_tolerable != "":
            cur.execute(f'''UPDATE carWithRoom SET max_number_tolerable={max_number_tolerable} WHERE num = {num}''')
                     
                       
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
    def __init__(self,num,max_weight,max_container_can_be_connected,number_of_containers = 0,weight = 0,property = ''):
        try:
            conn = sq.connect("containerCar.db")
            cur = conn.cursor()    
            cur.execute(f'SELECT 1 FROM containerCar WHERE num={num} ')
            data = cur.fetchone()
            if data is not None:
                print("this number exists in container Cars")
        except:pass  
        try:        
            conn = sq.connect("carWithRoom.db")
            cur = conn.cursor()    
            cur.execute(f'SELECT 1 FROM carWithRoom WHERE num={num} ')
            data = cur.fetchone()
            if data is not None:
                print("this number exists in cars with room")                
        except:pass
        else:
            conn = sq.connect("containerCar.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS containerCar (num int PRIMARY KEY, max_weight real,max_container_can_be_connected int,number_of_containers int,weight real,property text)''')
            cur.execute(f'''INSERT OR IGNORE INTO containerCar VALUES ({num},{max_weight},{max_container_can_be_connected},{number_of_containers},{weight},'{property}')''')
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
    print("normal container\n number - max_waight - max_package - current number of packages in container - current weight - property")
    for row in cur.execute('''SELECT * FROM Container '''):
        print(row)
        
    conn = sq.connect('freezercontainer.db')
    cur = conn.cursor()
    print('freezer containers\n number - max_weight - max_package - min temperature container can produce - current number of packages in container - weight - property')
    for row in cur.execute('''SELECT * FROM freezerContainer '''):
        print(row)
         
    conn = sq.connect('breakablecontainer.db')
    cur = conn.cursor() 
    print("breakable container\n number - max_weight - max_package _ max_speed - current number of packages in container - weight - property")       
    for row in cur.execute('''SELECT * FROM breakableContainer '''):
        print(row)  
        
        
def showallCars():
    conn = sq.connect("carWithRoom.db")     
    cur = conn.cursor()    
    print("cars with room\n number - max_weight - max_package _ current number of packages - weight - peoperty ")
    for row in cur.execute('''SELECT * FROM carWithRoom '''):
        print(row)
    
    conn = sq.connect("containerCar.db")     
    cur = conn.cursor() 
    print("container cars\n number - max_weight - max_containers _ current number of containers - weight - property ")
    for row in cur.execute('''SELECT * FROM containerCar '''):
        print(row)              

        
def addPackageTocarWithRoom(car_num):
    conn = sq.connect("carWithRoom.db")
    cur = conn.cursor()   
    cur.execute(f'SELECT 1 FROM carWithRoom WHERE num={car_num} ')
    data = cur.fetchone()
    if data is None:
        print('container car doesnt exist')
    else:
        conn = sq.connect("carWithRoom.db")
        cur = conn.cursor()
        cur.execute(f'''SELECT number_of_packages FROM carWithRoom WHERE num = {car_num}''')
        for row in cur:
            packages_number_in_car_with_room = row
        cur.execute(f'''SELECT max_package FROM carWithRoom WHERE num = {car_num}''')
        for row in cur:
            max_package = row
        if(packages_number_in_car_with_room[0]>= max_package[0]):
            print("The capacity of the number of car with room is complete ")  
            
                        
        else:
            cur.execute(f'''SELECT weight FROM carWithRoom WHERE num = {car_num}''')
            for row in cur:
                Car_weight = row
            
            conn = sq.connect("carWithRoom.db")
            cur = conn.cursor()
            
            cur.execute(f'''SELECT max_weight FROM carWithRoom WHERE num = {car_num}''')
            for row in cur:
                max_car_weight = row
            if(Car_weight[0]>=max_car_weight[0]):
                print("The weight capacity of the car with room is complete")
            else:
                conn = sq.connect('Packages.db')
                cur = conn.cursor()
                print("normal packages\nnumber - weight - destination - beginning") 
                for row in cur.execute('''SELECT * FROM Packages '''):
                    print(row)
                    
                input_string = input("enter numbers seperated by space :")
                package_num_list = input_string.split()
                for i in range(len(package_num_list)):
                    package_num_list[i] = int(package_num_list[i])
                
                for package_num in package_num_list:
                    
                    conn = sq.connect("Container_Packages.db")
                    cur = conn.cursor()    
                    cur.execute(f'SELECT 1 FROM Container_Packages WHERE num_package={package_num} ')
                    data = cur.fetchone()
                    if data is not None:
                        print(f"package {package_num} is already exist in a container")
 


                    else:

                        conn = sq.connect("Car_Packages.db")
                        cur = conn.cursor()    
                        cur.execute(f'SELECT 1 FROM Car_Packages WHERE num_package={package_num} ')
                        data = cur.fetchone()
                        if data is not None:
                            print(f"package {package_num} is already exist in a car with room")

                        else:
                        
                            conn = sq.connect("Packages.db")
                            cur = conn.cursor()
                            cur.execute(f'''SELECT weight FROM Packages WHERE num = {package_num} ''')
                            for row in cur:
                                package_weight = row
                            if Car_weight[0] + package_weight[0] > max_car_weight[0]:
                                print("By adding this package, the weight of the container exceeds its limit")    
                            else:
                                conn = sq.connect("carWithRoom.db")
                                cur = conn.cursor() 
                                cur.execute(f'''UPDATE carWithRoom SET weight ={Car_weight[0]+ package_weight[0]} , number_of_packages = {packages_number_in_car_with_room[0]+1} WHERE num={car_num}''')
                                conn.commit()
                                conn.close()
                                conn = sq.connect("Car_Packages.db")
                                cur = conn.cursor()
                                cur.execute('''CREATE TABLE IF NOT EXISTS Car_Packages (num_package int PRIMARY KEY , num_carWithRoom int, type_Package text, type_carWithRoom text)''')
                                cur.execute(f'''INSERT OR IGNORE INTO Car_Packages VALUES ({package_num},{car_num},'normal','normal')''')
                                conn.commit()
                                conn.close()                  


def addContainertoCar(container_num):
    
    conn = sq.connect("containerCar_Container.db")
    cur = conn.cursor()   
    cur.execute(f'SELECT 1 FROM containerCar_Container WHERE Container_num={container_num} ')
    data = cur.fetchone()
    if data is not None:
        print("Container is already connected in another car")
    else:
    
        conn = sq.connect("Container.db")
        cur = conn.cursor()   
        cur.execute(f'SELECT 1 FROM Container WHERE num={container_num} ')
        data = cur.fetchone()
        if data is not None:
            
            cur.execute(f'''SELECT weight FROM Container WHERE num = {container_num}''')
            for row in cur:
                container_weight = row
            
            conn = sq.connect("containerCar.db")
            cur = conn.cursor() 
            print("container cars\n number - max_weight - max_containers _ current number of containers - weight - property ") 
            for row in cur.execute(f"SELECT * FROM containerCar "):
                print(row)     
                
                
            input_string = input("enter numbers seperated by space :")
            containerCar_num_list = input_string.split()
            for i in range(len(containerCar_num_list)):
                containerCar_num_list[i] = int(containerCar_num_list[i])                
            
            for containerCar_num in containerCar_num_list: 
                conn = sq.connect("containerCar.db")
                cur = conn.cursor() 
                cur.execute(f'''SELECT weight FROM containerCar WHERE num = {containerCar_num}''')  
                for row in cur:
                    containerCar_weight = row    

                cur.execute(f'''SELECT max_weight FROM containerCar WHERE num = {containerCar_num}''') 
                for row in cur:
                    max_weight_containerCar = row   

                if(max_weight_containerCar[0]< containerCar_weight[0]+container_weight[0]):
                    print(f"By adding  container {containerCar_num}, the weight of the container car exceeds its limit")

                else:
                    cur.execute(f'''SELECT number_of_containers FROM containerCar WHERE num = {containerCar_num}''')
                    for row in cur:
                        number_of_containers_in_car = row

                    cur.execute(f'''SELECT max_container_can_be_connected FROM containerCar WHERE num = {containerCar_num}''')
                    for row in cur:
                        max_number_of_container_in_car = row

                    if(number_of_containers_in_car>=max_number_of_container_in_car):
                        print(f"The capacity of the vehicle for the container {containerCar_num} is complete")

                    else:
                        conn = sq.connect('containerCar.db')
                        cur = conn.cursor()
                        cur.execute(f'''UPDATE containerCar SET weight ={containerCar_weight[0]+ container_weight[0]} , number_of_containers = {number_of_containers_in_car[0]+1} WHERE num={containerCar_num}''')
                        conn = sq.connect("containerCar_Container.db")
                        cur = conn.cursor()
    
                        cur.execute('''CREATE TABLE IF NOT EXISTS containerCar_Container (Container_num int PRIMARY KEY,containerCar_num int ,type_container text)''')
                        cur.execute(f'''INSERT OR IGNORE INTO containerCar_Container VALUES ({container_num},{containerCar_num},'normal')''')
                        conn.commit()
                        conn.close()
                        
        conn = sq.connect("freezerContainer.db")
        cur = conn.cursor()   
        cur.execute(f'SELECT 1 FROM freezerContainer WHERE num={container_num} ')
        data = cur.fetchone()
        if data is not None:
            cur.execute(f'''SELECT weight FROM freezerContainer WHERE num = {container_num}''')
            for row in cur:
                container_weight = row
            
            conn = sq.connect("containerCar.db")
            cur = conn.cursor() 
            print("container cars\n number - max_weight - max_containers _ current number of containers - weight - property ") 
            for row in cur.execute(f"SELECT * FROM containerCar "):
                print(row)     
                
            input_string = input("enter numbers seperated by space :")
            containerCar_num_list = input_string.split()
            for i in range(len(containerCar_num_list)):
                containerCar_num_list[i] = int(containerCar_num_list[i])                
            
            for containerCar_num in containerCar_num_list:                
            
            
                cur.execute(f'''SELECT weight FROM containerCar WHERE num = {containerCar_num}''')  
                for row in cur:
                    containerCar_weight = row    

                cur.execute(f'''SELECT max_weight FROM containerCar WHERE num = {containerCar_num}''') 
                for row in cur:
                    max_weight_containerCar = row   

                if(max_weight_containerCar[0]< containerCar_weight[0]+container_weight[0]):
                    print(f"By adding container{containerCar_num}, the weight of the container car exceeds its limit")

                else:
                    cur.execute(f'''SELECT number_of_containers FROM containerCar WHERE num = {containerCar_num}''')
                    for row in cur:
                        number_of_containers_in_car = row

                    cur.execute(f'''SELECT max_container_can_be_connected FROM containerCar WHERE num = {containerCar_num}''')
                    for row in cur:
                        max_number_of_container_in_car = row

                    if(number_of_containers_in_car>=max_number_of_container_in_car):
                        print(f"The capacity of the vehicle for the container {containerCar_num} is complete")

                    else:
                        conn = sq.connect("contaeinerCar_Container.db")
                        cur = conn.cursor()
    
                        cur.execute('''CREATE TABLE IF NOT EXISTS container_car (Container_num int PRIMARY KEY,containerCar_num int ,type_container text)''')
                        cur.execute(f'''INSERT OR IGNORE INTO container_car VALUES ({container_num},{containerCar_num},'cold')''')
                        conn.commit()
                        conn.close()
                    
        conn = sq.connect("breakableContainer.db")
        cur = conn.cursor()   
        cur.execute(f'SELECT 1 FROM breakableContainer WHERE num={container_num} ')
        data = cur.fetchone()
        if data is not None:
            cur.execute(f'''SELECT weight FROM breakableContainer WHERE num = {container_num}''')
            for row in cur:
                container_weight = row
            
            conn = sq.connect("containerCar.db")
            cur = conn.cursor() 
            print("container cars\n number - max_weight - max_containers _ current number of containers - weight - property ") 
            for row in cur.execute(f"SELECT * FROM containerCar "):
                print(row)     
            
            input_string = input("enter numbers seperated by space :")
            containerCar_num_list = input_string.split()
            for i in range(len(containerCar_num_list)):
                containerCar_num_list[i] = int(containerCar_num_list[i])                
            
            for containerCar_num in containerCar_num_list:                
 
            
                cur.execute(f'''SELECT weight FROM containerCar WHERE num = {containerCar_num}''')  
                for row in cur:
                    containerCar_weight = row    

                cur.execute(f'''SELECT max_weight FROM containerCar WHERE num = {containerCar_num}''') 
                for row in cur:
                    max_weight_containerCar = row   

                if(max_weight_containerCar[0]< containerCar_weight[0]+container_weight[0]):
                    print(f"By adding  container {containerCar_num}, the weight of the container car exceeds its limit")

                else:
                    cur.execute(f'''SELECT number_of_containers FROM containerCar WHERE num = {containerCar_num}''')
                    for row in cur:
                        number_of_containers_in_car = row

                    cur.execute(f'''SELECT max_container_can_be_connected FROM containerCar WHERE num = {containerCar_num}''')
                    for row in cur:
                        max_number_of_container_in_car = row

                    if(number_of_containers_in_car>=max_number_of_container_in_car):
                        print(f"The capacity of the vehicle for the container {containerCar_num} is complete")

                    else:
                        conn = sq.connect("contaeinerCar_Container.db")
                        cur = conn.cursor()
    
                        cur.execute('''CREATE TABLE IF NOT EXISTS container_car (Container_num int PRIMARY KEY,containerCar_num int ,type_container text)''')
                        cur.execute(f'''INSERT OR IGNORE INTO container_car VALUES ({container_num},{containerCar_num},'breakable')''')
                        conn.commit()
                        conn.close()
        
        
                   
def addPackageToCantainer(container_num):
    
    conn = sq.connect("Container.db")
    cur = conn.cursor()   
    cur.execute(f'SELECT 1 FROM Container WHERE num={container_num} ')
    data = cur.fetchone()
    if data is not None:
        conn = sq.connect("Container.db")
        cur = conn.cursor()
        cur.execute(f'''SELECT number_of_packages FROM Container WHERE num = {container_num}''')
        for row in cur:
            packages_number_in_container = row
        cur.execute(f'''SELECT max_package FROM Container WHERE num = {container_num}''')
        for row in cur:
            max_package = row
        if(packages_number_in_container[0]>= max_package[0]):
            print("The capacity of the number of containers is complete ")
        
        else:
            cur.execute(f'''SELECT weight FROM Container WHERE num = {container_num}''')
            for row in cur:
                Container_weight = row
                
            cur.execute(f'''SELECT max_weight FROM Container WHERE num = {container_num}''')
            for row in cur:
                max_container_weight = row
            if(Container_weight[0]>=max_container_weight[0]):
                print("The weight capacity of the container is complete")
            else:
                conn = sq.connect('Packages.db')
                cur = conn.cursor()
                print("normal packages\nnumber - weight - destination - beginning") 
                for row in cur.execute('''SELECT * FROM Packages '''):
                    print(row)
                    
                input_string = input("enter numbers seperated by space :")
                package_num_list = input_string.split()
                for i in range(len(package_num_list)):
                    package_num_list[i] = int(package_num_list[i])
                
                for package_num in package_num_list:                    
                
                
                    # conn = sq.connect("Container_Packages.db")
                    # cur = conn.cursor()
                    # cur.execute(f"SELECT 1 FROM Container_packages WHERE num_package = {package_num}")
                    # data=cur.fetchone()
                    # if data is not None:
                    #     print(f"package {package_num} is already exist in a container")

                    # else:
                        conn = sq.connect("Car_Packages.db")
                        cur = conn.cursor()
                        cur.execute(f"SELECT 1 FROM Car_packages WHERE num_package = {package_num}")
                        data=cur.fetchone()
                        if data is not None:
                            print(f"package {package_num} is already exist in a car with room")

                        else:
                        
                            conn = sq.connect("Packages.db")
                            cur = conn.cursor()
                            cur.execute(f'''SELECT weight FROM Packages WHERE num = {package_num} ''')
                            package_weight = cur.fetchone()


                            if Container_weight[0] + package_weight[0] > max_container_weight[0]:
                                print(f"By adding  package {package_num}, the weight of the container exceeds its limit")    


                            else:
                                conn = sq.connect("Container.db")
                                cur = conn.cursor() 

                                cur.execute(f'''UPDATE Container SET weight ={Container_weight[0]+ package_weight[0]} , number_of_packages = {packages_number_in_container[0]+1} WHERE num={container_num}''')
                                conn.commit()
                                conn.close()

                                conn = sq.connect("Container_Packages.db")
                                cur = conn.cursor()

                                cur.execute('''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
                                cur.execute(f'''INSERT OR IGNORE INTO Container_Packages VALUES ({package_num},{container_num},'normal','normal')''')

                                conn.commit()
                                conn.close()

    
    # #############################
    
    conn = sq.connect("freezerContainer.db")
    cur = conn.cursor()   
    cur.execute(f'SELECT 1 FROM freezerContainer WHERE num={container_num} ')
    data = cur.fetchone()
    if data is not None:
        conn = sq.connect("freezerContainer.db")
        cur = conn.cursor()
        cur.execute(f'''SELECT num FROM freezerContainer WHERE num = {container_num}''')
        for row in cur:
            packages_number_in_container = row
        cur.execute(f'''SELECT max_package FROM freezerContainer WHERE num = {container_num}''')
        for row in cur:
            max_package = row
        if(packages_number_in_container[0]>= max_package[0]):
            print("The capacity of the number of freezer containers is complete ")
        else:
            cur.execute(f'''SELECT weight FROM freezerContainer WHERE num = {container_num}''')
            for row in cur:
                Container_weight = row
                
            cur.execute(f'''SELECT max_weight FROM freezerContainer WHERE num = {container_num}''')
            for row in cur:
                max_container_weight = row
            if(Container_weight[0]>=max_container_weight[0]):
                print("The weight capacity of the freezer container is complete")
            else:
                conn = sq.connect('coldPackages.db')
                cur = conn.cursor()
                print("cold packages\n number - weight - destination - beginning - minimum tempreture - property") 
                for row in cur.execute('''SELECT * FROM coldPackages '''):
                    print(row) 
                    
                input_string = input("enter numbers seperated by space :")
                package_num_list = input_string.split()
                for i in range(len(package_num_list)):
                    package_num_list[i] = int(package_num_list[i])
                
                for package_num in package_num_list:                
                
                    conn = sq.connect("Container_Packages.db")
                    cur = conn.cursor()   
                    cur.execute(f'SELECT 1 FROM Container_Packages WHERE num={package_num} ')
                    data = cur.fetchone()
                    if data is not None:
                        print(f"package {package_num} is already exist in a container")

                    else:
                        conn = sq.connect("Car_Packages.db")
                        cur = conn.cursor()   
                        cur.execute(f'SELECT 1 FROM Car_Packages WHERE num={package_num} ')
                        data = cur.fetchone()
                        if data is not None:
                            print(f"package {package_num} is already exist in a car with room")

                        else:
                            conn = sq.connect("coldPackages.db")
                            cur = conn.cursor()
                            cur.execute(f'''SELECT weight FROM coldPackages WHERE num = {package_num} ''')
                            for row in cur:
                                package_weight = row


                            if Container_weight[0] + package_weight[0] > max_container_weight[0]:
                                print(f"By adding package {package_num}, the weight of the freezer container exceeds its limit")    


                            else:

                                conn = sq.connect("freezerContainer.db")
                                cur = conn.cursor()
                                cur.execute(f'''SELECT min_temp_produced_by_container FROM coldPackages WHERE num = {container_num} ''')
                                for row in cur:
                                    min_temp_container = row

                                conn = sq.connect("coldPackages.db")
                                cur = conn.cursor()
                                cur.execute(f'''SELECT min_temperature FROM coldPackages WHERE num = {package_num} ''')
                                for row in cur:
                                    min_temp_package = row

                                if(min_temp_container[0]>min_temp_package[0]):
                                    print(f"The package {package_num} will be spoiled in this container")

                                else:
                                
                                    conn = sq.connect("freezerContainer.db")
                                    cur = conn.cursor() 

                                    cur.execute(f'''UPDATE freezerContainer SET weight ={Container_weight[0]+ package_weight[0]} , number_of_packages = {packages_number_in_container[0]+1} WHERE num={container_num}''')
                                    conn.commit()
                                    conn.close()

                                    conn = sq.connect("Container_Packages.db")
                                    cur = conn.cursor()
                                    cur.execute('''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
                                    cur.execute(f'''INSERT OR IGNORE INTO Container_Packages VALUES ({package_num},{container_num},'cold','cold')''')

                                    conn.commit()
                                    conn.close()

#################################
    
    conn = sq.connect("breakableContainer.db")
    cur = conn.cursor()   
    cur.execute(f'SELECT 1 FROM breakableContainer WHERE num={container_num} ')
    data = cur.fetchone()
    if data is not None:
        conn = sq.connect("breakableContainer.db")
        cur = conn.cursor()
        cur.execute(f'''SELECT num FROM breakableContainer WHERE num = {container_num}''')
        for row in cur:
            packages_number_in_container = row
        cur.execute(f'''SELECT max_package FROM breakableContainer WHERE num = {container_num}''')
        for row in cur:
            max_package = row
        if(packages_number_in_container[0]>= max_package[0]):
            print("The capacity of the number of breakable containers is complete ")
        else:
            cur.execute(f'''SELECT weight FROM breakableContainer WHERE num = {container_num}''')
            for row in cur:
                Container_weight = row
                
            cur.execute(f'''SELECT max_weight FROM breakableContainer WHERE num = {container_num}''')
            for row in cur:
                max_container_weight = row
            if(Container_weight[0]>=max_container_weight[0]):
                print("The weight capacity of the breakable container is complete")
            else:
                conn = sq.connect('breakablePackages.db')
                cur = conn.cursor()
                print("breakable packages\n number - weight - destination - beginning - property")
                for row in cur.execute('''SELECT * FROM breakablePackages '''):
                    print(row)

                input_string = input("enter numbers seperated by space :")
                package_num_list = input_string.split()
                for i in range(len(package_num_list)):
                    package_num_list[i] = int(package_num_list[i])
                
                for package_num in package_num_list:
                
                
                
                    conn = sq.connect("Container_Packages.db")
                    cur = conn.cursor()   
                    cur.execute(f'SELECT 1 FROM Container_Packages WHERE num={package_num} ')
                    data = cur.fetchone()
                    if data is not None:
                        print(f"package {package_num} is already exist in a container")
                    else:
                        conn = sq.connect("Car_Packages.db")
                        cur = conn.cursor()   
                        cur.execute(f'SELECT 1 FROM Car_Packages WHERE num={package_num} ')
                        data = cur.fetchone()
                        if data is not None:
                            print(f"package {package_num} is already exist in a car with room")
                        else:
                            conn = sq.connect("breakablePackages.db")
                            cur = conn.cursor()
                            cur.execute(f'''SELECT weight FROM breakablePackages WHERE num = {package_num} ''')
                            for row in cur:
                                package_weight = row


                            if Container_weight[0] + package_weight[0] > max_container_weight[0]:
                                print(f"By adding package {package_num}, the weight of the breakable container exceeds its limit")    


                            else:
                                conn = sq.connect("breakableContainer.db")
                                cur = conn.cursor() 

                                cur.execute(f'''UPDATE breakableContainer SET weight ={Container_weight[0]+ package_weight[0]} , number_of_packages = {packages_number_in_container[0]+1} WHERE num={container_num}''')
                                conn.commit()
                                conn.close()

                                conn = sq.connect("Container_Packages.db")
                                cur = conn.cursor()

                                cur.execute('''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
                                cur.execute(f'''INSERT OR IGNORE INTO Container_Packages VALUES ({package_num},{container_num},'breakable','breakable')''')

                                conn.commit()
                                conn.close()


                            

                         
def ShowPackagesWaitingForReceive(): 
    pass
        
        

def export_waybill():
    conn = sq.connect("Car_Packages.db")
    cur = conn.cursor()
    cur.execute('''SELECT num_carWithRoom FROM Car_Packages ''')
    carWithRoom_keys = cur.fetchall()
    carWithRoom_keys = list(set(carWithRoom_keys))
    
    
    conn = sq.connect("containerCar_Container.db")
    cur = conn.cursor()
    cur.execute('''SELECT containerCar_num FROM containerCar_Container''')
    containerCar_keys = cur.fetchall()
    containerCar_keys = list(set(containerCar_keys))
    
    conn = sq.connect("carWithRoom.db")
    cur = conn.cursor()
    print("car with rooms\n number - max_weight - max_package - currnet number of packages in car - current weight - property")
    for i in carWithRoom_keys:
        for row in cur.execute(f'''SELECT * FROM carWithRoom WHERE num = {i[0]}'''):
            print(row)
    
    conn = sq.connect("containerCar.db") 
    cur = conn.cursor()
    print("container cars\n number - max_weight - max_container - current number of containers in car - current weight - property")
    for i in containerCar_keys:
        for row in cur.execute(f'''SELECT * FROM containerCar WHERE num = {i[0]}'''):
            print(row)    
            
    input_string = input("enter numbers seperated by space :")
    car_num_list = input_string.split()
    for i in range(len(car_num_list)):
        car_num_list[i] = int(car_num_list[i])
    
    for car_num in car_num_list:    
        conn = sq.connect("carWithRoom.db")
        cur = conn.cursor()   
        cur.execute(f'SELECT 1 FROM carWithRoom WHERE num={car_num} ')
        data = cur.fetchone()
        if data is not None:
            conn = sq.connect('Car_Packages.db')
            cur = conn.cursor()
            cur.execute(f'''SELECT num_package FROM Car_Packages WHERE num_carWithRoom = {car_num}''')
            package_keys = cur.fetchall()
            
            
            
            conn = sq.connect('carWithRoom.db')
            cur = conn.cursor()
            cur.execute(f'''SELECT * FROM carWithRoom WHERE num = {car_num}''')
            car = cur.fetchall()
        
            conn = sq.connect('waybill.db')
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS carWithRoom (num int PRIMARY KEY, max_weight real,max_package int,number_of_packages int,weight real,property text)''')
            cur.execute(f'''INSERT OR IGNORE INTO carWithRoom VALUES ({car[0][0]},{car[0][1]},{car[0][2]},{car[0][3]},{car[0][4]},'{car[0][5]}')''')   
            conn.commit()
            conn.close()
            
            conn = sq.connect("carWithRoom.db")
            cur = conn.cursor()
            cur.execute(f'''DELETE from carWithRoom WHERE num = {car_num}''')
            conn.commit()
            conn.close()
            
            
            for package_key in package_keys:
            
                conn = sq.connect('waybill.db')
                cur = conn.cursor()
                cur.execute('''CREATE TABLE IF NOT EXISTS Car_Packages (package_num int PRIMARY KEY , car_num int)''')
                cur.execute(f'''INSERT OR IGNORE INTO Car_Packages VALUES ({package_key[0]},{car_num})''') 
                conn.commit()
                conn.close() 
            
        
                conn = sq.connect('Packages.db')
                cur = conn.cursor()
                cur.execute(f'''SELECT * FROM Packages WHERE num = {package_key[0]}''')
                package = cur.fetchall()
                
                conn = sq.connect('waybill.db')
                cur = conn.cursor()
                cur.execute('''CREATE TABLE IF NOT EXISTS Packages (package_num int PRIMARY KEY ,  weight real ,destinaton text , beginning text)''')
                cur.execute(f'''INSERT OR IGNORE INTO Packages VALUES ({package[0][0]},{package[0][1]},'{package[0][2]}','{package[0][3]}')''')     
                conn.commit()
                conn.close()
        
                conn = sq.connect("Packages.db")
                cur = conn.cursor()
                cur.execute(f'''DELETE from Packages WHERE num = {package_key[0]}''')
                conn.commit()
                conn.close()
                
                conn = sq.connect("Car_Packages.db")
                cur = conn.cursor()
                cur.execute(f'''DELETE from Car_Packages WHERE num_package = {package_key[0]}''')
                conn.commit()
                conn.close()
        
        
        
        
        conn = sq.connect("containerCar.db")
        cur = conn.cursor()   
        cur.execute(f'SELECT 1 FROM containerCar WHERE num={car_num} ')
        data = cur.fetchone()
        if data is not None: 
            conn = sq.connect('containerCar_Container.db')
            cur = conn.cursor()
            cur.execute(f'''SELECT Container_num FROM containerCar_Container WHERE containerCar_num = {car_num}''')
            container_keys = cur.fetchall()
            
            
            for container_key in container_keys:
                conn = sq.connect('containerCar_Container.db')
                cur = conn.cursor()
                cur.execute(f'''SELECT type_container FROM containerCar_Container WHERE Container_num = {container_key[0]}''')
                type_container = cur.fetchone()
                   
                
                conn = sq.connect('waybill.db')
                cur = conn.cursor()
                cur.execute(f'''CREATE TABLE IF NOT EXISTS container_incontainerCar (container_num int PRIMARY KEY , containerCar_num int, type_contianer text )''')        
                cur.execute(f'''INSERT OR IGNORE INTO container_incontainerCar VALUES ({container_key[0]},{car_num},'{type_container[0]}')''')
                conn.commit()
                conn.close()
                
                
                conn = sq.connect('containerCar.db')
                cur = conn.cursor()
                cur.execute(f'''SELECT * FROM containerCar WHERE num = {car_num}''')
                car = cur.fetchall()

                conn = sq.connect('waybill.db')
                cur = conn.cursor()
                cur.execute('''CREATE TABLE IF NOT EXISTS containerCar (num int PRIMARY KEY, max_weight real,max_container_can_be_connected int,number_of_containers int,weight real,property text)''')
                cur.execute(f'''INSERT OR IGNORE INTO containerCar VALUES ({car[0][0]},{car[0][1]},{car[0][2]},{car[0][3]},{car[0][4]},'{car[0][5]}')''')   
                conn.commit()
                conn.close()

                conn = sq.connect("containerCar.db")
                cur = conn.cursor()
                cur.execute(f'''DELETE from containerCar WHERE num = {car_num}''')
                conn.commit()
                conn.close()
                
                conn = sq.connect("containerCar_Container.db")
                cur = conn.cursor()
                cur.execute(f'''DELETE from containerCar_Container WHERE Container_num = {container_key[0]}''')
                conn.commit()
                conn.close()
                
            
                conn = sq.connect('Container_Packages.db')
                cur = conn.cursor()
                cur.execute(f'''SELECT num_package FROM Container_Packages WHERE num_Container = {container_key[0]}''')
                package_keys = cur.fetchall()
                if type_container[0] == 'normal':
                        conn = sq.connect('Container.db')
                        cur = conn.cursor()
                        cur.execute(f'''SELECT * FROM Container WHERE num = {container_key[0]}''')
                        container = cur.fetchone()
                        
                        cur.execute(f'''DELETE FROM Container WHERE num = {container_key[0]}''')
                        
                        conn = sq.connect("waybill")
                        cur = conn.cursor()
                        cur.execute('''CREATE TABLE IF NOT EXISTS Container (num int PRIMARY KEY ,  max_weight real ,max_package int , number_of_packages int,weight real ,type_container text, property text)''')
                        cur.execute(f'''INSERT OR IGNORE INTO Packages VALUES ({container[0]},{container[1]},{container[2]},{container[3]},{container[4]},'normal','{container[5]}')''')
                        conn.commit()
                        conn.close()
                                            
                        for package_key in package_keys:
                            conn = sq.connect('waybill.db')
                            cur = conn.cursor()
                            cur.execute(f'''CREATE TABLE IF NOT EXISTS packages_inContainer (num_package int PEIMARY KEY,num_container int,type_package text)''')
                            cur.execute(f'''INSERT OR IGNORE INTO packages_inContainer VALUES({package_key[0]},{container_key[0]},'normal')''')        
                            conn.commit()
                            conn.close()


                            conn = sq.connect('Packages.db')
                            cur = conn.cursor()
                            cur.execute(f'''SELECT * FROM Packages WHERE num = {package_key[0]} ''')
                            package = cur.fetchone()

                            conn = sq.connect("Packages.db")
                            cur = conn.cursor()
                            cur.execute(f'''DELETE from Packages WHERE num = {package_key[0]}''')
                            conn.commit()
                            conn.close()

                            conn = sq.connect('waybill.db')
                            cur = conn.cursor()
                            cur.execute('''CREATE TABLE IF NOT EXISTS Packages (package_num int PRIMARY KEY ,  weight real ,destinaton text , beginning text)''')
                            cur.execute(f'''INSERT OR IGNORE INTO Packages VALUES ({package[0]},{package[1]},'{package[2]}','{package[3]}')''')     
                            conn.commit()
                            conn.close()
                if type_container == 'cold' :  
                       
                        conn = sq.connect('freezerContainer.db')
                        cur = conn.cursor()
                        cur.execute(f'''SELECT * FROM freeerContainer WHERE num = {container_key[0]}''')
                        container = cur.fetchone()
                        
                        cur.execute(f'''DELETE FROM freezerContainer WHERE num = {container_key[0]}''')
                        
                        conn = sq.connect("waybill")
                        cur = conn.cursor()
                        cur.execute('''CREATE TABLE IF NOT EXISTS Container (num int PRIMARY KEY ,  max_weight real ,max_package int , number_of_packages int,weight real ,type_container text, property text)''')
                        cur.execute(f'''INSERT OR IGNORE INTO Packages VALUES ({container[0]},{container[1]},{container[2]},{container[3]},{container[4]},'cold','{container[5]}')''')
                        conn.commit()
                        conn.close()          
                        for package_key in package_keys:
                            conn = sq.connect('waybill.db')
                            cur = conn.cursor()
                            cur.execute(f'''CREATE TABLE IF NOT EXISTS packages_inContainer (num_package int PEIMARY KEY,num_container int,type_package text)''')
                            cur.execute(f'''INSERT OR IGNORE INTO packages_inContainer VALUES({package_key[0]},{container_key},'cold')''')        
                            conn.commit()
                            conn.close()


                            conn = sq.connect('coldPackages.db')
                            cur = conn.cursor()
                            cur.execute(f'''SELECT * FROM coldPackages WHERE num = {package_key[0]} ''')
                            package = cur.fetchone()

                            conn = sq.connect("coldPackages.db")
                            cur = conn.cursor()
                            cur.execute(f'''DELETE from coldPackages WHERE num = {package_key[0]}''')
                            conn.commit()
                            conn.close()

                            conn = sq.connect('waybill.db')
                            cur = conn.cursor()
                            cur.execute('''CREATE TABLE IF NOT EXISTS Packages (package_num int PRIMARY KEY ,  weight real ,destinaton text , beginning text)''')
                            cur.execute(f'''INSERT OR IGNORE INTO Packages VALUES ({package[0]},{package[1]},'{package[2]}','{package[3]}')''')     
                            conn.commit()
                            conn.close()
                      
                if type_container == 'breakable':
                    conn = sq.connect('breakableContainer.db')
                    cur = conn.cursor()
                    cur.execute(f'''SELECT * FROM breakableContainer WHERE num = {container_key[0]}''')
                    container = cur.fetchone()
                    
                    cur.execute(f'''DELETE FROM breakableContainer WHERE num = {container_key[0]}''')
                    
                    conn = sq.connect("waybill")
                    cur = conn.cursor()
                    cur.execute('''CREATE TABLE IF NOT EXISTS Container (num int PRIMARY KEY ,  max_weight real ,max_package int , number_of_packages int,weight real ,type_container text, property text)''')
                    cur.execute(f'''INSERT OR IGNORE INTO Packages VALUES ({container[0]},{container[1]},{container[2]},{container[3]},{container[4]},'breakable','{container[5]}')''')
                    conn.commit()
                    conn.close()
                    for package_key in package_keys:
                            conn = sq.connect('waybill.db')
                            cur = conn.cursor()
                            cur.execute(f'''CREATE TABLE IF NOT EXISTS packages_inContainer (num_package int PEIMARY KEY,num_container int,type_package text)''')
                            cur.execute(f'''INSERT OR IGNORE INTO packages_inContainer VALUES({package_key[0]},{container_key},'breakable')''')        
                            conn.commit()
                            conn.close()                            
                            conn = sq.connect('breakablePackages.db')
                            cur = conn.cursor()
                            cur.execute(f'''SELECT * FROM breakablePackages WHERE num = {package_key[0]} ''')
                            package = cur.fetchone()
                            conn = sq.connect("breakablePackages.db")
                            cur = conn.cursor()
                            cur.execute(f'''DELETE from breakablePackages WHERE num = {package_key[0]}''')
                            conn.commit()
                            conn.close()
                            conn = sq.connect('waybill.db')
                            cur = conn.cursor()
                            cur.execute('''CREATE TABLE IF NOT EXISTS Packages (package_num int PRIMARY KEY ,  weight real ,destinaton text , beginning text)''')
                            cur.execute(f'''INSERT OR IGNORE INTO Packages VALUES ({package[0]},{package[1]},'{package[2]}','{package[3]}')''')     
                            conn.commit()
                            conn.close()
                            
            conn = sq.connect("containerCar_Container.db")
            cur = conn.cursor()
            cur.execute(f'''DELETE from containerCar_Container WHERE containerCar_num = {car_num}''')
            conn.commit()
            conn.close() 
###########################
    conn = sq.connect("waybill.db")
    cur = conn.cursor()
    print("cars with room\nnumber - max weight - max packages - current number of packages - current weight - property  ")
    for row in cur.execute('''SELECT * FROM carWithRoom '''):
        print(row)
    
    print("\npackages in car with room\npackage number - car with room number")
    for row in cur.execute('''SELECT * FROM Car_Packages '''):
        print(row)   
    
    print("\ncontainer cars\nnumber - max weight - max container - current number of containers in car - current weight - property") 
    for row in cur.execute('''SELECT * FROM containerCar'''):
        print(row)
        
    print("\ncontainer in container car\ncontainer number - container car number - type container")
    for row in cur.execute('''container_incontainerCar'''):
        print(row)
        
    print("\ncontainers\nnumber - max weight - max package - current number of packages - current weight - type container - property")
    for row in cur.execute('''SELECT * FROM Container'''):
        print(row)
           
    print("\npackage in container\npackage number - container number - type package")
    for row in cur.execute('''SELECT * FROM packages_inContainer'''):
        print(row)     
    
    print("\npackages\npackage number - weight - destination - beginning") 
    for row in cur.execute('''SELECT * FROM Packages'''):
        print(row)
             
                        
#adders need rework  and remover

# print all the barname

# x9 = Container(6,900,70)
# x5 = Package(10,6,"hmd","tehran")
# x1 = breakablePackage(1,6,"hmd","tehran")
# x2 = coldPackage(1,3,"azar","canada",0)
# x3 = Package(4,9,"america","turkey")
# x10 = carWithRoom(9,900,300,)
# x11 = carWithRoom(12,1000,546)
# x12 = containerCar(6,9000,5,)
# x6 = freezerContainer(1,100,30,5,)
# x7 = breakableContainer(2,1000,50,70,)
# x45 = breakableContainer(98,1800,600,100)
# x78 = Package(98,15,"nyc","vienna")
# x96 = Package(65,12,"a","b")
# x94 = Package(62,65,'f','z')
# x41 = Package(166,79,'d','4')
# x58 = breakableContainer(8,456,10,50)
# x9 = containerCar(98,1512,5,)
# x126 = Container(101,800,80)
# x4= containerCar(53,2000,20,)
#########################################################################






# export_waybill()

# x1 = Package(5,10,'a','b')
# x2 = Container(5,1000,1000,)
# x3 = containerCar(5,1500,5,)

# addPackageToCantainer(5)
# addContainertoCar(5)

# conn = sq.connect('Car_Packages.db')
# cur = conn.cursor()
# cur.execute('''DELETE FROM Car_Packages WHERE num_package = 5''')
# conn.commit()
# conn.close()

# x1 = Package(40,40,'z','a')
# x2 = carWithRoom(40,500,9,)
# addPackageTocarWithRoom(40)