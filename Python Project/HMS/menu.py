#Import Modules
from tkinter import *
from appointment import *
from update import *
from display import *

#creating object of Application  
def appointment1():
        
        root = Tk()  
        c = Application(root)
        root.geometry("1200x720+80+0")
        root.resizable(False, False)
        root.mainloop()

#creating object of Application1        
def update1():
        
        root = Tk()
        root.geometry("800x720+80+0")
        b = Application1(root)
        root.resizable(False, False)
        root.mainloop()
        
#creating object of Application2       
def display1():
        
        root = Tk()  
        a = Application2(root)
        root.geometry("800x720+80+0")
        root.resizable(False, False)
        root.mainloop()


           
root = Tk()
root.geometry("600x400+390+150")

#title of the Window
root.title("Hospital Management System")
f1=Frame(root, width=600,height=400,bg='lightblue')
f1.pack()

#inserting a photo in tkinter window
photo = PhotoImage(file = "host.png")
background_label = Label(f1, image=photo)
background_label.place(x=0, y=0 )

ttl=Label(f1,text='   CITY HOSPITAL   ',fg="deepskyblue4",bg='skyblue1',font=('consolas',25,'bold'),bd=10,relief="groove")
ttl.place(x=125,y=10)
submit2 = Button(f1,padx=6,pady=6,text="Add Appointment",font=('arial',9,'bold'), width=16,height=1,fg="gray99", bg='hotpink2',bd=6,relief="raise",command = appointment1)
submit2.place(x=82,y=300)
submit1 = Button(f1, padx=6,pady=6,text="Update",font=('arial',9,'bold'), width=16, height=1,fg="gray99",bg='deepskyblue',bd=6,relief="raise",command = update1)
submit1.place(x=232,y=300)
submit3 = Button(f1, padx=6,pady=6,text="Display",font=('arial',9,'bold'), width=16, height=1,fg="gray98",bg='seagreen2',bd=6,relief="raise", command =display1)
submit3.place(x=382,y=300)
root.resizable(False, False)
root.mainloop()
