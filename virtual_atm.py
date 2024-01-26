from tkinter import *
from tkinter import messagebox
import webbrowser


import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="805520",
    db="dell"
    )
frame = Tk()
frame.title("LOGIN FORM")
frame.geometry("500x300")
Title = Label(frame,text="L O G I N",font=('Arial',30),fg="BLACK")
Ll1 = Label(frame,text="USER ID")
Ll2 = Label(frame,text="ENTER PIN")
Lt1 = Entry(frame,width=20)
Lt2 = Entry(frame,width=20,show="*")
def LoginData():
    obj = con.cursor()
    user = Lt1.get()
    Pass = Lt2.get()
    sql = "select * from costumer where uid = %s and Password = %s"
    obj.execute(sql,[(user),(Pass)])
    results = obj.fetchall()
    if results:
        frame1=Toplevel()# class form
        frame1.title("Desktop")
        frame1.geometry("1000x700")
        Title1 = Label(frame1,text="A  T  M (Virtual)",font=('Arial',40))
        
        Title1.pack()
        def balance():
            
            frame2=Toplevel()# class form
            frame2.geometry("500x300")

            Title2 = Label(frame2,text=" CURRENT BALANCE ",font=('Arial',20))
            
            Title2.pack()
            obj = con.cursor()
            holder = Lt1.get()
            pin = Lt2.get()
            query1 = "SELECT balance FROM Costumer  WHERE uid ='"+holder+"' AND password = '"+pin+"'" 
            obj.execute(query1)
            results = obj.fetchall()

            bal = Label(frame2,text=results,font=('Arial',20))
            bal.place(x=200,y=150)
            frame2.mainloop()


        balance = Button(frame1, text = 'BALANCE', bd = 10, command=balance)
        balance.config(width=20, height=2)
        
        
        def deposit():
            frame2a=Toplevel()# class form
            frame2a.geometry("500x300")

            
            Title2a = Label(frame2a,text=" DEPOSIT ",font=('Arial',20))
            
            Title2a.pack()
            Cl2 = Label(frame2a,text="Enter AMOUNT")
            Ct2 = Entry(frame2a,width=20)
            def update():
                user = Lt1.get()

                balance = Ct2.get()
                Query = "update costumer set balance = balance+'"+balance+"' where uid = '"+user+"'"
                obj = con.cursor()
                obj.execute(Query)
                con.commit()#data save into the table
                messagebox.showinfo("Info","DEPOSIT SUCCESSFULL")
            Cb = Button(frame2a,text="Deposit",command=update)
            Cl2.place(x=100,y=120)
            Ct2.place(x=250,y=120)
            Cb.place(x=210,y=220)

            
            frame2a.mainloop()

        deposite = Button(frame1, text = 'DEPOSIT', bd = 10, command=deposit)
        deposite.config(width=20, height=2)

        def Update():
            frame2b=Toplevel()# class form
            frame2b.geometry("500x300")

            
            Title2b = Label(frame2b,text=" UPDATE PIN ",font=('Arial',20))
            
            Title2b.pack()
            Cl1 = Label(frame2b,text="Enter USER ID")
            Cl2 = Label(frame2b,text="Enter NEW PIN")
            Ct1 = Entry(frame2b,width=10)
            Ct2 = Entry(frame2b,width=20)
            def upgrade():
                uid = Ct1.get()
                pin = Ct2.get()
                Query = "update costumer set password ='"+pin+"' where uid = '"+uid+"'"
                obj = con.cursor()
                obj.execute(Query)
                con.commit()#data save into the table
                messagebox.showinfo("Info","PIN UPDATED")
            Cb1 = Button(frame2b,text="Update",command=upgrade)
            Cl1.place(x=100,y=80)
            Ct1.place(x=250,y=80)
            Cl2.place(x=100,y=120)
            Ct2.place(x=250,y=120)
            Cb1.place(x=210,y=220)

            
            frame2b.mainloop()

        update = Button(frame1, text = 'CHANGE PIN', bd = 10, command=Update)
        update.config(width=20, height=2)

        def withdrawl():
            frame2c=Toplevel()# class form
            frame2c.geometry("500x300")

            
            Title2c = Label(frame2c,text=" WITHDRAWL MONEY ",font=('Arial',20))
            
            Title2c.pack()
            Cl1 = Label(frame2c,text="Enter AMOUNT")
            Ct1 = Entry(frame2c,width=10)
            def upgrade():
                balance = Ct1.get()
                user = Lt1.get()
                Query21 = "update costumer set balance = balance-'"+balance+"' where uid = '"+user+"'"
                obj = con.cursor()
                obj.execute(Query21)
                con.commit()#data save into the table
                messagebox.showinfo("Info","PLEASE WAIT FOR CASH")
            Cb1 = Button(frame2c,text="Done",command=upgrade)
            Cl1.place(x=100,y=80)
            Ct1.place(x=250,y=80)
            Cb1.place(x=210,y=220)

            
            frame2c.mainloop()

        withdrawl = Button(frame1, text = 'WITHDRAWL', bd = 10,command=withdrawl)
        withdrawl.config(width=20, height=2)

        def openlink():
            webbrowser.open("https://www.onlinesbi.sbi")
        bank_site = Button(frame1, text = 'BANK SITE', bd = 10,command=openlink)
        bank_site.config(width=20, height=2)

        
        
        balance.place(x=100,y=120)
        deposite.place(x=800,y=120)
        update.place(x=100,y=420) 
        withdrawl.place(x=800,y=420) 
        bank_site.place(x=450,y=600) 
        frame1.mainloop()
        
    else:
        messagebox.showinfo("Info","Login Failed")
Lb1 = Button(frame,text="Login",command=LoginData)
Title.pack()
Ll1.place(x=100,y=80)
Lt1.place(x=250,y=80)
Ll2.place(x=100,y=120)
Lt2.place(x=250,y=120)
Lb1.place(x=200,y=200)
frame.mainloop()
