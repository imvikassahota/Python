# import  modules
from tkinter import *
import sqlite3
import tkinter.messagebox

# connect to the database
conn =sqlite3.connect('database.db')

#cursor to move around the database
c=conn.cursor()

#Empty list to later append the ids from the database
ids = []

# tkinter window
class Application:
    def __init__(self, master):
        self.master = master
        
        #Creating the Frames in the master
        self.left = Frame(master, width=800, height=720, bg='medium sea green',bd=15,relief="groove")
        self.left.pack(side=LEFT)
        

        self.right = Frame(master, width=400, height=720, bg='steelblue3',bd=15,relief="groove")
        self.right.pack(side=RIGHT)

        
        #Label for the window
        self.heading = Label(self.left, text="  ADD APPOINTMENT  ", font=('consolas 35 bold'),fg='green', bg='white',bd=10,relief="groove")
        self.heading.place(x=140,y=8)
   
        #Patient's Name       
        self.name = Label(self.left, text="Patient's Name",font=('arial 18 bold'), fg='white',bg='medium sea green')
        self.name.place(x=2,y=120)

        #Patient's Age       
        self.age = Label(self.left, text="Age",font=('arial 18 bold'), fg='white',bg='medium sea green')
        self.age.place(x=2,y=200)

        #Patient's Gender        
        self.gender = Label(self.left, text="Gender",font=('arial 18 bold'), fg='white',bg='medium sea green')
        self.gender.place(x=2,y=280)

        #Location       
        self.location = Label(self.left, text="Location",font=('arial 18 bold'), fg='white',bg='medium sea green')
        self.location.place(x=2,y=360)

        #Appointment time       
        self.time = Label(self.left, text="Appointment time",font=('arial 18 bold'), fg='white',bg='medium sea green')
        self.time.place(x=2,y=440)

        #Phone       
        self.phone = Label(self.left, text="Phone Number",font=('arial 18 bold'), fg='white',bg='medium sea green')
        self.phone.place(x=2,y=520)


        #Enteries for all Labels==========================================================
        self.name_ent = Entry(self.left, font=('arail',14,'bold'),bg="lemonchiffon",bd=7 ,width=20)
        self.name_ent.place(x=300,y=125)
        
        self.age_ent = Entry(self.left, font=('arail',14,'bold'),bg="lemonchiffon",bd=7 ,width=20)
        self.age_ent.place(x=300,y=205)
        
        self.gender_ent = Entry(self.left, font=('arail',14,'bold'),bg="lemonchiffon",bd=7 ,width=20)
        self.gender_ent.place(x=300,y=285)

        self.location_ent = Entry(self.left, font=('arail',14,'bold'),bg="lemonchiffon",bd=7 ,width=20)
        self.location_ent.place(x=300,y=365)

        self.time_ent = Entry(self.left, font=('arail',14,'bold'),bg="lemonchiffon",bd=7, width=20)
        self.time_ent.place(x=300,y=445)


        self.phone_ent = Entry(self.left, font=('arail',14,'bold'),bg="lemonchiffon",bd=7 ,width=20)
        self.phone_ent.place(x=300,y=525)
        

        #Button to perform a command
        self.submit = Button(self.left, text="ADD",padx=1,pady=1,font=('arail',12,'bold'), width=20, height=2, fg="white",bg='slateblue2',bd=10,relief="raise",command = self.add_appointment)
        self.submit.place(x=300,y=590)

        #Getting the Number of appointment fixed to view in the log
        sql2 = "SELECT ID FROM appointments "
        self.result = c.execute(sql2)
        for self.row in self.result:
                self.id= self.row[0]
                ids.append(self.id)
       
        #Odering the ids
        self.new = sorted(ids)
        self.final_id = len(ids)
        
        #Displaying the logs in our right frame
        self.logs = Label(self.right, text="Logs", font=('arial 28 bold'), fg='black', bg= 'white',bd=8,relief="raise")
        self.logs.place(x=150,y=5)
        self.box = Text(self.right, width=44, height=38)
        self.box.place(x=6,y=65)
        self.box.insert(END,"Total Appointments till now :" + str(self.final_id) + "\n" +"\n"  )

    #Function to call when the submit button is clicked
    def add_appointment(self):
        #Getting the user inputs
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()

        #Testing the user input
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 =='' or self.val5 == '' or self.val6 == '':
            tkinter.messagebox.showinfo("WARNING!", "Please Fill Up All Boxes")
                                                   
        else:
            # Now  we add to the database
            sql = "INSERT INTO 'appointments' (name,age,gender,location,phone,scheduled_time) VALUES(?,?,?,?,?,?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val6, self.val5))
            conn.commit()
            tkinter.messagebox.showinfo("SUCCESS*","Appointment for " +str(self.val1)+ " has been created")

            self.box.insert(END, 'Appointment fixed for: ' + str(self.val1) + ' at ' + str(self.val5)+"\n"+"\n") 
            
                

              

        
        
