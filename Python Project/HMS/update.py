# Update the appointments
from tkinter import *
import tkinter.messagebox
import sqlite3

#Connect to database
conn = sqlite3.connect('database.db')

#Cursor to move around the database
c = conn.cursor()

class Application1:
    def __init__(self, master):
        self.master = master

        #Creating the Frames in the master
        self.left = Frame(master, width=800, height=720, bg='medium sea green',bd=15,relief="groove")
        self.left.pack(side=LEFT)
        

        #Heading label
        self.heading = Label(master, text=" UPDATE APPOINTMENTS ", font=('consolas 35 bold'),fg='green', bg='white',bd=10,relief="groove")
        self.heading.place(x=114,y=18)

        # Search criteria --> name
        self.name = Label(master, text = "Enter Patient's Name",fg='white',bg='medium sea green', font=('arial 18 bold'))
        self.name.place(x=18,y=110)

        #Entry for the Name
        self.namenet = Entry(master, width=20,font=('arail',14,'bold'),bg="lemonchiffon",bd=7)
        self.namenet.place(x=460,y=110)

        #Search button
        self.search = Button(master, text="Search", font=('arail',14,'bold'), width=17,height=1,bg='lightpink', bd=10,command=self.search_db)
        self.search.place(x=460,y=165)

    #Function to search
    def search_db(self):
        self.input = self.namenet.get()

        #Execute sql
        sql = "SELECT * FROM appointments WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.phone = self.row[5]
            self.time = self.row[6]
            
        #Creating the update form
        self.uname = Label(self.master, text="Patient's Name",fg='white',bg='medium sea green', font=('arial 18 bold'))
        self.uname.place(x=18, y=240)
        
        self.uage = Label(self.master, text="Age",fg='white',bg='medium sea green', font=('arial 18 bold'))
        self.uage.place(x=18, y=310)

        self.ugender = Label(self.master, text="Gender",fg='white',bg='medium sea green', font=('arial 18 bold'))
        self.ugender.place(x=18, y=380)

        self.ulocation = Label(self.master, text="Location",fg='white',bg='medium sea green', font=('arial 18 bold'))
        self.ulocation.place(x=18, y=450)

        self.utime = Label(self.master, text="Appointment Time",fg='white',bg='medium sea green', font=('arial 18 bold'))
        self.utime.place(x=18, y=520)

        self.uphone = Label(self.master, text="Phone Number",fg='white',bg='medium sea green', font=('arial 18 bold'))
        self.uphone.place(x=18, y=590)


        #Enteries for each Label======================================

        #==============Filling the search result in the entry box to update==========
        self.ent1 = Entry(self.master, font=('arail',14,'bold'),bg="lemonchiffon",bd=7 , width=20)
        self.ent1.place(x=460,y=240)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = Entry(self.master, font=('arail',14,'bold'),bg="lemonchiffon",bd=7 ,  width=20)
        self.ent2.place(x=460,y=310)
        self.ent2.insert(END, str(self.age))
        
        self.ent3 = Entry(self.master, font=('arail',14,'bold'),bg="lemonchiffon",bd=7 ,  width=20)
        self.ent3.place(x=460,y=380)
        self.ent3.insert(END, str(self.gender))
        
        self.ent4 = Entry(self.master, font=('arail',14,'bold'),bg="lemonchiffon",bd=7 ,  width=20)
        self.ent4.place(x=460,y=450)
        self.ent4.insert(END, str(self.location))

        self.ent5 = Entry(self.master, font=('arail',14,'bold'),bg="lemonchiffon",bd=7 ,  width=20)
        self.ent5.place(x=460,y=520)
        self.ent5.insert(END, str(self.time))

        self.ent6 = Entry(self.master, font=('arail',14,'bold'),bg="lemonchiffon",bd=7 ,  width=20)
        self.ent6.place(x=460,y=590)
        self.ent6.insert(END, str(self.phone))

        #Button to execute update
        self.update = Button(self.master, text="Update", font=('arail',14,'bold'), width=17,height=1,bg='green', bd=10,command=self.update_db)
        self.update.place(x=431,y=639)

        #Button to delete
        self.delete = Button(self.master, text="Delete", font=('arail',14,'bold'), width=17, height=1,bg='red',bd=10,command=self.delete_db)
        self.delete.place(x=146,y=639)
        
        
    def update_db(self):
        #Declaring the variable to update
        self.var1 = self.ent1.get()#Updated name
        self.var2 = self.ent2.get()#Updated age
        self.var3 = self.ent3.get()#Updated gender        
        self.var4 = self.ent4.get()#Updated location
        self.var5 = self.ent5.get()#Updated time
        self.var6 = self.ent6.get()#Updated phone
        #Updating the Database
        query = " UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?, scheduled_time=? WHERE name LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var6, self.var5, self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("UPDATED", "Successfully Updated.")

    def delete_db(self):
        #Deleting the appointment
        sql2 = " DELETE FROM appointments WHERE name LIKE ? "
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("SUCCESS", "Deleted Sucessfully")
        self.ent1.destroy()                            
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()
        
        

                                                                                         
                                                                                         
