class Student:
    name = ""
    session = ""
    isDayScholar = None
    EntryTestMarks = None
    HSMarks = None

    def __init__(self,name,session,isDayScholar,EntryTestMarks,HSMarks):
        self.name=name
        self.session=session
        self.isDayScholar=isDayScholar
        self.EntryTestMarks=EntryTestMarks
        self.HSMarks=HSMarks
    
    def __str__(self):
        return f"{self.name},{self.session},{self.isDayScholar},{self.EntryTestMarks},{self.HSMarks}"

    def calculateMerit(self):
        agg = (0.50 * self.EntryTestMarks) + (0.50 * self.HSMarks)
        return agg

class Hostellite(Student): # inherits the properties and methods of Student class
    roomNumber = None
    isFridgeAvailable = None
    isInternetAvailable = None

    def __init__(self, * args):
        super().__init__(*args)
    
    def getHostelFee(self):
        print("Rs.12000")

h1=Hostellite("Faraz", "Fall 2025", True, 300, 1050)
print(h1)
