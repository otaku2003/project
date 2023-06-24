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
        for num in (f'{num}'): 
            cur.execute(f"SELECT {num} FROM coldPackages WHERE num = ?", (num,))
            data=cur.fetchone()
        if data is not None:
            print("this number exists in coldpackages")
    
            
        conn = sq.connect("breakablePackages.db")
        cur = conn.cursor()
        for num in (f'{num}'): 
            cur.execute(f"SELECT {num} FROM breakablePackages WHERE num = ?", (num,))
            data=cur.fetchone()
        if data is not None:
            print("this number exists in  breakable packages")
            
            
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
        cur.execute(f'''DELETE from Packages WHERE num = {num}''')
        conn.commit()
        conn.close()


   
    
class coldPackage:
    def __init__(self,num,weight,destination,beginning,min_temperature,property = ""):
        conn = sq.connect("Packages.db")
        cur = conn.cursor()
        for num in (f'{num}'): 
            cur.execute(f"SELECT {num} FROM Packages WHERE num = ?", (num,))
            data=cur.fetchone()
        if data is not None:
            print("this number exists in packages")
            
        conn = sq.connect("breakablePackages.db")
        cur = conn.cursor()
        for num in (f'{num}'): 
            cur.execute(f"SELECT {num} FROM breakablePackages WHERE num = ?", (num,))
            data=cur.fetchone()
        if data is not None:
            print("this number exists in breakable packages")
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
            conn = sq.connect("coldPackages.db")
            cur = conn.cursor()
            for num in (f'{num}'): 
                cur.execute(f"SELECT {num} FROM coldPackages WHERE num = ?", (num,))
                data=cur.fetchone()
            if data is not None:
                print("this number exists in cold packages")

            conn = sq.connect("Packages.db")
            cur = conn.cursor()
            for num in (f'{num}'): 
                cur.execute(f"SELECT {num} FROM Packages WHERE num = ?", (num,))
                data=cur.fetchone()
            if data is not None:
                print("this number exists in  packages") 

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
        conn = sq.connect("freezerContainer.db")
        cur = conn.cursor()
        for num in (f'{num}'): 
            cur.execute(f"SELECT {num} FROM freezerContainer WHERE num = ?", (num,))
            data=cur.fetchone()
        if data is not None:
            print("this number exists in freezer containers")
            
        conn = sq.connect("breakableContainer.db")
        cur = conn.cursor()
        for num in (f'{num}'): 
            cur.execute(f"SELECT {num} FROM breakableContainer WHERE num = ?", (num,))
            data=cur.fetchone()
        if data is not None:
            print("this number exists in breakable Container")
        else:
            conn = sq.connect("Container.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS Container (num int PRIMARY KEY, max_weight real, max_package int,number of packages int,weight real,property text)''')
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
        conn = sq.connect("Container.db")
        cur = conn.cursor()
        for num in (f'{num}'): 
            cur.execute(f"SELECT {num} FROM Container WHERE num = ?", (num,))
            data=cur.fetchone()
        if data is not None:
            print("this number exists in Container")
            
        conn = sq.connect("breakableContainer.db")
        cur = conn.cursor()
        for num in (f'{num}'): 
            cur.execute(f"SELECT {num} FROM breakableContainer WHERE num = ?", (num,))
            data=cur.fetchone()
        if data is not None:
            print("this number exists in breakable Containers")
        else:
            conn = sq.connect("freezerContainer.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS freezerContainer (num int PRIMARY KEY, max_weight real, max_packages int,min_temp_produced_by_container int,number_of_packages int,weight real,property text)''')
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
        conn = sq.connect("Container.db")
        cur = conn.cursor()
        for num in (f'{num}'): 
            cur.execute(f"SELECT {num} FROM Container WHERE num = ?", (num,))
            data=cur.fetchone()
        if data is not None:
            print("this number exists in Container")
            
        conn = sq.connect("freezerContainer.db")
        cur = conn.cursor()
        for num in (f'{num}'): 
            cur.execute(f"SELECT {num} FROM freezerContainer WHERE num = ?", (num,))
            data=cur.fetchone()
        if data is not None:
            print("this number exists in freezer container")
            
        else:
            conn = sq.connect("breakableContainer.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS breakableContainer (num int PRIMARY KEY, max_weight real, max_packages int,max_speed_of_car int,number_of_packages int,weight real,property text)''')
            cur.execute(f'''INSERT OR IGNORE INTO breakableContainer VALUES ({num},{max_weight},{max_package},{max_speed_of_car},{number_of_packages},{weight},'{property}')''')
            conn.commit()
            conn.close()

    def editbreakableContainer(self,num,max_weight = "",max_package = "",max_speed_of_car = '',property = ''):
        conn = sq.connect("breakableContainer.db")
        cur = conn.cursor()
        if max_weight != "":
            cur.execute(f'''UPDATE breakableContainer SET max_weight={max_weight} WHERE num = {num}''') 
            
        if max_package != "":
            cur.execute(f'''UPDATE breakableContainer SET max_package='{max_package}' WHERE num = {num}''')

        if property != "":
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
    
    
    
        
        
class carWithRoom():
    def __init__(self,num,max_weight_tolerable,max_number_tolerable,number_of_packages = 0,weight = 0,property = ''):
        conn = sq.connect("containerCar.db")
        cur = conn.cursor()
        for num in (f'{num}'): 
            cur.execute(f"SELECT {num} FROM containerCar WHERE num = ?", (num,))
            data=cur.fetchone()
        if data is not None:
            print("this number exists in container Cars")
        else:
            conn = sq.connect("carWithRoom.db")
            cur = conn.cursor()                                                                                         
            cur.execute('''CREATE TABLE IF NOT EXISTS carWithRoom (num int PRIMARY KEY, max_weight_tolerable real,max_number_tolerable int,number_of_packages int,weight,property text)''')
            cur.execute(f'''INSERT OR IGNORE INTO carWithRoom VALUES ({num},{max_weight_tolerable},{max_number_tolerable},{max_number_tolerable},{number_of_packages},{weight},'{property}')''')
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
        
        
class containerCar():##this
    def __init__(self,num,max_weight_tolerable,max_container_can_be_connected,property = ''):
        conn = sq.connect("carWithRoom.db")
        cur = conn.cursor()
        for num in (f'{num}'): 
            cur.execute(f"SELECT {num} FROM carWithRoom WHERE num = ?", (num,))
            data=cur.fetchone()
        if data is not None:
            print("this number exists in cars with room")
        else:
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


def addPackageToCantainer(container_num):##this 
    conn = sq.connect("Container.db")
    cur = conn.cursor()
    for num in (f'{num}'): 
        cur.execute(f"SELECT {num} FROM Container WHERE num = ?", (num,))
        data=cur.fetchone()
    if data is not None:
        conn = sq.connect("Container.db")
        cur = conn.cursor()
        cur.execute(f'''SELECT number FROM Container WHERE num = {container_num}''')
        for row in cur:
            packages_number_in_container = row
        cur.execute(f'''SELECT max_package FROM Container WHERE num = {container_num}''')
        for row in cur:
            max_package = row
        if(packages_number_in_container>= max_package):
            print("The capacity of the number of containers is complete ")
        else:
            cur.execute(f'''SELECT weight FROM Container WHERE num = {container_num}''')
            for row in cur:
                Container_weight = row
                
            cur.execute(f'''SELECT max_weight FROM Container WHERE num = {container_num}''')
            for row in cur:
                max_container_weight = row
            if(Container_weight>=max_container_weight):
                print("The weight capacity of the container is complete")
            else:
                conn = sq.connect('Packages.db')
                cur = conn.cursor()
                print("normal packages\nnumber - weight - destination - beginning") 
                for row in cur.execute('''SELECT * FROM Packages '''):
                    print(row)

                package_num = int(input("Enter package number : "))

                conn = sq.connect("Packages.db")##here1
                cur = conn.cursor()
                cur.execute(f'''SELECT weight FROM Packages WHERE num = {package_num} ''')
                for row in cur:
                    package_weight = row

                conn = sq.connect("Container.db")
                cur = conn.cursor()   
                            





                conn = sq.connect("Container_Package.db")
                cur= conn.cursor()

                cur.execute('''CREATE TABLE IF NOT EXISTS Container_Package (num_package int PRIMARY KEY, num_container int , type_package txt , type_container txt)''')
                cur.execute(f'''INSERT OR IGNORE INTO Container_Package VALUES ({package_num},{container_num},"normal","normal")''')
                conn.commit()
                conn.close()


    
    #############################
    
    conn = sq.connect("freezerContainer.db")
    cur = conn.cursor()
    for num in (f'{num}'): 
        cur.execute(f"SELECT {num} FROM freezerContainer WHERE num = ?", (num,))
        data=cur.fetchone()
    if data is not None:
        
        conn = sq.connect('coldPackages.db')
        cur = conn.cursor()
        print("cold packages\n number - weight - destination - beginning - minimum tempreture - property") 
        for row in cur.execute('''SELECT * FROM coldPackages '''):
            print(row) 
            
        package_num = int(input("Enter package number : "))
        conn = sq.connect("Container_Package.db")
        cur= conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Container_Package (num_package int PRIMARY KEY, num_container int  , type_package txt , type_container txt)''')
        cur.execute(f'''INSERT OR IGNORE INTO Container_Package VALUES ({package_num},{container_num},"cold","cold")''')
        conn.commit()
        conn.close()
    
    ######################################
    
    conn = sq.connect("breakableContainer.db")
    cur = conn.cursor()
    for num in (f'{num}'): 
        cur.execute(f"SELECT {num} FROM breakableContainer WHERE num = ?", (num,))
        data=cur.fetchone()
    if data is not None:
        
        conn = sq.connect('breakablePackages.db')
        cur = conn.cursor()
        print("breakable packages\n number - weight - destination - beginning - property")
        for row in cur.execute('''SELECT * FROM breakablePackages '''):
            print(row)
            
        package_num = int(input("Enter package number : "))
        conn = sq.connect("Container_Package.db")
        cur= conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Container_Package (num_package int PRIMARY KEY, num_container int  , type_package txt , type_container txt)''')
        cur.execute(f'''INSERT OR IGNORE INTO Container_Package VALUES ({package_num},{container_num},"breakable","breakable")''')
        conn.commit()
        conn.close()


x9 = Container(6,900,70)
# x5 = Package(1,6,"hmd","tehran")
# x1 = breakablePackage(1,6,"hmd","tehran")
# x2 = coldPackage(1,3,"azar","canada",0)
# x3 = Package(4,9,"america","turkey")

# x6 = freezerContainer(1,5,30,5,)
# x7 = breakableContainer(2,1000,50,70)
#########################################################################
# conn = sq.connect("Packages.db")
# cur = conn.cursor()
# cur.execute('''SELECT weight FROM Packages WHERE num = 9 ''')
# for row in cur:
    
    
#     print(row)