import sqlite3 as sq
import sys


def login():
    user = input("Enter username : ")
    password = input("Enter your password : ")
    if user == '1234' and password == '1234':
        return True
    else:
        return False


class Package:
    def __init__(self, num, weight, destination, beginning):

        conn = sq.connect("Packages.db")
        cur = conn.cursor()
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS Packages (num int PRIMARY KEY , weight real, destination text, beginning text)''')
        cur.execute(f'SELECT 1 FROM Packages WHERE num={num} ')
        conn.commit()
        data = cur.fetchone()
        if data is not None:
            print('this number exists in Packages')

        conn = sq.connect("coldPackages.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS coldPackages (num int PRIMARY KEY , weight real, destination text, beginning text,min_temperature int,property text )''')
        cur.execute(f'SELECT 1 FROM coldPackages WHERE num={num} ')
        conn.commit()
        data = cur.fetchone()
        if data is not None:
            print('this number exists in coldpackages')

        conn = sq.connect("breakablePackages.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS breakablePackages (num int PRIMARY KEY, weight real, destination text, beginning text , property text)''')
        cur.execute(f'SELECT 1 FROM breakablePackages WHERE num={num} ')
        conn.commit()
        data = cur.fetchone()
        if data is not None:
            print("this number exists in  breakable packages")

        else:
            conn = sq.connect("Packages.db")
            cur = conn.cursor()
            cur.execute(
                '''CREATE TABLE IF NOT EXISTS Packages (num int PRIMARY KEY , weight real, destination text, beginning text)''')
            cur.execute(
                f'''INSERT OR IGNORE INTO Packages VALUES ({num},{weight},'{destination}','{beginning}')''')
            conn.commit()
            conn.close()


class coldPackage:
    def __init__(self, num, weight, destination, beginning, min_temperature, property=""):

        conn = sq.connect("coldPackages.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS coldPackages (num int PRIMARY KEY, weight real, destination text, beginning text,min_temperature int,property text )''')
        cur.execute(f'SELECT 1 FROM coldPackages WHERE num={num} ')
        conn.commit()
        data = cur.fetchone()
        if data is not None:
            print('this number exists in coldpackages')

        conn = sq.connect("Packages.db")
        cur = conn.cursor()
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS Packages (num int PRIMARY KEY , weight real, destination text, beginning text)''')
        cur.execute(f'SELECT 1 FROM Packages WHERE num={num} ')
        conn.commit()
        data = cur.fetchone()
        if data is not None:
            print("this number exists in packages")

        conn = sq.connect("breakablePackages.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS breakablePackages (num int PRIMARY KEY, weight real, destination text, beginning text , property text)''')
        cur.execute(f'SELECT 1 FROM breakablePackages WHERE num={num} ')
        conn.commit()
        data = cur.fetchone()
        if data is not None:
            print("this number exists in breakable packages")

        else:
            conn = sq.connect("coldPackages.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS coldPackages (num int PRIMARY KEY AUTOINCREMENT, weight real, destination text, beginning text,min_temperature int,property text )''')
            cur.execute(
                f'''INSERT OR IGNORE INTO coldPackages VALUES ({num}, {weight}, '{destination}', '{beginning}',{min_temperature},'{property}' )''')
            conn.commit()
            conn.close()


class breakablePackage():
    def __init__(self, num, weight, destination, beginning, property=""):

        conn = sq.connect("breakablePackages.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS breakablePackages (num int PRIMARY KEY, weight real, destination text, beginning text , property text)''')
        cur.execute(f'SELECT 1 FROM breakablePackages WHERE num={num} ')
        conn.commit()
        data = cur.fetchone()
        if data is not None:
            print("this number exists in breakable packages")

        conn = sq.connect("coldPackages.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS coldPackages (num int PRIMARY KEY , weight real, destination text, beginning text,min_temperature int,property text )''')
        cur.execute(f'SELECT 1 FROM coldPackages WHERE num={num} ')
        conn.commit()
        data = cur.fetchone()
        if data is not None:
            print("this number exists in cold packages")

        conn = sq.connect("Packages.db")
        cur = conn.cursor()
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS Packages (num int PRIMARY KEY , weight real, destination text, beginning text)''')
        cur.execute(f'SELECT 1 FROM Packages WHERE num={num} ')
        conn.commit()
        data = cur.fetchone()
        if data is not None:
            print("this number exists in  packages")

        else:
            conn = sq.connect("breakablePackages.db")
            cur = conn.cursor()
            cur.execute(
                '''CREATE TABLE IF NOT EXISTS breakablePackages (num int PRIMARY KEY, weight real, destination text, beginning text , property text)''')
            cur.execute(
                f'''INSERT OR IGNORE INTO breakablePackages VALUES ({num},{weight},'{destination}','{beginning}','{property}')''')
            conn.commit()
            conn.close()


def packageRemover(num):
    conn = sq.connect("Packages.db")
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM Packages WHERE num={num} ')
    data = cur.fetchone()
    if data is not None:

        conn = sq.connect("Packages.db")
        cur = conn.cursor()
        cur.execute(f'''SELECT weight FROM Packages WHERE num = {num} ''')
        package_weight = cur.fetchone()
        cur.execute(f'''DELETE FROM Packages WHERE num = {num}''')
        conn.commit()
        conn.close()

        conn = sq.connect("Container_Packages.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
        cur.execute(
            f'''SELECT num_Container FROM Container_Packages WHERE num_package = {num}''')
        conn.commit()
        container_num = cur.fetchone()
        if container_num is not None:

            conn = sq.connect("Container.db")
            cur = conn.cursor()
            cur.execute(
                '''CREATE TABLE IF NOT EXISTS Container (num int PRIMARY KEY, max_weight real, max_package int,number_of_packages int,weight real,property text)''')
            cur.execute(
                f'''SELECT weight FROM Contaienr WHERE num = {container_num[0]} ''')
            conn.commit()
            container_weight = cur.fetchone()
            conn.close()

            conn = sq.connect("Container.db")
            cur = conn.cursor()
            cur.execute(
                f'''UPDATE Container SET weight = {container_weight[0]- package_weight[0]}''')
            conn.commit()
            conn.close()

            conn = sq.connect("Container_Packages.db")
            cur = conn.cursor()
            cur.execute(
                f'''DELETE FROM Container_Packages WHERE num_package = {num}''')
            conn.commit()
            conn.close()
            print("package deleted")

        conn = sq.connect("Car_Packages.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Car_Packages (num_package int PRIMARY KEY , num_carWithRoom int, type_Package text, type_carWithRoom text)''')
        cur.execute(
            f'''SELECT num_carWithRoom FROM Car_Packages WHERE num_package = {num} ''')
        carwithroom_num = cur.fetchone()
        conn.commit()
        if carwithroom_num is not None:

            conn = sq.connect("carWithRoom.db")
            cur = conn.cursor()
            cur.execute(
                '''CREATE TABLE IF NOT EXISTS carWithRoom (num int PRIMARY KEY, max_weight real,max_package int,number_of_packages int,weight real,property text)''')
            cur.execute(
                f'''SELECT weight FROM carWithRoom WHERE num = {carwithroom_num[0]} ''')
            carwithroom_weight = cur.fetchone()
            conn.commit()
            conn.close()

            conn = sq.connect("carWithRoom.db")
            cur = conn.cursor()
            cur.execute(
                f'''UPDATE carWithRoom SET weight = {carwithroom_weight[0]- package_weight[0]}''')
            conn.commit()
            conn.close()

            conn = sq.connect("Car_Packages.db")
            cur = conn.cursor()
            cur.execute(
                f'''DELETE FROM Car_Packages WHERE num_packages = {num}''')
            conn.commit()
            conn.close()
            print("package deleted")

    conn = sq.connect("coldPackages.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS coldPackages (num int PRIMARY KEY , weight real, destination text, beginning text,min_temperature int,property text )''')
    cur.execute(f'SELECT * FROM coldPackages WHERE num={num} ')
    data = cur.fetchone()
    if data is not None:
        conn = sq.connect("coldPackages.db")
        cur = conn.cursor()
        cur.execute(f'''SELECT weight FROM coldPackages WHERE num = {num} ''')
        package_weight = cur.fetchone()
        cur.execute(f'''DELETE FROM coldPackages WHERE num = {num}''')
        conn.commit()
        conn.close()

        conn = sq.connect("Container_Packages.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
        cur.execute(
            f'''SELECT num_Container FROM Container_Packages WHERE num_package = {num}''')
        conn.commit()
        container_num = cur.fetchone()

        conn = sq.connect("freezerContainer.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS freezerContainer (num int PRIMARY KEY, max_weight real, max_package int,min_temp_produced_by_container int,number_of_packages int,weight real,property text)''')
        cur.execute(
            f'''SELECT weight FROM freezerContaienr WHERE num = {container_num[0]} ''')
        conn.commit()
        container_weight = cur.fetchone()

        conn = sq.connect("freezerContainer.db")
        cur = conn.cursor()
        cur.execute(
            f'''UPDATE freezerContainer SET weight = {container_weight[0]- package_weight[0]}''')
        conn.commit()
        conn.close()

        conn = sq.connect("Container_Packages.db")
        cur = conn.cursor()
        cur.execute(
            f'''DELETE FROM Container_Packages WHERE num_package = {num}''')
        conn.commit()
        conn.close()
        print("package deleted")

    conn = sq.connect("breakablePackages.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS breakablePackages (num int PRIMARY KEY, weight real, destination text, beginning text , property text)''')
    cur.execute(f'SELECT * FROM breakablePackages WHERE num={num} ')
    data = cur.fetchone()
    if data is not None:
        conn = sq.connect("breakablePackages.db")
        cur = conn.cursor()
        cur.execute(
            f'''SELECT weight FROM breakablePackages WHERE num = {num} ''')
        package_weight = cur.fetchone()
        cur.execute(f'''DELETE FROM breakablePackages WHERE num = {num}''')
        conn.commit()
        conn.close()

        conn = sq.connect("Container_Packages.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
        cur.execute(
            f'''SELECT num_Container FROM Container_Packages WHERE num_package = {num}''')
        conn.commit()
        container_num = cur.fetchone()

        conn = sq.connect("breakableContainer.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS breakableContainer (num int PRIMARY KEY, max_weight real, max_package int,max_speed_of_car int,number_of_packages int,weight real,property text)''')
        cur.execute(
            f'''SELECT weight FROM breakableContaienr WHERE num = {container_num[0]} ''')
        container_weight = cur.fetchone()

        conn = sq.connect("breakableContainer.db")
        cur = conn.cursor()
        cur.execute(
            f'''UPDATE breakableContainer SET weight = {container_weight[0]- package_weight[0]}''')
        conn.commit()
        conn.close()

        conn = sq.connect("Container_Packages.db")
        cur = conn.cursor()
        cur.execute(
            f'''DELETE FROM Container_Packages WHERE num_package = {num}''')
        conn.commit()
        conn.close()
        print("package deleted")


def packageEditor(num):
    conn = sq.connect("Packages.db")
    cur = conn.cursor()
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS Packages (num int PRIMARY KEY , weight real, destination text, beginning text)''')
    cur.execute(f'''SELECT * FROM Packages WHERE num = {num}''')
    data = cur.fetchone()
    if data is not None:
        weight, destination, beginning = input(
            "Enter weight and destination and beginnig seperated by space (if you dont want change a value place 0 instead of that )  : ").split()

        conn = sq.connect("Packages.db")
        cur = conn.cursor()
        if weight != "0":
            conn = sq.connect("Packages.db")
            cur = conn.cursor()
            cur.execute(f'''SELECT weight FROM Packages WHERE num = {num}''')
            package_first_weight = cur.fetchone()

            weight = float(weight)
            cur.execute(
                f'''UPDATE Packages SET weight={weight} WHERE num = {num}''')
            conn.commit()
            conn.close()

            conn = sq.connect("Container_Packages.db")
            cur = conn.cursor()
            cur.execute(
                '''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
            cur.execute(
                f'''SELECT num_Container FROM Container_Packages WHERE num_package = {num}''')
            conn.commit()
            container_num = cur.fetchone()
            if container_num is not None:

                conn = sq.connect('Container.db')
                cur = conn.cursor()
                cur.execute(
                    f'''SELECT weight FROM Container WHERE num = {container_num[0]}''')
                container_weight = cur.fetchone()

                cur.execute(
                    f'''UPDATE Container SET weight = {weight + container_weight[0] - package_first_weight[0]} WHERE num = {container_num[0]}''')
                conn.commit()
                conn.close()

                conn = sq.connect("containerCar_Container.db")
                cur = conn.cursor()
                cur.execute(
                    '''CREATE TABLE IF NOT EXISTS containerCar_Container (Container_num int PRIMARY KEY,containerCar_num int ,type_container text)''')
                cur.execute(
                    f'''SELECT containerCar_num FROM containerCar_Container WHERE Container_num = {container_num[0]}''')
                conn.commit()
                containercar_num = cur.fetchone()

                if containercar_num is not None:
                    conn = sq.connect("containerCar.db")
                    cur = conn.cursor()
                    cur.execute(
                        '''CREATE TABLE IF NOT EXISTS containerCar (num int PRIMARY KEY, max_weight real,max_container_can_be_connected int,number_of_containers int,weight real,property text)''')
                    cur.execute(
                        f'''SELECT weight FROM containerCar WHERE num = {containercar_num[0]} ''')
                    conn.commit()
                    containercar_weight = cur.fetchone()

                    cur.execute(
                        f'''UPDATE containerCar SET weight = {weight + containercar_weight[0] - package_first_weight[0]}''')
                    conn.commit()
                    conn.close()

        conn = sq.connect("Packages.db")
        cur = conn.cursor()
        if destination != "0":
            cur.execute(
                f'''UPDATE Packages SET destination='{destination}' WHERE num = {num}''')

        if beginning != "0":
            cur.execute(
                f'''UPDATE Packages SET beginning='{beginning}' WHERE num = {num}''')
        conn.commit()
        conn.close()

    conn = sq.connect("coldPackages.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS coldPackages (num int PRIMARY KEY , weight real, destination text, beginning text,min_temperature int,property text )''')
    cur.execute(f'''SELECT * FROM coldPackages WHERE num = {num}''')
    data = cur.fetchone()
    if data is not None:
        weight, destination, beginning, min_temp, property = input(
            "Enter weight and destination and beginnig and min_temprature and property seperated by space (if you dont want change a value place 0 instead of that )  : ").split()

        if weight != "0":
            weight = float(weight)
            conn = sq.connect("coldPackages.db")
            cur = conn.cursor()
            cur.execute(
                f'''SELECT weight FROM coldPackages WHERE num = {num}''')
            package_first_weight = cur.fetchone()

            conn = sq.connect("coldPackages.db")
            cur = conn.cursor()
            cur.execute(
                f'''UPDATE coldPackages SET weight={weight} WHERE num = {num}''')
            conn.commit()
            conn.close()

            conn = sq.connect("Container_Packages.db")
            cur = conn.cursor()
            cur.execute(
                '''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
            cur.execute(
                f'''SELECT num_Container FROM Container_Packages WHERE num_package = {num}''')
            conn.commit()
            container_num = cur.fetchone()
            if container_num is not None:

                conn = sq.connect('freezerContainer.db')
                cur = conn.cursor()
                cur.execute('''CREATE TABLE IF NOT EXISTS freezerContainer (num int PRIMARY KEY, max_weight real, max_package int,min_temp_produced_by_container int,number_of_packages int,weight real,property text)''')
                cur.execute(
                    f'''SELECT weight FROM freezerContainer WHERE num = {container_num[0]}''')
                conn.commit()
                container_weight = cur.fetchone()

                cur.execute(
                    f'''UPDATE freezerContainer SET weight = {weight + container_weight[0] - package_first_weight[0]} WHERE num = {container_num[0]}''')
                conn.commit()
                conn.close()

                conn = sq.connect("containerCar_Container.db")
                cur = conn.cursor()
                cur.execute(
                    '''CREATE TABLE IF NOT EXISTS containerCar_Container (Container_num int PRIMARY KEY,containerCar_num int ,type_container text)''')
                cur.execute(
                    f'''SELECT containerCar_num FROM containerCar_Container WHERE Container_num = {container_num[0]}''')
                conn.commit()
                containercar_num = cur.fetchone()

                if containercar_num is not None:
                    conn = sq.connect("containerCar.db")
                    cur = conn.cursor()
                    cur.execute(
                        '''CREATE TABLE IF NOT EXISTS containerCar (num int PRIMARY KEY, max_weight real,max_container_can_be_connected int,number_of_containers int,weight real,property text)''')
                    cur.execute(
                        f'''SELECT weight FROM containerCar WHERE num = {containercar_num[0]} ''')
                    conn.commit()
                    containercar_weight = cur.fetchone()

                    cur.execute(
                        f'''UPDATE containerCar SET weight = {weight + containercar_weight[0] - package_first_weight[0]}''')
                    conn.commit()
                    conn.close()

        if destination != "0":
            cur.execute(
                f'''UPDATE coldPackages SET destination='{destination}' WHERE num = {num}''')

        if beginning != "0":
            cur.execute(
                f'''UPDATE coldPackages SET beginning='{beginning}' WHERE num = {num}''')

        if min_temp != "0":
            min_temp = float(min_temp)
            cur.execute(
                f'''UPDATE coldPackages SET min_temperature={min_temp} WHERE num = {num}''')

        if property != "0":
            cur.execute(
                f'''UPDATE coldPackages SET property='{property}' WHERE num = {num}''')
        conn.commit()
        conn.close()

    conn = sq.connect("breakablePackages.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS breakablePackages (num int PRIMARY KEY, weight real, destination text, beginning text , property text)''')
    cur.execute(f'''SELECT * FROM breakablePackages WHERE num = {num}''')
    data = cur.fetchone()
    if data is not None:

        weight, destination, beginning, property = input(
            "Enter weight and destination and beginnig and property seperated by space (if you dont want change a value place 0 instead of that )  : ").split()

        if weight != "0":
            weight = float(weight)

            conn = sq.connect("breakablePackages.db")
            cur = conn.cursor()
            cur.execute(
                f'''SELECT weight FROM breakablePackages WHERE num = {num}''')
            package_first_weight = cur.fetchone()

            cur.execute(
                f'''UPDATE breakablePackages SET weight={weight} WHERE num = {num}''')
            conn.commit()
            conn.close()

            conn = sq.connect("Container_Packages.db")
            cur = conn.cursor()
            cur.execute(
                '''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
            cur.execute(
                f'''SELECT num_Container FROM Container_Packages WHERE num_package = {num}''')
            conn.commit()
            container_num = cur.fetchone()
            if container_num is not None:

                conn = sq.connect('breakablContainer.db')
                cur = conn.cursor()
                cur.execute('''CREATE TABLE IF NOT EXISTS breakableContainer (num int PRIMARY KEY, max_weight real, max_package int,max_speed_of_car int,number_of_packages int,weight real,property text)''')
                cur.execute(
                    f'''SELECT weight FROM breakableContainer WHERE num = {container_num[0]}''')
                conn.commit()
                container_weight = cur.fetchone()

                cur.execute(
                    f'''UPDATE breakableContainer SET weight = {weight + container_weight[0] - package_first_weight[0]}''')
                conn.commit()
                conn.close()

                conn = sq.connect("containerCar_Container.db")
                cur = conn.cursor()
                cur.execute(
                    '''CREATE TABLE IF NOT EXISTS containerCar_Container (Container_num int PRIMARY KEY,containerCar_num int ,type_container text)''')
                cur.execute(
                    f'''SELECT containerCar_num FROM containerCar_Container WHERE Container_num = {container_num[0]}''')
                conn.commit()
                containercar_num = cur.fetchone()
                if containercar_num is not None:
                    conn = sq.connect("containerCar.db")
                    cur = conn.cursor()
                    cur.execute(
                        '''CREATE TABLE IF NOT EXISTS containerCar (num int PRIMARY KEY, max_weight real,max_container_can_be_connected int,number_of_containers int,weight real,property text)''')
                    cur.execute(
                        f'''SELECT weight FROM containerCar WHERE num = {containercar_num[0]} ''')
                    conn.commit()
                    containercar_weight = cur.fetchone()

                    cur.execute(
                        f'''UPDATE containerCar SET weight = {weight + containercar_weight[0] - package_first_weight[0]}''')
                    conn.commit()
                    conn.close()

        if destination != "0":
            cur.execute(
                f'''UPDATE coldPackages SET destination='{destination}' WHERE num = {num}''')

        if beginning != "0":
            cur.execute(
                f'''UPDATE coldPackages SET beginning='{beginning}' WHERE num = {num}''')

        if property != "0":
            cur.execute(
                f'''UPDATE coldPackages SET property='{property}' WHERE num = {num}''')
        conn.commit()
        conn.close()


class Container():
    def __init__(self, num, max_weight, max_package, number_of_packages=0, weight=0, property=""):

        conn = sq.connect("Container.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Container (num int PRIMARY KEY, max_weight real, max_package int,number_of_packages int,weight real,property text)''')
        cur.execute(f'SELECT 1 FROM Container WHERE num={num} ')
        data = cur.fetchone()
        if data is not None:
            print("this number exists in Container")

        conn = sq.connect("freezerContainer.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS freezerContainer (num int PRIMARY KEY, max_weight real, max_package int,min_temp_produced_by_container int,number_of_packages int,weight real,property text)''')
        cur.execute(f'SELECT 1 FROM freezerContainer WHERE num={num} ')
        data = cur.fetchone()
        if data is not None:
            print("this number exists in freezer containers")

        conn = sq.connect("breakableContainer.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS breakableContainer (num int PRIMARY KEY, max_weight real, max_package int,max_speed_of_car int,number_of_packages int,weight real,property text)''')
        cur.execute(f'SELECT 1 FROM breakableContainer WHERE num={num} ')
        data = cur.fetchone()
        if data is not None:
            print("this number exists in breakable Container")

        else:
            conn = sq.connect("Container.db")
            cur = conn.cursor()
            cur.execute(
                '''CREATE TABLE IF NOT EXISTS Container (num int PRIMARY KEY, max_weight real, max_package int,number_of_packages int,weight real,property text)''')
            cur.execute(
                f'''INSERT OR IGNORE INTO Container VALUES ({num},{max_weight},{max_package},{number_of_packages},{weight},'{property}')''')
            conn.commit()
            conn.close()


class freezerContainer():
    def __init__(self, num, max_weight, max_package, min_temp_produced_by_container, number_of_packages=0, weight=0, property=""):

        conn = sq.connect("freezerContainer.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS freezerContainer (num int PRIMARY KEY, max_weight real, max_package int,min_temp_produced_by_container int,number_of_packages int,weight real,property text)''')
        cur.execute(f'SELECT 1 FROM freezerContainer WHERE num={num} ')
        data = cur.fetchone()
        if data is not None:
            print("this number exists in freezer containers")

        conn = sq.connect("Container.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Container (num int PRIMARY KEY, max_weight real, max_package int,number_of_packages int,weight real,property text)''')
        cur.execute(f'SELECT 1 FROM Container WHERE num={num} ')
        data = cur.fetchone()
        if data is not None:
            print("this number exists in Container")

        conn = sq.connect("breakableContainer.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS breakableContainer (num int PRIMARY KEY, max_weight real, max_package int,max_speed_of_car int,number_of_packages int,weight real,property text)''')
        cur.execute(f'SELECT 1 FROM breakableContainer WHERE num={num} ')
        data = cur.fetchone()
        if data is not None:
            print("this number exists in breakable Containers")

        else:
            conn = sq.connect("freezerContainer.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS freezerContainer (num int PRIMARY KEY, max_weight real, max_package int,min_temp_produced_by_container int,number_of_packages int,weight real,property text)''')
            cur.execute(
                f'''INSERT OR IGNORE INTO freezerContainer VALUES ({num},{max_weight},{max_package},{min_temp_produced_by_container},{number_of_packages},{weight},'{property}')''')
            conn.commit()
            conn.close()


class breakableContainer():
    def __init__(self, num, max_weight, max_package, max_speed_of_car, number_of_packages=0, weight=0, property=""):

        conn = sq.connect("breakableContainer.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS breakableContainer (num int PRIMARY KEY, max_weight real, max_package int,max_speed_of_car int,number_of_packages int,weight real,property text)''')
        cur.execute(f'SELECT 1 FROM breakableContainer WHERE num={num} ')
        data = cur.fetchone()
        if data is not None:
            print("this number exists in breakable Containers")

        conn = sq.connect("Container.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Container (num int PRIMARY KEY, max_weight real, max_package int,number_of_packages int,weight real,property text)''')
        cur.execute(f'SELECT 1 FROM Container WHERE num={num} ')
        data = cur.fetchone()
        if data is not None:
            print("this number exists in Container")

        conn = sq.connect("freezerContainer.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS freezerContainer (num int PRIMARY KEY, max_weight real, max_package int,min_temp_produced_by_container int,number_of_packages int,weight real,property text)''')
        cur.execute(f'SELECT 1 FROM freezerContainer WHERE num={num} ')
        data = cur.fetchone()
        if data is not None:
            print("this number exists in freezer container")

        else:
            conn = sq.connect("breakableContainer.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS breakableContainer (num int PRIMARY KEY, max_weight real, max_package int,max_speed_of_car int,number_of_packages int,weight real,property text)''')
            cur.execute(
                f'''INSERT OR IGNORE INTO breakableContainer VALUES ({num},{max_weight},{max_package},{max_speed_of_car},{number_of_packages},{weight},'{property}')''')
            conn.commit()
            conn.close()


def containerRemover(num):
    conn = sq.connect("Container.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Container (num int PRIMARY KEY, max_weight real, max_package int,number_of_packages int,weight real,property text)''')
    cur.execute(f'SELECT * FROM Container WHERE num={num} ')
    data = cur.fetchone()
    if data is not None:
        conn = sq.connect("Container.db")
        cur = conn.cursor()
        cur.execute(f'''SELECT weight FROM Container WHERE num = {num}''')
        container_weight = cur.fetchone()

        conn = sq.connect("containerCar_Container.db")
        cur = conn.cursor()
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS containerCar_Container (Container_num int PRIMARY KEY,containerCar_num int ,type_container text)''')
        cur.execute(
            f'''SELECT containerCar_num FROM containerCar_Container WHERE Container_num = {num}''')
        conn.commit()
        containercar_num = cur.fetchone()

        if containercar_num is not None:

            conn = sq.connect("containerCar.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS containerCar (num int PRIMARY KEY, max_weight real,max_container_can_be_connected int,number_of_containers int,weight real,property text)''')
            cur.execute(
                f'''SELECT weight FROM containerCar WHERE num = {containercar_num[0]} ''')
            conn.commit()
            containercar_weight = cur.fetchone()

            cur.execute(
                f'''UPDATE containerCar SET weight = {containercar_weight[0] - container_weight[0]} WHERE num = {containercar_num[0]}''')
            conn.commit()
            conn.close()

            conn = sq.connect("containerCar_Container.db")
            cur = conn.cursor()
            cur.execute(
                f'''DELETE FROM containerCar_Container WHERE Container_num = {num}''')
            conn.commit()
            conn.close()

        conn = sq.connect("Container.db")
        cur = conn.cursor()
        cur.execute(f'''DELETE from Container WHERE num = {num}''')
        conn.commit()
        conn.close()

        conn = sq.connect("Container_Packages.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
        cur.execute(
            f'''DELETE FROM Container_Packages WHERE num_Container = {num}''')
        conn.commit()
        conn.close()

    conn = sq.connect("freezerContainer.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS freezerContainer (num int PRIMARY KEY, max_weight real, max_package int,min_temp_produced_by_container int,number_of_packages int,weight real,property text)''')
    cur.execute(f'SELECT * FROM freezerContainer WHERE num={num} ')
    data = cur.fetchone()
    if data is not None:
        conn = sq.connect("freezerContainer.db")
        cur = conn.cursor()
        cur.execute(
            f'''SELECT weight FROM freezerContainer WHERE num = {num}''')
        container_weight = cur.fetchone()

        conn = sq.connect("containerCar_Container.db")
        cur = conn.cursor()
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS containerCar_Container (Container_num int PRIMARY KEY,containerCar_num int ,type_container text)''')
        cur.execute(
            f'''SELECT containerCar_num FROM containerCar_Container WHERE Container_num = {num}''')
        conn.commit()
        containercar_num = cur.fetchone()

        if containercar_num is not None:

            conn = sq.connect("containerCar.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS containerCar (num int PRIMARY KEY, max_weight real,max_container_can_be_connected int,number_of_containers int,weight real,property text)''')
            cur.execute(
                f'''SELECT weight FROM containerCar WHERE num = {containercar_num[0]} ''')
            conn.commit()
            containercar_weight = cur.fetchone()

            cur.execute(
                f'''UPDATE containerCar SET weight = {containercar_weight[0] - container_weight[0]} WHERE num = {containercar_num[0]}''')
            conn.commit()
            conn.close()

            conn = sq.connect("containerCar_Container.db")
            cur = conn.cursor()
            cur.execute(
                f'''DELETE FROM containerCar_Container WHERE Container_num = {num}''')
            conn.commit()
            conn.close()

        conn = sq.connect("freezerContainer.db")
        cur = conn.cursor()
        cur.execute(f'''DELETE from freezerContainer WHERE num = {num}''')
        conn.commit()
        conn.close()

        conn = sq.connect("Container_Packages.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
        cur.execute(
            f'''DELETE FROM Container_Packages WHERE num_Container = {num}''')
        conn.commit()
        conn.close()

    conn = sq.connect("breakableContainer.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS breakableContainer (num int PRIMARY KEY, max_weight real, max_package int,max_speed_of_car int,number_of_packages int,weight real,property text)''')
    cur.execute(f'SELECT * FROM breakableContainer WHERE num={num} ')
    data = cur.fetchone()
    if data is not None:

        conn = sq.connect("breakableContainer.db")
        cur = conn.cursor()
        cur.execute(
            f'''SELECT weight FROM breakableContainer WHERE num = {num}''')
        container_weight = cur.fetchone()

        conn = sq.connect("containerCar_Container.db")
        cur = conn.cursor()
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS containerCar_Container (Container_num int PRIMARY KEY,containerCar_num int ,type_container text)''')
        cur.execute(
            f'''SELECT containerCar_num FROM containerCar_Container WHERE Container_num = {num}''')
        conn.commit()
        containercar_num = cur.fetchone()

        if containercar_num is not None:

            conn = sq.connect("containerCar.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS containerCar (num int PRIMARY KEY, max_weight real,max_container_can_be_connected int,number_of_containers int,weight real,property text)''')
            cur.execute(
                f'''SELECT weight FROM containerCar WHERE num = {containercar_num[0]} ''')
            conn.commit()
            containercar_weight = cur.fetchone()

            cur.execute(
                f'''UPDATE containerCar SET weight = {containercar_weight[0] - container_weight[0]} WHERE num = {containercar_num[0]}''')
            conn.commit()
            conn.close()

            conn = sq.connect("containerCar_Container.db")
            cur = conn.cursor()
            cur.execute(
                f'''DELETE FROM containerCar_Container WHERE Container_num = {num}''')
            conn.commit()
            conn.close()

        conn = sq.connect("breakableContainer.db")
        cur = conn.cursor()
        cur.execute(f'''DELETE from breakableContainer WHERE num = {num}''')
        conn.commit()
        conn.close()

        conn = sq.connect("Container_Packages.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
        cur.execute(
            f'''DELETE FROM Container_Packages WHERE num_Container = {num}''')
        conn.commit()
        conn.close()


def containerEditor(num):
    conn = sq.connect("Container.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Container (num int PRIMARY KEY, max_weight real, max_package int,number_of_packages int,weight real,property text)''')
    cur.execute(f'''SELECT * FROM Container  WHERE num = {num}''')
    conn.commit()
    data = cur.fetchone()
    if data is not None:
        max_weight, max_package, property = input(
            "Enter max_weight and max_package and  property seperated by space (if you dont want change a value place 0 instead of that )  : ").split()

        if max_weight != '0':
            max_weight = float(max_weight)
            cur.execute(
                f'''UPDATE Container SET max_weight = {max_weight} WHERE num = {num}''')

        if max_package != "0":
            max_package = int(max_package)
            cur.execute(
                f'''UPDATE Continer SET max_package = {max_package} WHERE num = {num}''')

        if property != '0':
            cur.execute(
                f'''UPDATE Container SET proprty = '{property}' WHERE num = {num}''')

        conn.commit()
        conn.close()

    conn = sq.connect("freezerContainer.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS freezerContainer (num int PRIMARY KEY, max_weight real, max_package int,min_temp_produced_by_container int,number_of_packages int,weight real,property text)''')
    cur.execute(f'''SELECT * FROM freezerContainer WHERE num = {num}''')
    conn.commit()
    data = cur.fetchone()
    if data is not None:
        max_weight, max_package, min_temp, property = input(
            "Enter max_weight and max_package and min_temprature of container and property seperated by space (if you dont want change a value place 0 instead of that )  : ").split()
        if max_weight != '0':
            max_weight = float(max_weight)
            cur.execute(
                f'''UPDATE freezerContainer SET max_weight = {max_weight} WHERE num = {num}''')

        if max_package != '0':
            max_package = int(max_package)
            cur.execute(
                f'''UPDATE freezerContainer SET max_package = {max_package} WHERE num = {num}''')

        if min_temp != '0':
            min_temp = float(min_temp)
            cur.execute(
                f'''UPDATE freezerContainer SET min_temp_produced_by_container = {min_temp} WHERE num = {num}''')

        if property != '0':
            cur.execute(
                f'''UPDATE freezerContainer SET property = '{property}' WHERE num = {num}''')

        conn.commit()
        conn.close()

    conn = sq.connect("breakableContainer.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS breakableContainer (num int PRIMARY KEY, max_weight real, max_package int,max_speed_of_car int,number_of_packages int,weight real,property text)''')
    cur.execute(f'''SELECT * FROM breakableContainer WHERE num = {num}''')
    conn.commit()
    data = cur.fetchone()
    if data is not None:
        max_weight, max_package, max_speed, property = input(
            "Enter max_weight and max_package and max speed of container and property seperated by space (if you dont want change a value place 0 instead of that )  : ").split()
        if max_weight != '0':
            max_weight = float(max_weight)
            cur.execute(
                f'''UPDATE breakableContainer SET max_weight = {max_weight} WHERE num = {num}''')

        if max_package != '0':
            max_package = int(max_package)
            cur.execute(
                f'''UPDATE breakableContainer SET max_package = {max_package} WHERE num = {num}''')

        if max_speed != '0':
            max_speed = int(max_speed)
            cur.execute(
                f'''UPDATE breakableContainer SET max_speed_of_car = {max_speed} WHERE num = {num}''')

        if property != '0':
            cur.execute(
                f'''UPDATE breakableContainer SET property = '{property}' WHERE num = {num}''')

        conn.commit()
        conn.close()


class carWithRoom():
    def __init__(self, num, max_weight, max_package, number_of_packages=0, weight=0, property=''):

        conn = sq.connect("carWithRoom.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS carWithRoom (num int PRIMARY KEY, max_weight real,max_package int,number_of_packages int,weight real,property text)''')
        conn.commit()
        cur.execute(f'SELECT 1 FROM carWithRoom WHERE num={num} ')
        data = cur.fetchone()
        if data is not None:
            print("this number exists in cars with room")

        conn = sq.connect("containerCar.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS containerCar (num int PRIMARY KEY, max_weight real,max_container_can_be_connected int,number_of_containers int,weight real,property text)''')
        cur.execute(f'SELECT 1 FROM containerCar WHERE num={num} ')
        data = cur.fetchone()
        conn.commit()
        conn.close()
        if data is not None:
            print("this number exists in container Cars")

        else:
            conn = sq.connect("carWithRoom.db")
            cur = conn.cursor()
            cur.execute(
                '''CREATE TABLE IF NOT EXISTS carWithRoom (num int PRIMARY KEY, max_weight real,max_package int,number_of_packages int,weight real,property text)''')
            cur.execute(
                f'''INSERT OR IGNORE INTO carWithRoom VALUES ({num},{max_weight},{max_package},{number_of_packages},{weight},'{property}')''')
            conn.commit()
            conn.close()


class containerCar():
    def __init__(self, num, max_weight, max_container_can_be_connected, number_of_containers=0, weight=0, property=''):

        conn = sq.connect("containerCar.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS containerCar (num int PRIMARY KEY, max_weight real,max_container_can_be_connected int,number_of_containers int,weight real,property text)''')
        cur.execute(f'SELECT 1 FROM containerCar WHERE num={num} ')
        conn.commit()
        data = cur.fetchone()
        if data is not None:
            print("this number exists in container Cars")
        conn.close()

        conn = sq.connect("carWithRoom.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS carWithRoom (num int PRIMARY KEY, max_weight real,max_package int,number_of_packages int,weight real,property text)''')
        cur.execute(f'SELECT 1 FROM carWithRoom WHERE num={num} ')
        data = cur.fetchone()
        conn.commit()
        if data is not None:
            print("this number exists in cars with room")

        else:
            conn = sq.connect("containerCar.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS containerCar (num int PRIMARY KEY, max_weight real,max_container_can_be_connected int,number_of_containers int,weight real,property text)''')
            cur.execute(
                f'''INSERT OR IGNORE INTO containerCar VALUES ({num},{max_weight},{max_container_can_be_connected},{number_of_containers},{weight},'{property}')''')
            conn.commit()
            conn.close()


def carRemover(num):
    conn = sq.connect("carWithRoom.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS carWithRoom (num int PRIMARY KEY, max_weight real,max_package int,number_of_packages int,weight real,property text)''')
    cur.execute(f'SELECT * FROM carWithRoom WHERE num={num} ')
    conn.commit()
    data = cur.fetchone()
    if data is not None:
        conn = sq.connect("carWithRoom.db")
        cur = conn.cursor()
        cur.execute(f'''DELETE FROM carWithRoom WHERE num = {num}''')
        conn.commit()
        conn.close()

        conn = sq.connect("Car_Packages.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Car_Packages (num_package int PRIMARY KEY , num_carWithRoom int, type_Package text, type_carWithRoom text)''')
        cur.execute(
            f'''DELETE FROM Car_Packages WHERE num_carWithRoom = {num}''')
        conn.commit()
        conn.close()
        print("car deleted")

    conn = sq.connect("containerCar.db")
    cur = conn.cursor()
    cur.execute(f'''SELECT * FROM containerCar WHERE num = {num} ''')
    data = cur.fetchone()
    if data is not None:
        conn = sq.connect("containerCar.db")
        cur = conn.cursor()
        cur.execute(f'''DELETE FROM containerCar WHERE num = {num}''')
        conn.commit()
        conn.close()

        conn = sq.connect("containerCar_Container.db")
        cur = conn.cursor()
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS containerCar_Container (Container_num int PRIMARY KEY,containerCar_num int ,type_container text)''')
        cur.execute(
            f'''DELETE FROM containerCar_Container WHERE containerCar_num = {num}''')
        conn.commit()
        conn.close()
        print("car deleted")


def carEditor(num):
    conn = sq.connect("carWithRoom.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS carWithRoom (num int PRIMARY KEY, max_weight real,max_package int,number_of_packages int,weight real,property text)''')
    cur.execute(f'''SELECT * FROM carWithRoom WHERE num = {num}''')
    conn.commit()
    data = cur.fetchone()
    if data is not None:
        max_weight, max_package, property = input(
            "Enter max_weight and max_package and property seperated by space (if you dont want change a value place 0 instead of that )  : ").split()
        if max_weight != "0":
            max_weight = float(max_weight)
            cur.execute(
                f'''UPDATE carWithRoom SET max_weight = {max_weight} WHERE num = {num}''')

        if max_package != '0':
            max_package = int(max_package)
            cur.execute(
                f'''UPDATE carWithRoom SET max_package = {max_package} WHERE num = {num}''')

        if property != '0':
            cur.execute(
                f'''UPDATE carWithRoom SET property = '{property}' WHERE num = {num}''')
        conn.commit()
        conn.close()

    conn = sq.connect("containerCar.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS containerCar (num int PRIMARY KEY, max_weight real,max_container_can_be_connected int,number_of_containers int,weight real,property text)''')
    cur.execute(f'''SELECT * FROM containerCar WHERE num = {num}''')
    conn.commit()
    data = cur.fetchone()
    if data is not None:
        max_weight, max_container, property = input(
            "Enter max_weight and max_container and property seperated by space (if you dont want change a value place 0 instead of that )  : ").split()
        if max_weight != "0":
            max_weight = float(max_weight)
            cur.execute(
                f'''UPDATE containerCar SET max_weight = {max_weight} WHERE num = {num}''')

        if max_container != '0':
            max_container = int(max_container)
            cur.execute(
                f'''UPDATE containerCar SET max_container = {max_container} WHERE num = {num}''')

        if property != '0':
            cur.execute(
                f'''UPDATE containerCar SET property = '{property}' WHERE num = {num}''')
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

    conn.close()
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
    conn.close()


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
        cur.execute(
            f'''SELECT number_of_packages FROM carWithRoom WHERE num = {car_num}''')
        for row in cur:
            packages_number_in_car_with_room = row
        cur.execute(
            f'''SELECT max_package FROM carWithRoom WHERE num = {car_num}''')
        for row in cur:
            max_package = row
        if (packages_number_in_car_with_room[0] >= max_package[0]):
            print("The capacity of the number of car with room is complete ")

        else:
            cur.execute(
                f'''SELECT weight FROM carWithRoom WHERE num = {car_num}''')
            for row in cur:
                Car_weight = row

            conn = sq.connect("carWithRoom.db")
            cur = conn.cursor()

            cur.execute(
                f'''SELECT max_weight FROM carWithRoom WHERE num = {car_num}''')
            for row in cur:
                max_car_weight = row
            if (Car_weight[0] >= max_car_weight[0]):
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
                    cur.execute(
                        '''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
                    cur.execute(
                        f'SELECT 1 FROM Container_Packages WHERE num_package={package_num} ')
                    conn.commit()
                    data = cur.fetchone()
                    if data is not None:
                        print(
                            f"package {package_num} is already exist in a container")

                    else:

                        conn = sq.connect("Car_Packages.db")
                        cur = conn.cursor()
                        cur.execute(
                            '''CREATE TABLE IF NOT EXISTS Car_Packages (num_package int PRIMARY KEY , num_carWithRoom int, type_Package text, type_carWithRoom text)''')
                        cur.execute(
                            f'SELECT 1 FROM Car_Packages WHERE num_package={package_num} ')
                        data = cur.fetchone()
                        conn.commit()
                        if data is not None:
                            print(
                                f"package {package_num} is already exist in a car with room")

                        else:

                            conn = sq.connect("Packages.db")
                            cur = conn.cursor()
                            cur.execute(
                                f'''SELECT weight FROM Packages WHERE num = {package_num} ''')
                            for row in cur:
                                package_weight = row
                            if Car_weight[0] + package_weight[0] > max_car_weight[0]:
                                print(
                                    "By adding this package, the weight of the container exceeds its limit")
                            else:
                                conn = sq.connect("carWithRoom.db")
                                cur = conn.cursor()
                                cur.execute(
                                    f'''UPDATE carWithRoom SET weight ={Car_weight[0]+ package_weight[0]} , number_of_packages = {packages_number_in_car_with_room[0]+1} WHERE num={car_num}''')
                                conn.commit()
                                conn.close()
                                conn = sq.connect("Car_Packages.db")
                                cur = conn.cursor()
                                cur.execute(
                                    '''CREATE TABLE IF NOT EXISTS Car_Packages (num_package int PRIMARY KEY , num_carWithRoom int, type_Package text, type_carWithRoom text)''')
                                cur.execute(
                                    f'''INSERT OR IGNORE INTO Car_Packages VALUES ({package_num},{car_num},'normal','normal')''')
                                conn.commit()
                                conn.close()

####


def addContainertoCar(container_num):

    conn = sq.connect("containerCar_Container.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS containerCar_Container (Container_num int PRIMARY KEY,containerCar_num int ,type_container text)''')
    cur.execute(
        f'SELECT 1 FROM containerCar_Container WHERE Container_num={container_num} ')
    conn.commit()
    data = cur.fetchone()
    if data is not None:
        print("Container is already connected in another car")
        conn.close()
    else:

        conn = sq.connect("Container.db")
        cur = conn.cursor()
        cur.execute(f'SELECT 1 FROM Container WHERE num={container_num} ')
        data = cur.fetchone()
        if data is not None:

            cur.execute(
                f'''SELECT weight FROM Container WHERE num = {container_num}''')
            for row in cur:
                container_weight = row

            conn = sq.connect("containerCar.db")
            cur = conn.cursor()
            print("container cars\n number - max_weight - max_containers _ current number of containers - weight - property ")
            for row in cur.execute(f"SELECT * FROM containerCar "):
                print(row)

            conn.close()

            input_string = input("enter numbers seperated by space :")
            containerCar_num_list = input_string.split()
            for i in range(len(containerCar_num_list)):
                containerCar_num_list[i] = int(containerCar_num_list[i])

            for containerCar_num in containerCar_num_list:
                conn = sq.connect("containerCar.db")
                cur = conn.cursor()
                cur.execute(
                    f'''SELECT weight FROM containerCar WHERE num = {containerCar_num}''')
                for row in cur:
                    containerCar_weight = row

                conn.close()

                conn = sq.connect("containerCar.db")
                cur = conn.cursor()
                cur.execute(
                    f'''SELECT max_weight FROM containerCar WHERE num = {containerCar_num}''')
                for row in cur:
                    max_weight_containerCar = row

                conn.close()

                if (max_weight_containerCar[0] < containerCar_weight[0]+container_weight[0]):
                    print(
                        f"By adding  container {containerCar_num}, the weight of the container car exceeds its limit")

                else:
                    conn = sq.connect("containerCar.db")
                    cur = conn.cursor()
                    cur.execute(
                        f'''SELECT number_of_containers FROM containerCar WHERE num = {containerCar_num}''')
                    for row in cur:
                        number_of_containers_in_car = row

                    conn.close()

                    conn = sq.connect("containerCar.db")
                    cur = conn.cursor()
                    cur.execute(
                        f'''SELECT max_container_can_be_connected FROM containerCar WHERE num = {containerCar_num}''')
                    for row in cur:
                        max_number_of_container_in_car = row
                    conn.close()
                    if (number_of_containers_in_car >= max_number_of_container_in_car):
                        print(
                            f"The capacity of the vehicle for the container {containerCar_num} is complete")

                    else:

                        conn = sq.connect('containerCar.db')
                        cur = conn.cursor()
                        cur.execute(
                            f'''UPDATE containerCar SET weight ={containerCar_weight[0]+ container_weight[0]} , number_of_containers = {number_of_containers_in_car[0]+1} WHERE num={containerCar_num}''')
                        conn.commit()
                        conn.close()

                        conn = sq.connect("containerCar_Container.db")
                        cur = conn.cursor()

                        cur.execute(
                            '''CREATE TABLE IF NOT EXISTS containerCar_Container (Container_num int PRIMARY KEY,containerCar_num int ,type_container text)''')
                        cur.execute(
                            f'''INSERT OR IGNORE INTO containerCar_Container VALUES ({container_num},{containerCar_num},'normal')''')
                        conn.commit()
                        conn.close()
        conn.close()

        conn = sq.connect("freezerContainer.db")
        cur = conn.cursor()
        cur.execute(
            f'SELECT 1 FROM freezerContainer WHERE num={container_num} ')
        data = cur.fetchone()
        if data is not None:
            cur.execute(
                f'''SELECT weight FROM freezerContainer WHERE num = {container_num}''')
            for row in cur:
                container_weight = row

            conn = sq.connect("containerCar.db")
            cur = conn.cursor()
            print("container cars\n number - max_weight - max_containers _ current number of containers - weight - property ")
            for row in cur.execute(f"SELECT * FROM containerCar "):
                print(row)
            conn.close()
            input_string = input("enter numbers seperated by space :")
            containerCar_num_list = input_string.split()
            for i in range(len(containerCar_num_list)):
                containerCar_num_list[i] = int(containerCar_num_list[i])

            for containerCar_num in containerCar_num_list:

                cur.execute(
                    f'''SELECT weight FROM containerCar WHERE num = {containerCar_num}''')
                for row in cur:
                    containerCar_weight = row

                cur.execute(
                    f'''SELECT max_weight FROM containerCar WHERE num = {containerCar_num}''')
                for row in cur:
                    max_weight_containerCar = row

                if (max_weight_containerCar[0] < containerCar_weight[0]+container_weight[0]):
                    print(
                        f"By adding container{containerCar_num}, the weight of the container car exceeds its limit")

                else:
                    cur.execute(
                        f'''SELECT number_of_containers FROM containerCar WHERE num = {containerCar_num}''')
                    for row in cur:
                        number_of_containers_in_car = row

                    cur.execute(
                        f'''SELECT max_container_can_be_connected FROM containerCar WHERE num = {containerCar_num}''')
                    for row in cur:
                        max_number_of_container_in_car = row

                    if (number_of_containers_in_car >= max_number_of_container_in_car):
                        print(
                            f"The capacity of the vehicle for the container {containerCar_num} is complete")

                    else:
                        conn = sq.connect("containerCar_Container.db")
                        cur = conn.cursor()

                        cur.execute(
                            '''CREATE TABLE IF NOT EXISTS containerCar_Container (Container_num int PRIMARY KEY,containerCar_num int ,type_container text)''')
                        cur.execute(
                            f'''INSERT OR IGNORE INTO containerCar_Container VALUES ({container_num},{containerCar_num},'cold')''')
                        conn.commit()
                        conn.close()

        conn = sq.connect("breakableContainer.db")
        cur = conn.cursor()
        cur.execute(
            f'SELECT 1 FROM breakableContainer WHERE num={container_num} ')
        data = cur.fetchone()
        if data is not None:
            cur.execute(
                f'''SELECT weight FROM breakableContainer WHERE num = {container_num}''')
            for row in cur:
                container_weight = row

            conn = sq.connect("containerCar.db")
            cur = conn.cursor()
            print("container cars\n number - max_weight - max_containers _ current number of containers - weight - property ")
            for row in cur.execute(f"SELECT * FROM containerCar "):
                print(row)
            conn.close()
            input_string = input("enter numbers seperated by space :")
            containerCar_num_list = input_string.split()
            for i in range(len(containerCar_num_list)):
                containerCar_num_list[i] = int(containerCar_num_list[i])

            for containerCar_num in containerCar_num_list:

                conn = sq.connect("containerCar.db")
                cur = conn.cursor()
                cur.execute(
                    f'''SELECT weight FROM containerCar WHERE num = {containerCar_num}''')
                for row in cur:
                    containerCar_weight = row

                cur.execute(
                    f'''SELECT max_weight FROM containerCar WHERE num = {containerCar_num}''')
                for row in cur:
                    max_weight_containerCar = row

                if (max_weight_containerCar[0] < containerCar_weight[0]+container_weight[0]):
                    print(
                        f"By adding  container {containerCar_num}, the weight of the container car exceeds its limit")

                else:
                    cur.execute(
                        f'''SELECT number_of_containers FROM containerCar WHERE num = {containerCar_num}''')
                    for row in cur:
                        number_of_containers_in_car = row

                    cur.execute(
                        f'''SELECT max_container_can_be_connected FROM containerCar WHERE num = {containerCar_num}''')
                    for row in cur:
                        max_number_of_container_in_car = row

                    if (number_of_containers_in_car >= max_number_of_container_in_car):
                        print(
                            f"The capacity of the vehicle for the container {containerCar_num} is complete")

                    else:
                        conn = sq.connect("containerCar_Container.db")
                        cur = conn.cursor()

                        cur.execute(
                            '''CREATE TABLE IF NOT EXISTS containerCar_Container (Container_num int PRIMARY KEY,containerCar_num int ,type_container text)''')
                        cur.execute(
                            f'''INSERT OR IGNORE INTO containerCar_Container VALUES ({container_num},{containerCar_num},'breakable')''')
                        conn.commit()
                        conn.close()
    conn.close()


def addPackageToCantainer(container_num):

    conn = sq.connect("Container.db")
    cur = conn.cursor()
    cur.execute(f'SELECT 1 FROM Container WHERE num={container_num} ')
    data = cur.fetchone()
    conn.close()
    if data is not None:
        conn = sq.connect("Container.db")
        cur = conn.cursor()
        cur.execute(
            f'''SELECT number_of_packages FROM Container WHERE num = {container_num}''')
        for row in cur:
            packages_number_in_container = row
        cur.execute(
            f'''SELECT max_package FROM Container WHERE num = {container_num}''')
        for row in cur:
            max_package = row
        if (packages_number_in_container[0] >= max_package[0]):
            print("The capacity of the number of containers is complete ")

        else:
            cur.execute(
                f'''SELECT weight FROM Container WHERE num = {container_num}''')
            for row in cur:
                Container_weight = row

            cur.execute(
                f'''SELECT max_weight FROM Container WHERE num = {container_num}''')
            for row in cur:
                max_container_weight = row
            if (Container_weight[0] >= max_container_weight[0]):
                print("The weight capacity of the container is complete")

            else:
                conn.close()
                conn = sq.connect('Packages.db')
                cur = conn.cursor()
                print("normal packages\nnumber - weight - destination - beginning")
                for row in cur.execute('''SELECT * FROM Packages '''):
                    print(row)

                conn.close()
                input_string = input("enter numbers seperated by space :")
                package_num_list = input_string.split()
                for i in range(len(package_num_list)):
                    package_num_list[i] = int(package_num_list[i])

                for package_num in package_num_list:

                    conn = sq.connect("Container_Packages.db")
                    cur = conn.cursor()
                    cur.execute(
                        '''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
                    cur.execute(
                        f"SELECT 1 FROM Container_packages WHERE num_package = {package_num}")
                    conn.commit()
                    data = cur.fetchone()
                    if data is not None:
                        print(
                            f"package {package_num} is already exist in a container")

                    else:
                        conn = sq.connect("Car_Packages.db")
                        cur = conn.cursor()
                        cur.execute(
                            '''CREATE TABLE IF NOT EXISTS Car_Packages (num_package int PRIMARY KEY , num_carWithRoom int, type_Package text, type_carWithRoom text)''')
                        cur.execute(
                            f"SELECT 1 FROM Car_packages WHERE num_package = {package_num}")
                        conn.commit()
                        data = cur.fetchone()
                        if data is not None:
                            print(
                                f"package {package_num} is already exist in a car with room")

                        else:

                            conn = sq.connect("Packages.db")
                            cur = conn.cursor()
                            cur.execute(
                                f'''SELECT weight FROM Packages WHERE num = {package_num} ''')
                            package_weight = cur.fetchone()

                            if Container_weight[0] + package_weight[0] > max_container_weight[0]:
                                print(
                                    f"By adding  package {package_num}, the weight of the container exceeds its limit")

                            else:
                                conn = sq.connect("Container.db")
                                cur = conn.cursor()

                                cur.execute(
                                    f'''UPDATE Container SET weight ={Container_weight[0]+ package_weight[0]} , number_of_packages = {packages_number_in_container[0]+1} WHERE num={container_num}''')
                                conn.commit()
                                conn.close()

                                conn = sq.connect("Container_Packages.db")
                                cur = conn.cursor()

                                cur.execute(
                                    '''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
                                cur.execute(
                                    f'''INSERT OR IGNORE INTO Container_Packages VALUES ({package_num},{container_num},'normal','normal')''')

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
        cur.execute(
            f'''SELECT num FROM freezerContainer WHERE num = {container_num}''')
        for row in cur:
            packages_number_in_container = row
        cur.execute(
            f'''SELECT max_package FROM freezerContainer WHERE num = {container_num}''')
        for row in cur:
            max_package = row
        if (packages_number_in_container[0] >= max_package[0]):
            print("The capacity of the number of freezer containers is complete ")
        else:
            cur.execute(
                f'''SELECT weight FROM freezerContainer WHERE num = {container_num}''')
            for row in cur:
                Container_weight = row

            cur.execute(
                f'''SELECT max_weight FROM freezerContainer WHERE num = {container_num}''')
            for row in cur:
                max_container_weight = row
            if (Container_weight[0] >= max_container_weight[0]):
                print("The weight capacity of the freezer container is complete")
            else:
                conn = sq.connect('coldPackages.db')
                cur = conn.cursor()
                print(
                    "cold packages\n number - weight - destination - beginning - minimum tempreture - property")
                for row in cur.execute('''SELECT * FROM coldPackages '''):
                    print(row)

                input_string = input("enter numbers seperated by space :")
                package_num_list = input_string.split()
                for i in range(len(package_num_list)):
                    package_num_list[i] = int(package_num_list[i])

                for package_num in package_num_list:

                    conn = sq.connect("Container_Packages.db")
                    cur = conn.cursor()
                    cur.execute(
                        '''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
                    cur.execute(
                        f'SELECT 1 FROM Container_Packages WHERE num_package={package_num} ')
                    conn.commit()
                    data = cur.fetchone()

                    if data is not None:
                        print(
                            f"package {package_num} is already exist in a container")

                    else:
                        conn = sq.connect("Car_Packages.db")
                        cur = conn.cursor()
                        cur.execute(
                            '''CREATE TABLE IF NOT EXISTS Car_Packages (num_package int PRIMARY KEY , num_carWithRoom int, type_Package text, type_carWithRoom text)''')
                        cur.execute(
                            f'SELECT 1 FROM Car_Packages WHERE num_package={package_num} ')
                        conn.commit()
                        data = cur.fetchone()
                        if data is not None:
                            print(
                                f"package {package_num} is already exist in a car with room")

                        else:
                            conn = sq.connect("coldPackages.db")
                            cur = conn.cursor()
                            cur.execute(
                                f'''SELECT weight FROM coldPackages WHERE num = {package_num} ''')
                            for row in cur:
                                package_weight = row

                            if Container_weight[0] + package_weight[0] > max_container_weight[0]:
                                print(
                                    f"By adding package {package_num}, the weight of the freezer container exceeds its limit")

                            else:

                                conn = sq.connect("freezerContainer.db")
                                cur = conn.cursor()
                                cur.execute(
                                    f'''SELECT min_temp_produced_by_container FROM freezerContainer WHERE num = {container_num} ''')
                                for row in cur:
                                    min_temp_container = row

                                conn = sq.connect("coldPackages.db")
                                cur = conn.cursor()
                                cur.execute(
                                    f'''SELECT min_temperature FROM coldPackages WHERE num = {package_num} ''')
                                for row in cur:
                                    min_temp_package = row

                                if (min_temp_container[0] > min_temp_package[0]):
                                    print(
                                        f"The package {package_num} will be spoiled in this container")

                                else:

                                    conn = sq.connect("freezerContainer.db")
                                    cur = conn.cursor()

                                    cur.execute(
                                        f'''UPDATE freezerContainer SET weight ={Container_weight[0]+ package_weight[0]} , number_of_packages = {packages_number_in_container[0]+1} WHERE num={container_num}''')
                                    conn.commit()
                                    conn.close()

                                    conn = sq.connect("Container_Packages.db")
                                    cur = conn.cursor()
                                    cur.execute(
                                        '''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
                                    cur.execute(
                                        f'''INSERT OR IGNORE INTO Container_Packages VALUES ({package_num},{container_num},'cold','cold')''')

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
        cur.execute(
            f'''SELECT num FROM breakableContainer WHERE num = {container_num}''')
        for row in cur:
            packages_number_in_container = row
        cur.execute(
            f'''SELECT max_package FROM breakableContainer WHERE num = {container_num}''')
        for row in cur:
            max_package = row
        if (packages_number_in_container[0] >= max_package[0]):
            print("The capacity of the number of breakable containers is complete ")
        else:
            cur.execute(
                f'''SELECT weight FROM breakableContainer WHERE num = {container_num}''')
            for row in cur:
                Container_weight = row

            cur.execute(
                f'''SELECT max_weight FROM breakableContainer WHERE num = {container_num}''')
            for row in cur:
                max_container_weight = row
            if (Container_weight[0] >= max_container_weight[0]):
                print("The weight capacity of the breakable container is complete")
            else:
                conn = sq.connect('breakablePackages.db')
                cur = conn.cursor()
                print(
                    "breakable packages\n number - weight - destination - beginning - property")
                for row in cur.execute('''SELECT * FROM breakablePackages '''):
                    print(row)

                input_string = input("enter numbers seperated by space :")
                package_num_list = input_string.split()
                for i in range(len(package_num_list)):
                    package_num_list[i] = int(package_num_list[i])

                for package_num in package_num_list:

                    conn = sq.connect("Container_Packages.db")
                    cur = conn.cursor()
                    cur.execute(
                        '''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
                    cur.execute(
                        f'SELECT 1 FROM Container_Packages WHERE num_package={package_num} ')
                    conn.commit()
                    data = cur.fetchone()
                    if data is not None:
                        print(
                            f"package {package_num} is already exist in a container")
                    else:
                        conn = sq.connect("Car_Packages.db")
                        cur = conn.cursor()
                        cur.execute(
                            '''CREATE TABLE IF NOT EXISTS Car_Packages (num_package int PRIMARY KEY , num_carWithRoom int, type_Package text, type_carWithRoom text)''')
                        conn.commit()
                        cur.execute(
                            f'SELECT 1 FROM Car_Packages WHERE num_package={package_num} ')
                        data = cur.fetchone()
                        if data is not None:
                            print(
                                f"package {package_num} is already exist in a car with room")
                        else:
                            conn = sq.connect("breakablePackages.db")
                            cur = conn.cursor()
                            cur.execute(
                                f'''SELECT weight FROM breakablePackages WHERE num = {package_num} ''')
                            for row in cur:
                                package_weight = row

                            if Container_weight[0] + package_weight[0] > max_container_weight[0]:
                                print(
                                    f"By adding package {package_num}, the weight of the breakable container exceeds its limit")

                            else:
                                conn = sq.connect("breakableContainer.db")
                                cur = conn.cursor()

                                cur.execute(
                                    f'''UPDATE breakableContainer SET weight ={Container_weight[0]+ package_weight[0]} , number_of_packages = {packages_number_in_container[0]+1} WHERE num={container_num}''')
                                conn.commit()
                                conn.close()

                                conn = sq.connect("Container_Packages.db")
                                cur = conn.cursor()

                                cur.execute(
                                    '''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
                                cur.execute(
                                    f'''INSERT OR IGNORE INTO Container_Packages VALUES ({package_num},{container_num},'breakable','breakable')''')

                                conn.commit()
                                conn.close()


def export_waybill():
    conn = sq.connect("Car_Packages.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Car_Packages (num_package int PRIMARY KEY , num_carWithRoom int, type_Package text, type_carWithRoom text)''')
    cur.execute('''SELECT num_carWithRoom FROM Car_Packages ''')
    conn.commit()
    carWithRoom_keys = cur.fetchall()
    carWithRoom_keys = list(set(carWithRoom_keys))

    conn = sq.connect("containerCar_Container.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS containerCar_Container (Container_num int PRIMARY KEY,containerCar_num int ,type_container text)''')
    cur.execute('''SELECT containerCar_num FROM containerCar_Container''')
    conn.commit()
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
    conn.close()
    input_string = input("enter numbers seperated by space :")
    car_num_list = input_string.split()
    for i in range(len(car_num_list)):
        car_num_list[i] = int(car_num_list[i])

    for car_num in car_num_list:
        conn = sq.connect("carWithRoom.db")
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM carWithRoom WHERE num={car_num} ')
        data = cur.fetchone()
        if data is not None:
            conn = sq.connect('Car_Packages.db')
            cur = conn.cursor()
            cur.execute(
                f'''SELECT num_package FROM Car_Packages WHERE num_carWithRoom = {car_num}''')
            package_keys = cur.fetchall()

            conn = sq.connect('carWithRoom.db')
            cur = conn.cursor()
            cur.execute(f'''SELECT * FROM carWithRoom WHERE num = {car_num}''')
            car = cur.fetchall()

            conn = sq.connect('waybill.db')
            cur = conn.cursor()
            cur.execute(
                '''CREATE TABLE IF NOT EXISTS carWithRoom (num int PRIMARY KEY, max_weight real,max_package int,number_of_packages int,weight real,property text)''')
            cur.execute(
                f'''INSERT OR IGNORE INTO carWithRoom VALUES ({car[0][0]},{car[0][1]},{car[0][2]},{car[0][3]},{car[0][4]},'{car[0][5]}')''')
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
                cur.execute(
                    '''CREATE TABLE IF NOT EXISTS Car_Packages (package_num int PRIMARY KEY , car_num int)''')
                cur.execute(
                    f'''INSERT OR IGNORE INTO Car_Packages VALUES ({package_key[0]},{car_num})''')
                conn.commit()
                conn.close()

                conn = sq.connect('Packages.db')
                cur = conn.cursor()
                cur.execute(
                    f'''SELECT * FROM Packages WHERE num = {package_key[0]}''')
                package = cur.fetchall()

                conn = sq.connect('waybill.db')
                cur = conn.cursor()
                cur.execute(
                    '''CREATE TABLE IF NOT EXISTS Packages (package_num int PRIMARY KEY ,  weight real ,destinaton text , beginning text)''')
                cur.execute(
                    f'''INSERT OR IGNORE INTO Packages VALUES ({package[0][0]},{package[0][1]},'{package[0][2]}','{package[0][3]}')''')
                conn.commit()
                conn.close()

                conn = sq.connect("Packages.db")
                cur = conn.cursor()
                cur.execute(
                    f'''DELETE from Packages WHERE num = {package_key[0]}''')
                conn.commit()
                conn.close()

                conn = sq.connect("Car_Packages.db")
                cur = conn.cursor()
                cur.execute(
                    f'''DELETE from Car_Packages WHERE num_package = {package_key[0]}''')
                conn.commit()
                conn.close()

        conn = sq.connect("containerCar.db")
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM containerCar WHERE num={car_num} ')
        data = cur.fetchone()
        conn.close()
        if data is not None:
            conn = sq.connect('containerCar_Container.db')
            cur = conn.cursor()
            cur.execute(
                f'''SELECT Container_num FROM containerCar_Container WHERE containerCar_num = {car_num}''')
            container_keys = cur.fetchall()

            for container_key in container_keys:
                conn = sq.connect('containerCar_Container.db')
                cur = conn.cursor()
                cur.execute(
                    f'''SELECT type_container FROM containerCar_Container WHERE Container_num = {container_key[0]}''')
                type_container = cur.fetchone()
                conn.close()

                conn = sq.connect('waybill.db')
                cur = conn.cursor()
                cur.execute(
                    f'''CREATE TABLE IF NOT EXISTS container_incontainerCar (container_num int PRIMARY KEY , containerCar_num int, type_contianer text )''')
                cur.execute(
                    f'''INSERT OR IGNORE INTO container_incontainerCar VALUES ({container_key[0]},{car_num},'{type_container[0]}')''')
                conn.commit()
                conn.close()

                conn = sq.connect('containerCar.db')
                cur = conn.cursor()
                cur.execute(
                    f'''SELECT * FROM containerCar WHERE num = {car_num}''')
                car = cur.fetchone()
                conn.close()

                if car is not None:

                    conn = sq.connect('waybill.db')
                    cur = conn.cursor()
                    cur.execute(
                        '''CREATE TABLE IF NOT EXISTS containerCar (num int PRIMARY KEY, max_weight real,max_container_can_be_connected int,number_of_containers int,weight real,property text)''')
                    cur.execute(
                        f'''INSERT OR IGNORE INTO containerCar VALUES ({car[0]},{car[1]},{car[2]},{car[3]},{car[4]},'{car[5]}')''')
                    conn.commit()
                    conn.close()

                    conn = sq.connect("containerCar.db")
                    cur = conn.cursor()
                    cur.execute(
                        f'''DELETE from containerCar WHERE num = {car_num}''')
                    conn.commit()
                    conn.close()

                conn = sq.connect("containerCar_Container.db")
                cur = conn.cursor()
                cur.execute(
                    f'''DELETE from containerCar_Container WHERE Container_num = {container_key[0]}''')
                conn.commit()
                conn.close()

                conn = sq.connect('Container_Packages.db')
                cur = conn.cursor()
                cur.execute(
                    '''CREATE TABLE IF NOT EXISTS Container_Packages (num_package int PRIMARY KEY , num_Container int, type_Package text, type_Container text)''')
                cur.execute(
                    f'''SELECT num_package FROM Container_Packages WHERE num_Container = {container_key[0]}''')
                conn.commit()
                package_keys = cur.fetchall()
                conn.close()
                if type_container[0] == 'normal':
                    conn = sq.connect('Container.db')
                    cur = conn.cursor()
                    cur.execute(
                        f'''SELECT * FROM Container WHERE num = {container_key[0]}''')
                    container = cur.fetchone()

                    cur.execute(
                        f'''DELETE FROM Container WHERE num = {container_key[0]}''')
                    conn.close()

                    conn = sq.connect("waybill.db")
                    cur = conn.cursor()
                    cur.execute(
                        '''CREATE TABLE IF NOT EXISTS Container (num int PRIMARY KEY ,  max_weight real ,max_package int , number_of_packages int,weight real , property text)''')
                    cur.execute(
                        f'''INSERT OR IGNORE INTO Container VALUES ({container[0]},{container[1]},{container[2]},{container[3]},{container[4]},'{container[5]}')''')
                    conn.commit()
                    conn.close()

                    for package_key in package_keys:
                        conn = sq.connect('waybill.db')
                        cur = conn.cursor()
                        cur.execute(
                            f'''CREATE TABLE IF NOT EXISTS packages_inContainer (num_package int PRIMARY KEY,num_container int,type_package text)''')
                        cur.execute(
                            f'''INSERT OR IGNORE INTO packages_inContainer VALUES({package_key[0]},{container_key[0]},'normal')''')
                        conn.commit()
                        conn.close()

                        conn = sq.connect('Packages.db')
                        cur = conn.cursor()
                        cur.execute(
                            f'''SELECT * FROM Packages WHERE num = {package_key[0]} ''')
                        package = cur.fetchone()

                        conn = sq.connect("Packages.db")
                        cur = conn.cursor()
                        cur.execute(
                            f'''DELETE from Packages WHERE num = {package_key[0]}''')
                        conn.commit()
                        conn.close()

                        conn = sq.connect('waybill.db')
                        cur = conn.cursor()
                        cur.execute(
                            '''CREATE TABLE IF NOT EXISTS Packages (package_num int PRIMARY KEY ,  weight real ,destinaton text , beginning text)''')
                        cur.execute(
                            f'''INSERT OR IGNORE INTO Packages VALUES ({package[0]},{package[1]},'{package[2]}','{package[3]}')''')
                        conn.commit()
                        conn.close()

                        conn = sq.connect("Container_Packages.db")
                        cur = conn.cursor()
                        cur.execute(
                            f'''DELETE FROM Container_Packages WHERE num_package = {package_key[0]}''')
                        conn.commit()
                        conn.close()

                if type_container[0] == 'cold':

                    conn = sq.connect('freezerContainer.db')
                    cur = conn.cursor()
                    cur.execute(
                        f'''SELECT * FROM freezerContainer WHERE num = {container_key[0]}''')
                    container = cur.fetchone()

                    cur.execute(
                        f'''DELETE FROM freezerContainer WHERE num = {container_key[0]}''')

                    conn = sq.connect("waybill.db")
                    cur = conn.cursor()
                    cur.execute(
                        '''CREATE TABLE IF NOT EXISTS Container (num int PRIMARY KEY ,  max_weight real ,max_package int , number_of_packages int,weight real , property text)''')
                    cur.execute(
                        f'''INSERT OR IGNORE INTO Container VALUES ({container[0]},{container[1]},{container[2]},{container[3]},{container[4]},'{container[5]}')''')
                    conn.commit()
                    conn.close()
                    for package_key in package_keys:
                        conn = sq.connect('waybill.db')
                        cur = conn.cursor()
                        cur.execute(
                            f'''CREATE TABLE IF NOT EXISTS packages_inContainer (num_package int PRIMARY KEY,num_container int,type_package text)''')
                        cur.execute(
                            f'''INSERT OR IGNORE INTO packages_inContainer VALUES({package_key[0]},{container_key[0]},'cold')''')
                        conn.commit()
                        conn.close()

                        conn = sq.connect('coldPackages.db')
                        cur = conn.cursor()
                        cur.execute(
                            f'''SELECT * FROM coldPackages WHERE num = {package_key[0]} ''')
                        package = cur.fetchone()

                        conn = sq.connect("coldPackages.db")
                        cur = conn.cursor()
                        cur.execute(
                            f'''DELETE from coldPackages WHERE num = {package_key[0]}''')
                        conn.commit()
                        conn.close()

                        conn = sq.connect('waybill.db')
                        cur = conn.cursor()
                        cur.execute(
                            '''CREATE TABLE IF NOT EXISTS Packages (package_num int PRIMARY KEY ,  weight real ,destinaton text , beginning text)''')
                        cur.execute(
                            f'''INSERT OR IGNORE INTO Packages VALUES ({package[0]},{package[1]},'{package[2]}','{package[3]}')''')
                        conn.commit()
                        conn.close()

                        conn = sq.connect("Container_Packages.db")
                        cur = conn.cursor()
                        cur.execute(
                            f'''DELETE FROM Container_Packages WHERE num_package = {package_key[0]}''')
                        conn.commit()
                        conn.close()

                if type_container[0] == 'breakable':
                    conn = sq.connect('breakableContainer.db')
                    cur = conn.cursor()
                    cur.execute(
                        f'''SELECT * FROM breakableContainer WHERE num = {container_key[0]}''')
                    container = cur.fetchone()

                    cur.execute(
                        f'''DELETE FROM breakableContainer WHERE num = {container_key[0]}''')
                    conn.commit()
                    conn.close()

                    conn = sq.connect("waybill.db")
                    cur = conn.cursor()
                    cur.execute(
                        '''CREATE TABLE IF NOT EXISTS Container (num int PRIMARY KEY ,  max_weight real ,max_package int , number_of_packages int,weight real , property text)''')
                    cur.execute(
                        f'''INSERT OR IGNORE INTO Container VALUES ({container[0]},{container[1]},{container[2]},{container[3]},{container[4]},'{container[5]}')''')
                    conn.commit()
                    conn.close()
                    for package_key in package_keys:
                        conn = sq.connect('waybill.db')
                        cur = conn.cursor()
                        cur.execute(
                            f'''CREATE TABLE IF NOT EXISTS packages_inContainer (num_package int PRIMARY KEY,num_container int,type_package text)''')
                        cur.execute(
                            f'''INSERT OR IGNORE INTO packages_inContainer VALUES({package_key[0]},{container_key[0]},'breakable')''')
                        conn.commit()
                        conn.close()
                        conn = sq.connect('breakablePackages.db')
                        cur = conn.cursor()
                        cur.execute(
                            f'''SELECT * FROM breakablePackages WHERE num = {package_key[0]} ''')
                        package = cur.fetchone()

                        conn = sq.connect("breakablePackages.db")
                        cur = conn.cursor()
                        cur.execute(
                            f'''DELETE from breakablePackages WHERE num = {package_key[0]}''')
                        conn.commit()
                        conn.close()

                        conn = sq.connect('waybill.db')
                        cur = conn.cursor()
                        cur.execute(
                            '''CREATE TABLE IF NOT EXISTS Packages (package_num int PRIMARY KEY ,  weight real ,destinaton text , beginning text)''')
                        cur.execute(
                            f'''INSERT OR IGNORE INTO Packages VALUES ({package[0]},{package[1]},'{package[2]}','{package[3]}')''')
                        conn.commit()
                        conn.close()

                        conn = sq.connect("Container_Packages.db")
                        cur = conn.cursor()
                        cur.execute(
                            f'''DELETE FROM Container_Packages WHERE num_package = {package_key[0]}''')
                        conn.commit()
                        conn.close()

            conn = sq.connect("containerCar_Container.db")
            cur = conn.cursor()
            cur.execute(
                f'''DELETE from containerCar_Container WHERE containerCar_num = {car_num}''')
            conn.commit()
            conn.close()
###########################
    try:
        conn = sq.connect("waybill.db")
        cur = conn.cursor()
        print("cars with room\nnumber - max weight - max packages - current number of packages - current weight - property  ")
        for row in cur.execute('''SELECT * FROM carWithRoom '''):
            print(row)

        print("\npackages in car with room\npackage number - car with room number")
        for row in cur.execute('''SELECT * FROM Car_Packages '''):
            print(row)
    except:
        pass

    try:
        print("\ncontainer cars\nnumber - max weight - max container - current number of containers in car - current weight - property")
        for row in cur.execute('''SELECT * FROM containerCar'''):
            print(row)

        print("\ncontainer in container car\ncontainer number - container car number - type container")
        for row in cur.execute('''SELECT * FROM container_incontainerCar'''):
            print(row)

        print("\ncontainers\nnumber - max weight - max package - current number of packages - current weight - type container - property")
        for row in cur.execute('''SELECT * FROM Container'''):
            print(row)

        print("\npackage in container\npackage number - container number - type package")
        for row in cur.execute('''SELECT * FROM packages_inContainer'''):
            print(row)
    except:
        pass
    try:
        print("\npackages\npackage number - weight - destination - beginning")
        for row in cur.execute('''SELECT * FROM Packages'''):
            print(row)
    except:
        pass


def showPackages_onTheWay():
    conn = sq.connect("waybill.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Packages (package_num int PRIMARY KEY ,  weight real ,destinaton text , beginning text)''')
    print("\npackages\npackage number - weight - destination - beginning")
    conn.commit()
    for row in cur.execute('''SELECT * FROM Packages'''):
        print(row)

    input_string = input("enter numbers seperated by space :")
    package_num_list = input_string.split()
    for i in range(len(package_num_list)):
        package_num_list[i] = int(package_num_list[i])

    for package_num in package_num_list:

        conn = sq.connect("waybill.db")
        cur = conn.cursor()
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS Car_Packages (package_num int PRIMARY KEY , car_num int)''')
        cur.execute(
            f'''SELECT * FROM Car_Packages WHERE package_num = {package_num}''')
        conn.commit()
        data = cur.fetchone()
        if data is not None:
            cur.execute(
                f'''SELECT car_num FROM Car_Packages WHERE package_num = {package_num}''')
            car_num = cur.fetchone()

            cur.execute(
                f'''SELECT package_num FROM Car_Packages WHERE car_num = {car_num[0]}''')
            packages_num_incar_list = cur.fetchall()

            for package_num2 in packages_num_incar_list:

                cur.execute(
                    f'''DELETE FROM Car_Packages WHERE package_num = {package_num}''')
                conn.commit()
                conn.close()

                conn = sq.connect("waybill.db")
                cur = conn.cursor()
                cur.execute(
                    f'''SELECT * FROM Packages WHERE package_num = {package_num2[0]}''')
                package = cur.fetchone()

                cur.execute(
                    f'''DELETE  FROM Packages WHERE package_num = {package_num2[0]}''')
                conn.commit()
                conn.close()

                conn = sq.connect("Packages.db")
                cur = conn.cursor()
                cur.execute(
                    f'''INSERT OR IGNORE INTO Packages VALUES ({package[0]},{package[1]},'{package[2]}','{package[3]}')''')
                conn.commit()
                conn.close()

            conn = sq.connect("waybill.db")
            cur = conn.cursor()
            cur.execute(
                f'''DELETE FROM Car_Packages WHERE car_num = {car_num[0]}''')
            cur.execute(
                f'''DELETE FROM carWithRoom WHERE num = {car_num[0]}''')
            conn.commit()

            conn = sq.connect("waybill.db")
            cur = conn.cursor()
            cur.execute(
                f'''SELECT * FROM carWithRoom WHERE num = {car_num[0]}''')
            car = cur.fetchone()
            conn.commit()

            if car is not None:

                conn = sq.connect("carWithRoom.db")
                cur = conn.cursor()
                cur.execute(
                    f'''INSERT OR IGNORE INTO carWithRoom VALUES ({car[0]},{car[1]},{car[2]},{car[3]},{car[4]},'{car[5]}')''')
                conn.commit()
                conn.close()

            # ____________

        conn = sq.connect("waybill.db")
        cur = conn.cursor()
        cur.execute(
            f'''CREATE TABLE IF NOT EXISTS packages_inContainer (num_package int PRIMARY KEY,num_container int,type_package text)''')
        cur.execute(
            f'''SELECT * FROM packages_inContainer WHERE num_package = {package_num}''')
        conn.commit()
        data = cur.fetchone()
        if data is not None:
            conn = sq.connect("waybill.db")
            cur = conn.cursor()
            cur.execute(
                f'''SELECT type_package FROM packages_inContainer WHERE num_package = {package_num}''')
            type_package = cur.fetchone()
            if type_package[0] == "normal":
                cur.execute(
                    f'''SELECT num_container FROM packages_inContainer WHERE num_package = {package_num}''')
                container_num = cur.fetchone()

                cur.execute(
                    f'''SELECT containerCar_num FROM container_incontainerCar WHERE container_num = {container_num[0]}''')
                containerCar_num = cur.fetchone()

                cur.execute(
                    f'''SELECT container_num  FROM container_incontainerCar WHERE containerCar_num = {containerCar_num[0]}''')
                containers_num_incar = cur.fetchall()

                cur.execute(
                    f'DELETE  FROM container_incontainerCar WHERE containerCar_num = {container_num[0]}')
                conn.commit()

                cur.execute(
                    f'''SELECT * FROM containerCar WHERE num = {containerCar_num[0]}''')
                containerCar = cur.fetchone()

                cur.execute(
                    f'''DELETE FROM containerCar WHERE num = {containerCar_num[0]}''')
                conn.commit()
                conn.close()

                conn = sq.connect("containerCar.db")
                cur = conn.cursor()
                cur.execute(
                    f'''INSERT OR IGNORE INTO containerCar VALUES ({containerCar[0]},{containerCar[1]},{containerCar[2]},{containerCar[3]},{containerCar[4]},'{containerCar[5]}')''')
                conn.commit()
                conn.close()

                for container_i in containers_num_incar:
                    conn = sq.connect("waybill.db")
                    cur = conn.cursor()
                    cur.execute(
                        f'''SELECT * FROM Container WHERE num = {container_i[0]}''')
                    container = cur.fetchone()

                    cur.execute(
                        f'DELETE  FROM Container WHERE num = {container_i[0]}')
                    conn.commit()
                    conn.close()

                    conn = sq.connect("waybill.db")
                    cur = conn.cursor()
                    cur.execute(
                        f'''DELETE FROM container_incontainerCar WHERE container_num = {container_i[0]}''')
                    conn.commit()
                    conn.close()

                    if container is not None:
                        conn = sq.connect("Container.db")
                        cur = conn.cursor()
                        cur.execute(
                            f'''INSERT OR IGNORE INTO Container VALUES ({container[0]},{container[1]},{container[2]},{container[3]},{container[4]},'{container[5]}')''')
                        conn.commit()
                        conn.close()

                    conn = sq.connect("waybill.db")
                    cur = conn.cursor()
                    cur.execute(
                        f'''SELECT num_package FROM packages_inContainer WHERE num_container = {container_i[0]}''')
                    packages_num_incontainer_list = cur.fetchall()
                    cur.execute(
                        f'''DELETE FROM packages_inContainer WHERE num_container = {container_i[0]}''')
                    conn.commit()
                    conn.close()

                    for package_i in packages_num_incontainer_list:
                        conn = sq.connect("waybill.db")
                        cur = conn.cursor()
                        cur.execute(
                            f'SELECT * FROM Packages WHERE package_num = {package_i[0]}')
                        package = cur.fetchone()

                        cur.execute(
                            f'DELETE  FROM Packages WHERE package_num = {package_i[0]}')
                        conn.commit()

                        conn = sq.connect("Packages.db")
                        cur = conn.cursor()
                        cur.execute(
                            f'''INSERT OR IGNORE INTO Packages VALUES ({package[0]},{package[1]},'{package[2]}','{package[3]}')''')
                        conn.commit()
                        conn.close()

                        conn = sq.connect("waybill.db")
                        cur = conn.cursor()
                        cur.execute(
                            f'''DELETE FROM containerCar WHERE num = {container_num[0]}''')
                        conn.commit()
                        conn.close()

            if type_package[0] == "cold":
                cur.execute(
                    f'''SELECT num_container FROM packages_inContainer WHERE num_package = {package_num}''')
                container_num = cur.fetchone()

                cur.execute(
                    f'''SELECT containerCar_num FROM container_incontainerCar WHERE container_num = {container_num[0]}''')
                containerCar_num = cur.fetchone()

                cur.execute(
                    f'''SELECT container_num  FROM container_incontainerCar WHERE containerCar_num = {containerCar_num[0]}''')
                containers_num_incar = cur.fetchall()

                cur.execute(
                    f'DELETE FROM container_incontainerCar WHERE containerCar_num = {container_num[0]}')
                conn.commit()

                cur.execute(
                    f'''SELECT * FROM containerCar WHERE num = {containerCar_num[0]}''')
                containerCar = cur.fetchone()

                cur.execute(
                    f'''DELETE FROM containerCar WHERE num = {container_num[0]}''')
                conn.commit()
                conn.close()

                conn = sq.connect("containerCar.db")
                cur = conn.cursor()
                cur.execute(
                    f'''INSERT OR IGNORE INTO containerCar VALUES ({containerCar[0]},{containerCar[1]},{containerCar[2]},{containerCar[3]},{containerCar[4]},'{containerCar[5]}')''')
                conn.commit()
                conn.close()

                for container_i in containers_num_incar:
                    conn = sq.connect("waybill.db")
                    cur = conn.cursor()
                    cur.execute(
                        f'''SELECT * FROM Container WHERE num = {container_i[0]}''')
                    container = cur.fetchone()

                    cur.execute(
                        f'DELETE  FROM Container WHERE num = {container_i[0]}')
                    conn.commit()

                    conn = sq.connect("freezerContainer.db")
                    cur = conn.cursor()
                    cur.execute(
                        f'''INSERT OR IGNORE INTO freezerContainer VALUES ({container[0]},{container[1]},{container[2]},{container[3]},{container[4]},-5,'{container[5]}')''')
                    conn.commit()
                    conn.close()

                    conn = sq.connect("waybill.db")
                    cur = conn.cursor()
                    cur.execute(
                        f'''SELECT num_package FROM packages_inContainer WHERE num_container = {container_i[0]}''')
                    packages_num_incontainer_list = cur.fetchall()
                    cur.execute(
                        f'''DELETE FROM packages_inContainer WHERE num_container = {container_i[0]}''')
                    conn.commit()
                    for package_i in packages_num_incontainer_list:
                        conn = sq.connect("waybill.db")
                        cur = conn.cursor()
                        cur.execute(
                            f'SELECT * FROM Packages WHERE package_num = {package_i[0]}')
                        package = cur.fetchone()

                        cur.execute(
                            f'DELETE  FROM Packages WHERE package_num = {package_i[0]}')
                        conn.commit()

                        conn = sq.connect("coldPackages.db")
                        cur = conn.cursor()
                        cur.execute(
                            f'''INSERT OR IGNORE INTO coldPackages VALUES ({package[0]},{package[1]},'{package[2]}','{package[3]}',{5},'')''')
                        conn.commit()
                        conn.close()

                        conn = sq.connect("waybill.db")
                        cur = conn.cursor()
                        cur.execute(
                            f'''DELETE FROM containerCar WHERE num = {container_num[0]}''')
                        conn.commit()
                        conn.close()

            if type_package[0] == "breakable":

                cur.execute(
                    f'''SELECT num_container FROM packages_inContainer WHERE num_package = {package_num}''')
                container_num = cur.fetchone()

                cur.execute(
                    f'''SELECT containerCar_num FROM container_incontainerCar WHERE container_num = {container_num[0]}''')
                containerCar_num = cur.fetchone()

                cur.execute(
                    f'''SELECT container_num  FROM container_incontainerCar WHERE containerCar_num = {containerCar_num[0]}''')
                containers_num_incar = cur.fetchall()

                cur.execute(
                    f'DELETE FROM container_incontainerCar WHERE containerCar_num = {container_num[0]}')
                conn.commit()

                cur.execute(
                    f'''SELECT * FROM containerCar WHERE num = {containerCar_num[0]}''')
                containerCar = cur.fetchone()

                cur.execute(
                    f'''DELETE FROM containerCar WHERE num = {container_num[0]}''')
                conn.commit()
                conn.close()

                conn = sq.connect("containerCar.db")
                cur = conn.cursor()
                cur.execute(
                    f'''INSERT OR IGNORE INTO containerCar VALUES ({containerCar[0]},{containerCar[1]},{containerCar[2]},{containerCar[3]},{containerCar[4]},'{containerCar[5]}')''')
                conn.commit()
                conn.close()

                for container_i in containers_num_incar:
                    conn = sq.connect("waybill.db")
                    cur = conn.cursor()
                    cur.execute(
                        f'''SELECT * FROM Container WHERE num = {container_i[0]}''')
                    container = cur.fetchone()

                    cur.execute(
                        f'DELETE  FROM Container WHERE num = {container_i[0]}')
                    conn.commit()

                    conn = sq.connect("breakableContainer.db")
                    cur = conn.cursor()
                    cur.execute(
                        f'''INSERT OR IGNORE INTO breakableContainer VALUES ({container[0]},{container[1]},{container[2]},110,{container[3]},{container[4]},'{container[5]}')''')
                    conn.commit()
                    conn.close()

                    conn = sq.connect("waybill.db")
                    cur = conn.cursor()
                    cur.execute(
                        f'''CREATE TABLE IF NOT EXISTS packages_inContainer (num_package int PRIMARY KEY,num_container int,type_package text)''')
                    cur.execute(
                        f'''SELECT num_package FROM packages_inContainer WHERE num_container = {container_i[0]}''')
                    packages_num_incontainer_list = cur.fetchall()
                    cur.execute(
                        f'''DELETE FROM packages_inContainer WHERE num_container = {container_i[0]}''')
                    conn.commit()

                    for package_i in packages_num_incontainer_list:
                        conn = sq.connect("waybill.db")
                        cur = conn.cursor()
                        cur.execute(
                            f'SELECT * FROM Packages WHERE package_num = {package_i[0]}')
                        package = cur.fetchone()

                        cur.execute(
                            f'DELETE FROM Packages WHERE package_num = {package_i[0]}')
                        conn.commit()

                        conn = sq.connect("breakablePackages.db")
                        cur = conn.cursor()
                        cur.execute(
                            f'''INSERT OR IGNORE INTO breakablePackages VALUES ({package[0]},{package[1]},'{package[2]}','{package[3]}','')''')
                        conn.commit()
                        conn.close()

                        conn = sq.connect("waybill.db")
                        cur = conn.cursor()
                        cur.execute(
                            f'''DELETE FROM containerCar WHERE num = {container_num[0]}''')
                        conn.commit()
                        conn.close()


def Exit():
    sys.exit()


def printMenu():
    print("1 'add , edit and remove package' ")
    print("\n2 'add , edit and remove container' ")
    print("\n3 'add , edit and remove car '")
    print("\n4 ' Loading '")
    print("\n5 'Send and receive package '")
    print("\n6 'Exit '")


def loadingMenu():
    print("1 'show packages'")
    print("\n2 'show containers'")
    print("\n3 'show cars'")
    print("\n4 'loading package into container'")
    print("\n5 'loading package into car with room' ")
    print("\n6 'loading container into container car'")
    print("\n7 'Return to the beginning of the program'")
    print("\n8 'Exit from program'")
    loading_order = int(input("\nChoose a number from the above numbers : "))
    if loading_order == 1:
        showallPackages()
    if loading_order == 2:
        showallcontainers()
    if loading_order == 3:
        showallCars()
    if loading_order == 4:
        container_num = int(input("Enter container number : "))
        addPackageToCantainer(container_num)
        print("package added to container")
        loadingMenu()

    if loading_order == 5:
        car_num = int(input("Enter car number : "))
        addPackageTocarWithRoom(car_num)
        print("package added into car with room")
        loadingMenu()

    if loading_order == 6:
        container_num = int(input("Enter container number : "))
        addContainertoCar(container_num)
        print("container added into car")
        loadingMenu()

    if loading_order == 7:
        main()

    if loading_order == 8:
        Exit()

    else:
        print("wrong number ")
        loadingMenu()


def sendAndReceiveMenu():
    print("1 'show packages in the way'")
    print("\n2 'issuing and save and show waybill'")
    print("\n3 'Return to the beginning of the program'")
    print("\n4 'Exit program'")
    order = int(input("Choose a number from the above numbers : "))

    if order == 1:
        showPackages_onTheWay()
        print("task done")
        sendAndReceiveMenu()

    if order == 2:
        export_waybill()
        print("task done")
        sendAndReceiveMenu()

    if order == 3:
        main()

    if order == 4:
        Exit()


def main():
    printMenu()
    order = int(input("\nChoose a number from the above numbers : "))
    if order == 1:
        print("1 'add package'")
        print("\n2 'edit package'")
        print("\n3 'remove package'")
        package_order = int(input("Choose a number from the above numbers : "))
        if package_order == 1:
            print("1 'add normal package'")
            print("\n2 'add cold package'")
            print("\n3 'add breakable package'")
            package_type_order = int(
                input("\nChoose a number from the above numbers : "))
            if package_type_order == 1:
                number, weight, destination, beginning = input(
                    "\nEnter 'number' and 'weight' and 'destination' and 'beginning' separated by space : ").split()
                weight = float(weight)
                number = int(number)
                x1 = Package(number, weight, destination, beginning)
                print("package added")
                main()

            elif package_type_order == 2:
                number, weight, destination, beginning, min_temp = input(
                    "\nEnter 'number' and 'weight' and 'destination' and 'beginning' and 'min temprature' separated by space : ").split()
                property = input(
                    "enter property if package has property else leave it blank :  ")
                weight = float(weight)
                min_temp = float(min_temp)
                number = int(number)
                if property != "":
                    x2 = coldPackage(number, weight, destination,
                                     beginning, min_temp, property)
                    print("package added")
                    main()
                else:
                    x2 = coldPackage(
                        number, weight, destination, beginning, min_temp)
                    print("package added")
                    main()

            elif package_type_order == 3:
                number, weight, destination, beginning = input(
                    "\nEnter 'number' and 'weight' and 'destination' and 'beginning'  separated by space : ").split()
                property = input(
                    "enter property if package has property else leave it blank :  ")
                weight = float(weight)
                number = int(number)
                if property != "":
                    x3 = breakablePackage(
                        number, weight, destination, beginning, property)
                    print("package added")
                    main()
                else:
                    x3 = breakablePackage(
                        number, weight, destination, beginning)
                    print("package added")
                    main()

            else:
                print("wrong number")
                main()

        elif package_order == 2:
            package_num = int(input("Enter package number : "))
            packageEditor(package_num)
            print("package edited")
            main()

        elif package_order == 3:
            package_num = int(input("Enter package number : "))
            packageRemover(package_num)
            print("package removed")
            main()

        else:
            print("wrong number")
            main()

    elif order == 2:
        print("1 'add container'")
        print("\n2 'edit container'")
        print("\n3 'remove container'")
        container_order = int(
            input("\nChoose a number from the above numbers : "))

        if container_order == 1:
            print("1 'add normal container'")
            print("\n2 'add freezer container'")
            print("\n3 'add container for breakable packages '")
            container_type_order = int(
                input("\nChoose a number from the above numbers : "))
            if container_type_order == 1:
                number, max_weight, max_package = input(
                    "\nEnter 'number' and 'max weight' and 'max package' separated by space : ").split()
                property = input(
                    "enter property if container has property else leave it blank :  ")
                number = int(number)
                max_weight = float(max_weight)
                max_package = int(max_package)
                if property != '':
                    x1 = Container(number, max_weight,
                                   max_package, property=property)
                    print("container added")
                    main()
                else:
                    x2 = Container(number, max_weight, max_package)
                    print("container added")
                    main()

            elif container_type_order == 2:
                number, max_weight, max_package, min_temp = input(
                    "\nEnter 'number' and 'max weight' and 'max package'and 'min temperatue' separated by space : ").split()
                property = input(
                    "enter property if container has property else leave it blank :  ")
                number = int(number)
                max_weight = float(max_weight)
                max_package = int(max_package)
                min_temp = float(min_temp)
                if property != "":
                    x1 = freezerContainer(
                        number, max_weight, max_package, min_temp, property=property)
                    print("container added")
                    main()
                else:
                    x1 = freezerContainer(
                        number, max_weight, max_package, min_temp)
                    print("container added")
                    main()

            elif container_type_order == 3:
                number, max_weight, max_package, max_speed = input(
                    "\nEnter 'number' and 'max weight' and 'max package'and 'max speed' separated by space : ").split()
                property = input(
                    "enter property if container has property else leave it blank :  ")
                number = int(number)
                max_weight = float(max_weight)
                max_speed = int(max_speed)
                if property != "":
                    x1 = breakableContainer(
                        number, max_weight, max_package, max_speed, property=property)
                    print("container added")
                    main()
                else:
                    x1 = breakableContainer(
                        number, max_weight, max_package, max_speed)
                    print("container added")
                    main()

        elif container_order == 2:
            container_num = int(input("Enter container number : "))
            containerEditor(container_num)
            print("container edited")
            main()

        elif container_order == 3:
            container_num = int(input("Enter container number : "))
            containerRemover(container_num)
            print("container removed")
            main()

        else:
            print("wrong number")
            main()

    elif order == 3:
        print("1 'add car'")
        print("\n2 'edit car'")
        print("\n3 'remove car'")
        car_order = int(input("\nChoose a number from the above numbers : "))
        if car_order == 1:
            print("1 'add car with room'")
            print("\n2 'add container car'")
            car_type_order = int(
                input("\nChoose a number from the above numbers : "))
            if car_type_order == 1:
                number, max_weight, max_package = input(
                    "\nEnter 'number' and 'max weight' and 'max package' separated by space : ").split()
                property = input(
                    "enter property if car has property else leave it blank :  ")
                number = int(number)
                max_weight = float(max_weight)
                max_package = int(max_package)
                if property != "":
                    x3 = carWithRoom(number, max_weight,
                                     max_package, property=property)
                    print("car added")
                    main()

                else:
                    x3 = carWithRoom(number, max_weight, max_package)
                    print("car added")
                    main()

            if car_type_order == 2:
                number, max_weight, max_container = input(
                    "\nEnter 'number' and 'max weight' and 'max container' separated by space : ").split()
                property = input(
                    "enter property if car has property else leave it blank :  ")
                number = int(number)
                max_weight = float(max_weight)
                max_container = int(max_container)
                if property != "":
                    x2 = containerCar(number, max_weight,
                                      max_container, property=property)
                    print("car added")
                    main()
                else:
                    x2 = containerCar(number, max_weight, max_container)
                    print("car added")
                    main()

            else:
                print('wrong number')
                main()

        elif car_order == 2:
            car_num = int(input("Enter car number : "))
            carEditor(car_num)
            print("car edited")
            main()

        elif car_order == 3:
            car_num = int(input("Enter car number : "))
            carRemover(car_num)
            print("car deleted")
            main()

        else:
            print("wrong number")
            main()

    elif order == 4:
        loadingMenu()
        conn = sq.connect("Packages.db")
        conn.close()

    elif order == 5:
        sendAndReceiveMenu()

    elif order == 6:
        Exit()

    else:
        print("wrong number")
        main()


def start():

    if login():
        main()
    else:
        print("wrong user name or password")
        start()


start()
