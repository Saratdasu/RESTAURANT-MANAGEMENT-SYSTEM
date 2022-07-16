import sqlite3
import datetime
class Booking:

    def getInfo(self,idNumber):
        self.id=idNumber
        conn=sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("select * from dates WHERE id=?", idNumber)
        info=c.fetchone()
        print("\n\tYOUR INFO\nOwner: %s\nPeople: %s\nDate: %s\nTime: %s" % (str(info[1]),str(info[2]),str(info[3]),str(info[4])))
        conn.close()

    def getInfoBrief(self,idNumber):
        self.id=int(idNumber)
        conn=sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("select * from dates WHERE id=?", str(idNumber))
        info=c.fetchone()
        print("People: %s\tDate: %s\tTime: %s" % (str(info[2]),str(info[3]),str(info[4])))
        conn.close()

    def cancel(self):
        conn=sqlite3.connect("database.db")
        c = conn.cursor()
        sure=str(input("Are you sure to cancel[Y/N]: "))
        if sure=="Y":
            c.execute("delete from dates WHERE id=?", self.id)
            conn.commit()
            print("The booking was deleted.")
        else:
            print("The cancellation was stopped.")
        conn.close()


    def setDate(self,dateOfParameter):
        self.dateOf=dateOfParameter

    def setTime(self,timeOfParameter):
        self.timeOf=timeOfParameter

    def setPeople(self,numberOfPeopleParameter):
        self.numberOfPeople=numberOfPeopleParameter

    def setOwner(self,ownerParameter):
        self.owner=ownerParameter

    def saveToDB(self):
        conn=sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute('insert into dates(owner,howmanypeople,dateof,timeof) values(?,?,?,?)', [self.owner,self.numberOfPeople,self.dateOf,self.timeOf])
        conn.commit()
        return c.lastrowid
        conn.close()

def newBooking():
    aBooking=Booking()

    dateRaw=input("Select a date(dd-mm-yyyy): ")
    dateProcessed=datetime.datetime.strptime(dateRaw, '%d-%m-%Y')
    aBooking.setDate(dateProcessed)

    ownerRaw=str(input("Owner name: "))
    aBooking.setOwner(ownerRaw)

    numberOfPeople=input("Number of people(3,4,5 etc): ")
    aBooking.setPeople(numberOfPeople)

    timeRaw=input("Select a time: ")
    aBooking.setTime(timeRaw)

    bookingID=aBooking.saveToDB()
    print("\n\tYour booking ID is: %s, please note for other proceess like cancelation.\t" % str(bookingID))

def deleteBooking():
    idRaw=input("Please type your booking ID number: ")
    aBooking=Booking()
    aBooking.getInfo(idRaw)
    aBooking.cancel()

def bookingStatus():
    dateRaw=input("Select a date(dd-mm-yyyy): ")
    dateProcessed=datetime.datetime.strptime(dateRaw, '%d-%m-%Y')

    conn=sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("select * from dates WHERE dateOf=(?)", (str(dateProcessed),))
    info=c.fetchall()
    print("STATUS OF the DAY:\n")
    for booking in info:
        aBooking=Booking()
        aBooking.getInfoBrief(booking[0])
    input("Enter a key to continue...")

    conn.close()  
    
    
import sys


def prepareDB():
    try:
        conn=sqlite3.connect("database.db")
        c = conn.cursor()
        print("Database connection is successfull.")

        c.execute('''CREATE TABLE IF NOT EXISTS dates
         (id INTEGER PRIMARY KEY AUTOINCREMENT,
         owner TEXT NOT NULL,
         howmanypeople INT NOT NULL,
         dateof DATE NOT NULL,
         timeof INT NOT NULL);''')

        print("Table checking is ok.")
        print("\n---\n")
        conn.commit()
        conn.close()
    except:
        print("Hata")
        raise


def whishChoosing():
    print("\nPLEASE MAKE A CHOICE:")
    print("[1] New booking\n[2] Delete booking\n[3] Check the status for a day\n[4] Exit")
    try:
        choice = int(input("YOUR CHOICE: "))
        return choice
    except:
        print("Please, just type a number from 1 to 3.")
        whishChoosing()

def processChoosing(choosingParameter):
    if choosingParameter==1:
        newBooking()
    elif choosingParameter==2:
        deleteBooking()
    elif choosingParameter==3:
        bookingStatus()
    elif choosingParameter==4:
        sys.exit()


prepareDB()

currentDT=datetime.datetime.now().strftime("%d-%m-%Y")
print ("Today: %s\nYou should select a date in the next 10 days." % str(currentDT))

while 1:
    choosing=whishChoosing()
    processChoosing(choosing)   
    

class Booking:

    def getInfo(self,idNumber):
        self.id=idNumber
        conn=sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("select * from dates WHERE id=?", idNumber)
        info=c.fetchone()
        print("\n\tYOUR INFO\nOwner: %s\nPeople: %s\nDate: %s\nTime: %s" % (str(info[1]),str(info[2]),str(info[3]),str(info[4])))
        conn.close()

    def getInfoBrief(self,idNumber):
        self.id=int(idNumber)
        conn=sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("select * from dates WHERE id=?", str(idNumber))
        info=c.fetchone()
        print("People: %s\tDate: %s\tTime: %s" % (str(info[2]),str(info[3]),str(info[4])))
        conn.close()

    def cancel(self):
        conn=sqlite3.connect("database.db")
        c = conn.cursor()
        sure=str(input("Are you sure to cancel[Y/N]: "))
        if sure=="Y":
            c.execute("delete from dates WHERE id=?", self.id)
            conn.commit()
            print("The booking was deleted.")
        else:
            print("The cancellation was stopped.")
        conn.close()


    def setDate(self,dateOfParameter):
        self.dateOf=dateOfParameter

    def setTime(self,timeOfParameter):
        self.timeOf=timeOfParameter

    def setPeople(self,numberOfPeopleParameter):
        self.numberOfPeople=numberOfPeopleParameter

    def setOwner(self,ownerParameter):
        self.owner=ownerParameter

    def saveToDB(self):
        conn=sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute('insert into dates(owner,howmanypeople,dateof,timeof) values(?,?,?,?)', [self.owner,self.numberOfPeople,self.dateOf,self.timeOf])
        conn.commit()
        return c.lastrowid
        conn.close()

def newBooking():
    aBooking=Booking()

    dateRaw=input("Select a date(dd-mm-yyyy): ")
    dateProcessed=datetime.datetime.strptime(dateRaw, '%d-%m-%Y')
    aBooking.setDate(dateProcessed)

    ownerRaw=str(input("Owner name: "))
    aBooking.setOwner(ownerRaw)

    numberOfPeople=input("Number of people(3,4,5 etc): ")
    aBooking.setPeople(numberOfPeople)

    timeRaw=input("Select a time: ")
    aBooking.setTime(timeRaw)

    bookingID=aBooking.saveToDB()
    print("\n\tYour booking ID is: %s, please note for other proceess like cancellation.\t" % str(bookingID))

def deleteBooking():
    idRaw=input("Please type your booking ID number: ")
    aBooking=Booking()
    aBooking.getInfo(idRaw)
    aBooking.cancel()

def bookingStatus():
    dateRaw=input("Select a date(dd-mm-yyyy): ")
    dateProcessed=datetime.datetime.strptime(dateRaw, '%d-%m-%Y')

    conn=sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("select * from dates WHERE dateOf=(?)", (str(dateProcessed),))
    info=c.fetchall()
    print("STATUS OF the DAY:\n")
    for booking in info:
        aBooking=Booking()
        aBooking.getInfoBrief(booking[0])
    input("Enter a key to continue...")

    conn.close()
