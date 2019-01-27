from tkinter import *
import sqlite3
import pyttsx3

#Connection to database
conn = sqlite3.connect('database.db')
c=conn.cursor()

#Empty list to append later
number = []
patients = []
    
# Window
class Application2:
    
    def __init__(self, master):
        
        self.master = master

        self.x = 0
        #Creating the Frames in the master
        self.left = Frame(master, width=900, height= 800, bg='medium sea green',bd=15,relief="groove")
        self.left.pack(side=LEFT)

        #Heading
        self.heading = Label(master, text="APPOINTMENTS", bg='white', fg='green', font=('consolas 55 bold'),bd=10,relief="groove")
        self.heading.place(x=150,y=20)
  
        #Button to change patients
        self.change = Button(master, text="Next Patient", font=('arail',14,'bold'), width=17, height=1,bd=10,relief="raised", bg='steelblue', command=self.func)
        self.change.place(x=295,y=630)

        #Labels
        self.ides = Label(master, text="ID-->", font=('arial 20 bold'),fg='white', bg='medium sea green')
        self.ides.place(x=18,y=200)
        self.names = Label(master, text="NAME-->", font=('arial 20 bold'),fg='white', bg='medium sea green')
        self.names.place(x=18,y=400)
        
        #Empty text labels to later config
        self.n = Label(master, text="",font=('arial 105 bold'),bg='medium sea green')
        self.n.place(x=135,y=135)

        self.pname = Label(master, text="", font=('arial 75 bold'),bg='medium sea green')
        self.pname.place(x=135,y=357)

        # RETRIVE VALUES FROM DATABASE
        sql = "SELECT * FROM appointments"
        res=c.execute(sql)
        for r in res:
            ids = r[0]
            name = r[1]
            number.append(ids)
            patients.append(name)
            
    #Function to speak the text and update the text
    def func(self):
        
        self.n.config(text=str(number[self.x]))
        self.pname.config(text=str(patients[self.x]))
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        engine.setProperty('rate' ,rate-50)
        engine.say('Patient number ' + str(number[self.x]) + str(patients[self.x]))
        engine.runAndWait()
        self.x +=1
        
            
        

