from tkinter import*
import tkinter as tk


root=tk.Tk()
root.geometry('500x200')
root.title("Home Page")
label_0 = Label(root, text="Solent Trips management system welcomes you!",fg='Blue',width=50,font=("bold", 10))
label_0.place(x=35,y=50)

def Coordinator():
   exec(open("coord.py").read())
def Manager():
   exec(open("Manager_.py").read())
def Admin():
   exec(open("Admin_.py").read())

Button(root, text='Co-ordinator',width=10,bg='Red',fg='white',command=Coordinator).place(x=100,y=100)
Button(root, text='Manager',width=10,bg='Green',fg='white',command=Manager).place(x=200,y=100)
Button(root, text='Admin',width=10,bg='Blue',fg='white',command=Admin).place(x=300,y=100)




root.mainloop()
