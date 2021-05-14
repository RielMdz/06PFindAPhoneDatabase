class programMenu(object):
    @staticmethod
    def mainMenu():
        print("|Welcome To PhoneSearch| \n------------------------\n1.Search Using Name \n2.Search Using Specifications\n3.List All\n4.Advance Search \n5.Exit ")
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Invalid input!\n")
       

    @staticmethod 
    def specMenu():
        print("|Search by Specification|\n----------------------\n1.Clock Speed\n2.Dual Sim\n3.Camera\n4.Internal Memory\n5.Number of Cores\n6.Ram\n7.Touch Screen\n8.3G\n9.WIFI")
        try:
            choice = int(input("Enter your Choice: "))
            return choice
        except ValueError:
            print("Invalid Input!\n")
   
    @staticmethod
    def cameraMenu():
        print("|Camera Placement|\n ------------------\n1.Front\n2.Back")
        try: 
            choice = int(input("Camera Placement: "))
            return choice
        except ValueError:
            print ("Invalid Input!\n")

    @staticmethod
    def advancedSearchBattery():
        batterySearch = input("Battery Power: ")
        return batterySearch
    
    @staticmethod
    def advancedSearchBlueT():
        blueSearch = input("Blue Tooth(y/n): ")
        blueSearch = blueSearch.lower()
        if blueSearch == "y":
            bTsearch = 1
        elif blueSearch == "n":
            bTsearch = 0
        else:
            print ("Defult value used!")
            bTsearch = 1 
        return bTsearch
    
    @staticmethod
    def advancedSearchClockS():
        clockSSearch = input("Clock Speed: ")
        return clockSSearch
    
    @staticmethod
    def advancedSearchDualSim():
        dualSearch = input("Dual Sim(y/n): ")
        dualSearch = dualSearch.lower()
        if dualSearch == "y":
            dsearch = 1
        elif dualSearch == "n":
            dsearch = 0
        else:
            print ("Defult value used!")
            dsearch = 1 
        return dsearch
    
    @staticmethod
    def advancedSearchFrontCam():
        fCamSearch = input("Front Camera Quality: ")
        return fCamSearch
    
    @staticmethod
    def advancedSearch4G():
        fgSearch = input("4G(y/n): ")
        fgSearch = fgSearch.lower()
        if fgSearch == "y":
            fgsearch = 1
        elif fgSearch == "n":  
            fgsearch = 0
        else:
            print ("Defult value used!")
            fgsearch = 1 
        return fgsearch

    @staticmethod
    def advancedSearchMemory():
        memSearch = input("Internal Memory in mb: ")
        return memSearch

    
    @staticmethod
    def advancedSearchNCores():
        nCoresSearch = input("Number of cores: ")
        return nCoresSearch
    
    @staticmethod
    def advancedBackCam():
        bCamSearch = input("Back Camera Quality: ")
        return bCamSearch
    
    @staticmethod
    def advancedSearchRam():
        ramSearch = input("RAM in mb: ")
        return ramSearch
    
    @staticmethod
    def advancedSearch3G():
        tgSearch = input("3G(y/n): ")
        tgSearch = tgSearch.lower()
        if tgSearch == "y":
            tgsearch = 1
        elif tgSearch == "n":  
            tgsearch = 0
        else:
            print ("Defult value used!")
            tgsearch = 1 
        return tgsearch
    
    @staticmethod
    def advancedSearchWifi():
        wSearch = input("WIFI(y/n): ")
        wSearch = wSearch.lower()
        if wSearch == "y":
            wsearch = 1
        elif wSearch == "n":  
            wsearch = 0
        else:
            print ("Defult value used!")
            wsearch = 1 
        return wsearch

    @staticmethod
    def advancedSearchTouchScreen():
        tsSearch = input ("Touch Screen(y/n): ")
        tsSearch = tsSearch.lower()
        if tsSearch == "y":
            tssearch = 1
        elif tsSearch == "n":  
            tssearch = 0
        else:
            print ("Defult value used!")
            tssearch = 1 
        return tssearch

