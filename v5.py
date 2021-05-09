import sqlite3,csv
from menu import programMenu

class phoneClass(object):
    def _init_(self,userName):
        self.name = ''
        self.out = ''

    def start (self):
        userChoice = programMenu.mainMenu()
        stop = 0
        while stop == 0 :
            if userChoice == 1:
                self.listAll()
            elif userChoice == 2:
                self.searchID()  
            elif userChoice == 3:
                self.searchBySpecs()
            elif userChoice == 5:
                stop = 1
            else:
                print("Invalid input")
            userChoice = programMenu.mainMenu()

    def searchBySpecs(self):
        userInput = programMenu.specMenu()
        return


    def listAll(self):
        cur.execute("SELECT * FROM phoneTable")
        result = cur.fetchall()
        print(result)

    def searchID(self):
        searchId = input("ID of Phone: ")
        sql_cmd = "SELECT * FROM phoneTable WHERE id = '{}'".format(searchId)
        cur.execute(sql_cmd)
        result = cur.fetchall()
        print (result)
    
    def searchDualSim(self):
        searchDS = input("\tDual Sim?(Y/N) ")
        searchDS = searchDS.lower()
        if searchDS == "y":
            sql_cmd = "SELECT * FROM phoneTable WHERE dual_sim = '1'"
            cur.execute(sql_cmd)
            result = cur.fetchall()
            print (result)
        elif searchDS =="n":
            sql_cmd = "SELECT * FROM phoneTable WHERE dual_sim = '0'"
            cur.execute(sql_cmd)
            result = cur.fetchall()
            print (result)
        else:
            print("Wrong input")
     
    def searchClockSpeed(self):
        searchCS =input ("Clock speed required: ")
        sql_cmd = "SELECT * FROM phoneTable WHERE clock_speed = '{}'".format(searchCS)
        cur.execute(sql_cmd)
        result = cur.fetchall()
        print(result)

    def searchFrontCam(self):
        searchFC = input ("Front Camera Resolution in megapixels: ")
        sql_cmd = "SELECT * FROM phoneTable WHERE clock_speed = '{}'".format(searchFC)
        cur.execute(sql_cmd)
        result = cur.fetchall()
        print(result)
    
    def searchInternalMemory(self):
        searchIM = input ("Required phone memory in GB: ")
        sql_cmd = "SELECT * FROM phoneTable WHERE clock_speed = '{}'".format(searchIM)
        cur.execute(sql_cmd)
        result = cur.fetchall()
        print(result)
    
    def searchPrimaryCam(self):
        searchPC = input ("Back Camera Resolution in megapixels: ")
        sql_cmd = "SELECT * FROM phoneTable WHERE clock_speed = '{}'".format(searchPC)
        cur.execute(sql_cmd)
        result = cur.fetchall()
        print(result)
    
    def searchRam(self):
        searchR = input ("Amount of ram in mb: ")
        sql_cmd = "SELECT * FROM phoneTable WHERE clock_speed = '{}'".format(searchR)
        cur.execute(sql_cmd)
        result = cur.fetchall()
        print(result)
    
    def searchTouchScreen(self):
        searchTS = input ("Touch screen? (Y/N)")
        searchTS = searchTS.lower()
        if searchTS == "y":
            sql_cmd = "SELECT * FROM phoneTable WHERE dual_sim = '1'"
            cur.execute(sql_cmd)
            result = cur.fetchall()
            print (result)
        elif searchTS =="n":
            sql_cmd = "SELECT * FROM phoneTable WHERE dual_sim = '0'"
            cur.execute(sql_cmd)
            result = cur.fetchall()
            print (result)
        else:
            print("Wrong input")

        


try:
    conn = sqlite3.connect('phones.db', uri=True)
    cur = conn.cursor()
# gawa ng table tangalin if wala
    cur.execute("""CREATE TABLE phoneTable(
        id TEXT,
        battery_power INTEGER,
        blue INTEGER,
        clock_speed INTEGER,
        dual_sim INTEGER,
        fc INTEGER,
        four_g INTEGER,
        int_memory INTEGER,
        m_dep INTEGER,
        mobile_wt INTEGER,
        n_cores INTEGER,
        pc INTEGER,
        px_height INTEGER,
        px_width INTEGER,
        ram INTEGER,
        sc_h INTEGER,
        sc_w INTEGER,
        talk_time INTEGER,
        three_g INTEGER,
        touch_screen INTEGER,
        wifi INTEGER,
        primary key(id)
        )""")

    #pag write sa table
    with open ('test.csv','r') as file:
        no_records = 0
        for row in file:
            cur.execute("INSERT INTO phoneTable VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",row.split(","))
            no_records += 1
    print ("complete")     
    conn.commit()
    conn.close()
#pag meron nang table  
except sqlite3.OperationalError as err:
    conn = sqlite3.connect('phones.db')
    cur = conn.cursor()

user1 = phoneClass()
user1.start()

