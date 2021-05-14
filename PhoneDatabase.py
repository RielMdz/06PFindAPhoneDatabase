import sqlite3,csv
import pandas as pd
from menu import programMenu

class phoneClass(object):
    def _init_(self,userName):
        self.name = ''
        self.out = ''

    def start (self):
        userChoice = programMenu.mainMenu()
        while userChoice != 5 :
            if userChoice == 1:
                self.searchID()
            elif userChoice == 2:
                self.searchBySpecs()  
            elif userChoice == 3:
                self.listAll()
            elif userChoice == 4:
                self.advanceSearch()
                
            userChoice = programMenu.mainMenu()

    def searchBySpecs(self):
        userInput = programMenu.specMenu()
        if userInput == 1:
            self.searchClockSpeed()
        elif userInput == 2:
            self.searchDualSim()
        elif userInput == 3:
            self.FoBCam()
        elif userInput == 4:
            self.searchInternalMemory()
        elif userInput == 5:
            self.searchNumberCores()
        elif userInput == 6:
            self.searchRam()
        elif userInput == 7:
            self.searchTouchScreen()
        elif userInput == 8:
            self.searchThreeG()
        elif userInput == 9:
            self.searchWifi()
        return

    def FoBCam(self):
        userInput = programMenu.cameraMenu()
        if userInput == 1:
            self.searchFrontCam()
        elif userInput == 2:
            self.searchPrimaryCam()

    def listAll(self):
        cur.execute("SELECT * FROM phoneTable")
        result = cur.fetchall()
        dl1 = pd.read_sql_query("SELECT * FROM phoneTable",conn)
        print(dl1)
   

    def searchID(self):
        searchId = input("ID of Phone: ")
        dl1 = pd.read_sql_query("SELECT * FROM phoneTable WHERE id = '{}'".format(searchId),conn)
        print (dl1)
    

    
    def searchDualSim(self):
        searchDS = input("\tDual Sim?(Y/N) ")
        searchDS = searchDS.lower()
        if searchDS == "y":
            dl1 = pd.read_sql_query("SELECT * FROM phoneTable WHERE dual_sim = '1'",conn)
            print (dl1)
        elif searchDS =="n":
            dl1 = pd.read_sql_query("SELECT * FROM phoneTable WHERE dual_sim = '0'",conn)
            print (dl1)
        else:
            print("Wrong input")
     
    def searchClockSpeed(self):
        searchCS =input ("Clock speed required: ")
        dl1 = pd.read_sql_query("SELECT * FROM phoneTable WHERE clock_speed = '{}'".format(searchCS),conn)
        print(dl1)

    def searchFrontCam(self):
        searchFC = input ("Front Camera Resolution in megapixels: ")
        dl1 = pd.read_sql_query("SELECT * FROM phoneTable WHERE fc = '{}'".format(searchFC),conn)
        print(dl1)
    
    def searchInternalMemory(self):
        searchIM = input ("Required phone memory in GB: ")
        dl1 = pd.read_sql_query("SELECT * FROM phoneTable WHERE int_memory = '{}'".format(searchIM),conn)
        print(dl1)

    
    def searchNumberCores(self):
        searchNC = input ("Number of Cores: ")
        dl1 = pd.read_sql_query("SELECT * FROM phoneTable WHERE n_cores = '{}'".format(searchNC),conn)
        print(dl1)

    def searchPrimaryCam(self):
        searchPC = input ("Back Camera Resolution in megapixels: ")
        dl1 = pd.read_sql_query("SELECT * FROM phoneTable WHERE pc = '{}'".format(searchPC),conn)
        print(dl1)
    
    def searchRam(self):
        searchR = input ("Amount of ram in mb: ")
        dl1 = pd.read_sql_query("SELECT * FROM phoneTable WHERE ram = '{}'".format(searchR),conn)
        print (dl1)
    
    def searchTouchScreen(self):
        searchTS = input ("Touch screen? (Y/N)")
        searchTS = searchTS.lower()
        if searchTS == "y":
            dl1 = pd.read_sql_query("SELECT * FROM phoneTable WHERE touch_screen = '1'",conn)
            print(dl1)
        elif searchTS =="n":
            dl1 = pd.read_sql_query("SELECT * FROM phoneTable WHERE touch_screen = '0'",conn)
            print(dl1)
        else:
            print("Wrong input")

    def searchThreeG(self):
        search3G = input ("Phone with 3G? (y/n): ")
        search3G = search3G.lower()
        if search3G == "y":
            dl1 = pd.read_sql_query("SELECT * FROM phoneTable WHERE three_g = '1'",conn)
            print(dl1)
        elif search3G == "n":
            dl1 = pd.read_sql_query("SELECT * FROM phoneTable WHERE three_g = '0'",conn)
            print(dl1)
        else:
            print("Wrong input")

    def searchWifi(self):
        searchW = input("Phone with Wifi? (y/n): ")
        searchW = searchW.lower()
        if searchW == "y":
            dl1 = pd.read_sql_query("SELECT * FROM phoneTable WHERE wifi = '1'",conn)
            print(dl1)
        elif searchW =="n":
            dl1 = pd.read_sql_query("SELECT * FROM phoneTable WHERE wifi = '0'",conn)
            print(dl1)
        else:
            print("Wrong input")
    
    def advanceSearch(self):
        print("Advanced Search\n---------------\nDo not leave a blank\n")
        battery = programMenu.advancedSearchBattery()
        bT = programMenu.advancedSearchBlueT()
        clockS = programMenu.advancedSearchClockS()
        dualS = programMenu.advancedSearchDualSim()
        frontC = programMenu.advancedSearchFrontCam()
        backC = programMenu.advancedBackCam()
        fG = programMenu.advancedSearch4G()
        memory = programMenu.advancedSearchMemory()
        cores = programMenu.advancedSearchNCores()
        nRam = programMenu.advancedSearchRam()
        tG = programMenu.advancedSearch3G()
        pwifi = programMenu.advancedSearchWifi()
        touchS = programMenu.advancedSearchTouchScreen()
        dl1 = pd.read_sql_query("SELECT * FROM phoneTable WHERE battery_power = '{}' AND blue = '{}' AND clock_speed = '{}' AND dual_sim = '{}' AND fc = '{}' AND four_g = '{}' AND int_memory = '{}' AND n_cores = '{}' AND pc = '{}' AND ram = '{}'AND three_g = '{}' AND wifi = '{}'AND touch_screen = '{}'".format(battery,bT,clockS,dualS,frontC,fG,memory,cores,backC,nRam,tG,pwifi,touchS),conn)
        print (dl1)
    
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
        wifi INTEGER
    )""")

    #pag write sa table
    with open ('test.csv','r') as file:
        no_records = 0
        for row in file:
            cur.execute("INSERT INTO phoneTable VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",row.split(","))
            no_records += 1
    print ("complete")     
    conn.commit()
#pag meron nang table  
except sqlite3.OperationalError as err:
    conn = sqlite3.connect('phones.db')
    cur = conn.cursor()

user1 = phoneClass()
user1.start()
conn.close()

