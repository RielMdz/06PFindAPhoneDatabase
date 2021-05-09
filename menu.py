class programMenu(object):
    @staticmethod
    def mainMenu():
        print("|Welcome To PhoneSearch| \n------------------------\n1.See Full List \n2.Search Using Name \n3.Search Using Specifications\n4.Search by Use\n5.Exit ")
        choice = int(input("Enter your choice: "))
        return choice

    @staticmethod 
    def specMenu():
        print("|Search by Specification|\n----------------------\n1.Clock Speed\n2.Dual Sim\n3.Camera\n4.Internal Memory\n5.Number of Cores\n6.Ram")
        choice = int(input("Enter your Choice: "))
        return choice
   