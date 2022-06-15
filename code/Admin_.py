from tkinter import*
import tkinter as tk
from csv import writer
from pprint import pprint
import csv
from tkinter import messagebox
from datetime import datetime
import os
class Admin:
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry('1500x700')
        self.root.title("Admin Page")
        self.label_0 = Label(self.root, text="Solent Trips management system",fg='Blue',width=50,font=("bold", 30))
        self.label_0.place(x=250,y=50)
        
        self.label_1 = Label(self.root, text="Enter Trip Details",width=50,font=("bold", 16))
        self.label_1.place(x=180,y=200)
        
        self.label_11 = Label(self.root, text="Enter Traveller Details",width=50,font=("bold", 16))
        self.label_11.place(x=680,y=200)
        
        self.label_pay = Label(self.root, text="Enter Payment Details",width=20,font=("bold", 16))
        self.label_pay.place(x=1180,y=200)
        
        
        self.e1=tk.StringVar()
        self.e2=tk.StringVar()
        self.e3=tk.StringVar()
        self.e4=tk.StringVar()
        self.e5=tk.StringVar()
        self.e6=tk.StringVar()
        self.e7=tk.StringVar()
        self.e8=tk.StringVar()
        self.e9=tk.StringVar()
        self.e10=tk.StringVar()
        self.e11=tk.StringVar()
        self.e12=tk.StringVar()
        self.ee7=tk.StringVar()
        self.ee8=tk.StringVar()
        self.ee9=tk.StringVar()
        self.ee10=tk.StringVar()
        self.ee11=tk.StringVar()
        self.ee12=tk.StringVar()
        
        self.ei1=tk.StringVar()
        self.ei2=tk.StringVar()
        self.ei3=tk.StringVar()
        self.ei4=tk.StringVar()
        self.e15=tk.StringVar()
        self.btn1=tk.Button(self.root, text='Generate Invoice',width=20,bg='brown',fg='white',command =self.Generate_invoice).place(x=1200,y=450)
        self.btn2=tk.Button(self.root, text='Print Invoice',width=20,bg='brown',fg='white',command = self.Print_invoice).place(x=1200,y=500)
        
        
        #TRIP DETAILS
        
        
        self.label_2 = Label(self.root, text="Trip Name:",width=20,font=("bold", 10))
        self.label_2.place(x=200,y=250)
        self.entry_2 = tk.Entry(self.root,textvariable = self.e1, font=('calibre',10,'normal'))
        self.entry_2.place(x=330,y=250)
        self.label_3 = Label(self.root, text="Start Date:",width=20,font=("bold", 10))
        self.label_3.place(x=200,y=300)
        self.entry_3 = tk.Entry(self.root,textvariable = self.e2, font=('calibre',10,'normal'))
        self.entry_3.place(x=330,y=300)
        self.label_4 = Label(self.root, text="No of Travellers:",width=20,font=("bold", 10))
        self.label_4.place(x=200,y=350)
        self.entry_4 = tk.Entry(self.root,textvariable = self.e3, font=('calibre',10,'normal'))
        self.entry_4.place(x=330,y=350)
        self.label_5 = Label(self.root, text="support staffs:",width=20,font=("bold", 10))
        self.label_5.place(x=200,y=400)
        self.entry_5 = tk.Entry(self.root,textvariable = self.e4, font=('calibre',10,'normal'))
        self.entry_5.place(x=330,y=400)
        self.label_6 = Label(self.root, text="Trip Duration:",width=20,font=("bold", 10))
        self.label_6.place(x=200,y=450)
        self.entry_6 = tk.Entry(self.root,textvariable = self.e5, font=('calibre',10,'normal'))
        self.entry_6.place(x=330,y=450)
        self.label_7 = Label(self.root, text="Co-ordinator:",width=20,font=("bold", 10))
        self.label_7.place(x=200,y=500)
        self.entry_7 = tk.Entry(self.root,textvariable = self.e6, font=('calibre',10,'normal'))
        self.entry_7.place(x=330,y=500)
        
        #TRIP LEGS DETAILS
        self.label_8 = Label(self.root, text="Start Location:",width=20,font=("bold", 10))
        self.label_8.place(x=500,y=250)
        self.entry_8 = tk.Entry(self.root,textvariable = self.e7, font=('calibre',10,'normal'))
        self.entry_8.place(x=630,y=250)
        self.label_9 = Label(self.root, text="Destination:",width=20,font=("bold", 10))
        self.label_9.place(x=500,y=300)
        self.entry_9 = tk.Entry(self.root,textvariable = self.e8, font=('calibre',10,'normal'))
        self.entry_9.place(x=630,y=300)
        self.label_10 = Label(self.root, text="Place to stay:",width=20,font=("bold", 10))
        self.label_10.place(x=500,y=350)
        self.entry_10 = tk.Entry(self.root,textvariable = self.e9, font=('calibre',10,'normal'))
        self.entry_10.place(x=630,y=350)
        self.label_11 = Label(self.root, text="Need Food:",width=20,font=("bold", 10))
        self.label_11.place(x=500,y=400)
        self.entry_11 = tk.Entry(self.root,textvariable = self.e10, font=('calibre',10,'normal'))
        self.entry_11.place(x=630,y=400)
        self.label_12 = Label(self.root, text="Interest area:",width=20,font=("bold", 10))
        self.label_12.place(x=500,y=450)
        self.entry_12 = tk.Entry(self.root,textvariable = self.e11, font=('calibre',10,'normal'))
        self.entry_12.place(x=630,y=450)
        self.label_13 = Label(self.root, text="Mode of transport:",width=20,font=("bold", 10))
        self.label_13.place(x=500,y=500)
        self.entry_13 = tk.Entry(self.root,textvariable = self.e12, font=('calibre',10,'normal'))
        self.entry_13.place(x=630,y=500)
        self.btn3=tk.Button(self.root, text='Add Trip',width=20,bg='brown',fg='white',command = self.submit).place(x=425,y=550)
        
        #Traveller DETAILS
        self.label_18 = Label(self.root, text="Name:",width=20,font=("bold", 10))
        self.label_18.place(x=800,y=250)
        self.entry_18 = tk.Entry(self.root,textvariable = self.ee7, font=('calibre',10,'normal'))
        self.entry_18.place(x=930,y=250)
        self.label_19 = Label(self.root, text="Address:",width=20,font=("bold", 10))
        self.label_19.place(x=800,y=300)
        self.entry_19 = tk.Entry(self.root,textvariable = self.ee8, font=('calibre',10,'normal'))
        self.entry_19.place(x=930,y=300)
        self.label_110 = Label(self.root, text="Contact:",width=20,font=("bold", 10))
        self.label_110.place(x=800,y=350)
        self.entry_110 = tk.Entry(self.root,textvariable = self.ee9, font=('calibre',10,'normal'))
        self.entry_110.place(x=930,y=350)
        self.label_111 = Label(self.root, text="Emergency Contact:",width=20,font=("bold", 10))
        self.label_111.place(x=800,y=400)
        self.entry_111 = tk.Entry(self.root,textvariable = self.ee10, font=('calibre',10,'normal'))
        self.entry_111.place(x=930,y=400)
        self.label_112 = Label(self.root, text="Valid Govt ID:",width=20,font=("bold", 10))
        self.label_112.place(x=800,y=450)
        self.entry_112 = tk.Entry(self.root,textvariable = self.ee11, font=('calibre',10,'normal'))
        self.entry_112.place(x=930,y=450)
        self.btn4=tk.Button(self.root, text='Add Traveller',width=20,bg='brown',fg='white',command = self.traveller).place(x=900,y=500)
        
        #Generate Invoice
        self.label_01 = Label(self.root, text="ID:",width=20,font=("bold", 10))
        self.label_01.place(x=1100,y=250)
        self.entry_01 = tk.Entry(self.root,textvariable = self.ei1, font=('calibre',10,'normal'))
        self.entry_01.place(x=1230,y=250)
        #Generate Invoice
        self.label_02 = Label(self.root, text="Amount in $:",width=20,font=("bold", 10))
        self.label_02.place(x=1100,y=300)
        self.entry_02 = tk.Entry(self.root,textvariable = self.ei2, font=('calibre',10,'normal'))
        self.entry_02.place(x=1230,y=300)
        #Generate Invoice
        self.label_03 = Label(self.root, text="Name of Payee:",width=20,font=("bold", 10))
        self.label_03.place(x=1100,y=350)
        self.entry_03 = tk.Entry(self.root,textvariable = self.ei3, font=('calibre',10,'normal'))
        self.entry_03.place(x=1230,y=350)
        #Generate Invoice
        self.label_04 = Label(self.root, text="Mode of Payment:",width=18,font=("bold", 10))
        self.label_04.place(x=1100,y=400)
        self.entry_04 = tk.Entry(self.root,textvariable = self.ei4, font=('calibre',10,'normal'))
        self.entry_04.place(x=1230,y=400)
        self.label_trip = Label(self.root, text="Enter Trip Name to Delete:",font=("bold", 10))
        self.label_trip.place(x=1050,y=150)
        self.entry_trip = tk.Entry(self.root,textvariable = self.e15, font=('calibre',10,'normal'))
        self.entry_trip.place(x=1250,y=150)

        self.btn5=tk.Button(self.root, text='Delete Trips Manager',width=20,bg='Green',fg='Black',command = self.del_trip_m).place(x=100,y=150)
        #Button(root, text='Delete Trips Co-ordinator',width=30,bg='Green',fg='Black',command = del_trip_co).place(x=900,y=150)
        self.btn6=tk.Button(self.root, text='Delete Trips Invoice',width=20,bg='Yellow',fg='Black',command = self.del_invoices).place(x=450,y=150)
        self.btn7=tk.Button(self.root, text='View all Invoices',width=30,bg='Red',fg='Black',command = self.view_invoice).place(x=600,y=150)
        self.btn8=tk.Button(self.root, text='Delete Trips coordinator',width=30,bg='Green',fg='Black',command = self.del_trip_co).place(x=250,y=150)
        self.btn9=tk.Button(self.root, text='Delete Trips',width=30,bg='Yellow',fg='Black',command = self.del_trips).place(x=800,y=150)     
                
        
        self.root.mainloop()




    def submit(self):
        print("hai")
        Lis=[self.e1.get(),self.e2.get(),int(self.e3.get()),int(self.e4.get()),int(self.e5.get()),self.e6.get(),self.e7.get(),self.e8.get(),self.e9.get(),self.e10.get(),self.e11.get(),self.e12.get()]
       
        with open('tripsAdmin.csv', 'a') as f_object:
      
            writer_object = writer(f_object)
          
            
            writer_object.writerow(Lis)
          
            
            f_object.close()
    def traveller(self):
        tripname=self.e1.get()
        Lis=[self.ee7.get(),self.ee8.get(),self.ee9.get(),self.ee10.get(),self.ee11.get()]
        #print(Lis)
        fname=tripname+'.csv'
        with open(fname, 'a') as f_object:
      
            
            writer_object = writer(f_object)
          
            
            writer_object.writerow(Lis)
          
            f_object.close()
    def Generate_invoice(self):
     
        today = datetime.today()
    
        Lis=[self.ei1.get(),today,self.e1.get(),self.ei2.get(),self.ei3.get(),self.ei4.get()]
        with open('AdminInvoice.csv', 'a') as f_object:
     
            writer_object = writer(f_object)
          
            writer_object.writerow(Lis)
          
            f_object.close()
    def Print_invoice(self):
        today = datetime.today()
        dic={"ID":self.ei1.get(),"Trip Name":self.e1.get(),"Date & Time":today,"Amount":self.ei2.get(),"Payee Name":self.ei3.get(),"Payment Mode":self.ei4.get()}
        pprint(dic)
    def del_trip_co(self):
        os.remove("tripscoordinator.csv")
    def del_trips(self):
        file=self.e15.get()+'.csv'
        os.remove(file)
    def del_trip_m(self):
        os.remove("tripmanager.csv")

    def del_invoices(self):
        os.remove("ManagerInvoice.csv")
        os.remove("CoordinatorInvoice.csv")

    def view_invoice(self):
        print("##################### Invoice of Co-ordinator ###############################")
        with open('CoordinatorInvoice.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            data=[]
            for row in csv_reader:
                data.append(row)
        pprint(data)
        print("##################### Invoice of Manager ###############################")
        with open('ManagerInvoice.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            data=[]
            for row in csv_reader:
                data.append(row)
        pprint(data)
Admin()

