from datetime import date
from tkinter import *
from tkinter.messagebox import *
class Test:
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
    def Page9_Add_Bus_Running_Details(self):
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
        root=Tk()

        import sqlite3
        con=sqlite3.Connection('Bus_Booking')
        cur=con.cursor()

        cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,Name varchar(30),address varchar(40),phone number,email varchar(40))')
        cur.execute('create table if not exists bus(Bus_id number PRIMARY KEY,type varchar(30),capacity number,fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(Bus_id) references runs(Bus_id),foreign key(route_id) references route(route_id))')
        cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
        cur.execute('create table if not exists runs(Bus_id number,date date ,seat_avaiable number,PRIMARY KEY(Bus_id,date))')
        #cur.execute('drop table booking_history')
        cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile varchar(10) PRIMARY KEY,age number,bus_select number,t_o varchar(13),fr varchar(13),date date,fare number,current_date varchar(20))')

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        #root.geometry('%dx%d+0+0'%(w,h))
        root.state("zoomed")

        root.configure(background='LightYellow2')

        root.title("Add Bus Running Details")

        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        img_home=PhotoImage(file=".\\home.png")
        Label(root,image=img_Bus).grid(row=0,column=0,padx=w//3+155,columnspan=81)                                       

        Label(root,text="Online Bus Booking System",font="Arial 35 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=81)
        Label(root,text="Add Bus Running Details",font="Arial 25 bold",bg="light green",fg="dark green").grid(row=2,column=0,columnspan=81,pady=30)

        Label(root,text="Bus ID",font="Arial 15 bold").grid(row=3,column=31)
        Bus_ID=Entry(root,font="Arial 10 bold")
        Bus_ID.grid(row=3,column=32)

        Label(root,text="Running Date",font="Arial 15 bold").grid(row=3,column=33)
        Running_Date=Entry(root,font="Arial 10 bold")
        Running_Date.grid(row=3,column=34)

        Label(root,text="Seat Available",font="Arial 15 bold").grid(row=3,column=35)
        Seat_Available=Entry(root,font="Arial 10 bold")
        Seat_Available.grid(row=3,column=36)

        def add_run():
            if(askyesnocancel('?','Continue to Add Bus Running Details?')):
                if(Bus_ID.get().isspace() or Running_Date.get().isspace() or Seat_Available.get().isspace()):
                    showerror("Error","Missing")
                elif(len(Bus_ID.get())==0):
                    showerror("Missing","Please enter Bus ID")
                elif(len(Running_Date.get())==0):
                    showerror("Missing","Please enter Running Date")
                elif(len(Seat_Available.get())==0):
                    showerror("Missing","Please enter Seat Available")
                elif((Seat_Available.get()).isalpha()):
                    showerror("Error","Please enter Seats in no.")
                    
                else:
                    Bus__ID=Bus_ID.get()
                    Running__Date=Running_Date.get()
                    Seat__Available=Seat_Available.get()

                    query1='select Bus_id from runs where Bus_id=? and date=?'
                    y=(Bus__ID,Running__Date)
                    cur.execute(query1,y)
                    res=cur.fetchall()
                    if(res):
                        showerror('Error','Bus ID and Date already Exixts')
                    else:
                        query='insert into runs(Bus_id,date,seat_avaiable)values(?,?,?)'
                        value=(Bus__ID,Running__Date,Seat__Available)
                        cur.execute(query,value)
                        con.commit()
                        query2='select * from runs where Bus_id=? and date=?'
                        y=(Bus__ID,Running__Date)
                        cur.execute(query2,y)
                        result=cur.fetchall()
                        Label(root,text=result,font='arial 11 bold').grid(row=7,column=0,columnspan=200)

                        Bus_ID.delete(0,END)
                        Running_Date.delete(0,END)
                        Seat_Available.delete(0,END)
                        
                        showinfo("Success","Running Details Added Successfully")
                    
        def delete_run():
            if(askyesnocancel('?','Continue to Delete Bus Running Details?')):
                if(Bus_ID.get().isspace()): #or Running_Date.get().isspace() or Seat_Available.get().isspace()):
                    showerror("Error","Missing")
                if(len(Bus_ID.get())==0):
                    showerror("Missing","Please enter Bus ID")
                elif(len(Running_Date.get())==0):
                    showerror("Missing","Please enter Running Date")
                #elif(len(Seat_Available.get())==0):
                    showerror("Missing","Please enter Seat Available")
                #elif((Seat_Available.get()).isalpha()):
                    showerror("Error","Please enter Seats in no.")
                else:
                    Bus__ID=Bus_ID.get()
                    Running__Date=Running_Date.get()
                    Seat__Available=Seat_Available.get()

                    query1='select Bus_id from runs where Bus_id=? and date=?'
                    y=(Bus__ID,Running__Date)
                    cur.execute(query1,y)
                    res=cur.fetchall()
                    if(res):
                        showinfo('Found','Bus ID and date Exixts')
                        query1='delete from runs where Bus_id=? and date=?'
                        value=(Bus__ID,Running__Date)
                        cur.execute(query1,value)
                        con.commit()

                        #query2='select * from runs where bus_id=? and date=?'
                        #cur.execute(query2,value)
                        #result=cur.fetchall()
                        Label(root,text='Deleted',font='arial 11 bold').grid(row=7,column=0,columnspan=200)

                        Bus_ID.delete(0,END)
                        Running_Date.delete(0,END)
                        Seat_Available.delete(0,END)
                    
                        showinfo("Success","Running Deleted Successfully")

                    else:
                        showerror('NotFound','Bus ID and date not Exixts')

        Button(root,text="Add Run",font="Arial 15 bold",bg="light green",fg="black",command=add_run).grid(row=3,column=37)
        Button(root,text="Delete Run",font="Arial 15 bold",bg="light green",fg="red",command=delete_run).grid(row=3,column=38)

        def Page2_Home_Page():
            root.destroy()
            self.Page2_Home_Page()
        Button(root,image=img_home,command=Page2_Home_Page).grid(row=3,column=39)

        def Page5_Add_New_Details_To_Database():
            root.destroy()
            self.Page5_Add_New_Details_To_Database()
        Button(root,text="BACK",font="Arial 15 bold",bg="yellow",fg="black",command=Page5_Add_New_Details_To_Database).grid(row=3,column=40)

        root.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------      
    def Page8_Add_Bus_Route_Details(self):
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------      
        root=Tk()

        import sqlite3
        con=sqlite3.Connection('Bus_Booking')
        cur=con.cursor()

        cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,Name varchar(30),address varchar(40),phone number,email varchar(40))')
        cur.execute('create table if not exists bus(Bus_id number PRIMARY KEY,type varchar(30),capacity number,fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(Bus_id) references runs(Bus_id),foreign key(route_id) references route(route_id))')
        cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
        cur.execute('create table if not exists runs(Bus_id number,date date ,seat_avaiable number,PRIMARY KEY(Bus_id,date))')
        #cur.execute('drop table booking_history')
        cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile varchar(10) PRIMARY KEY,age number,bus_select number,t_o varchar(13),fr varchar(13),date date,fare number,current_date varchar(20))')


        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        #root.geometry('%dx%d+0+0'%(w,h))
        root.state("zoomed")

        root.configure(background='LightYellow2')

        root.title("Add Bus Route Details")

        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        img_home=PhotoImage(file=".\\home.png")
        Label(root,image=img_Bus).grid(row=0,column=0,padx=w//3+155,columnspan=81)
                                       

        Label(root,text="Online Bus Booking System",font="Arial 35 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=81)
        Label(root,text="Add Bus Route Details",font="Arial 25 bold",bg="light green",fg="dark green").grid(row=2,column=0,columnspan=81,pady=30)

        Label(root,text="RouteID",font="Arial 15 bold").grid(row=3,column=31)
        RouteID=Entry(root,font="Arial 10 bold")
        RouteID.grid(row=3,column=32)

        Label(root,text="Station Name",font="Arial 15 bold").grid(row=3,column=33)
        Station_Name=Entry(root,font="Arial 10 bold")
        Station_Name.grid(row=3,column=34)

        Label(root,text="Station ID",font="Arial 15 bold").grid(row=3,column=35)
        Station_ID=Entry(root,font="Arial 10 bold")
        Station_ID.grid(row=3,column=36)


        def add_route():
            if(askyesnocancel('?','Continue to Add Bus Route Details?')):
                if(len(RouteID.get())==0):
                    showerror("Missing","Please enter Route ID")
                elif(RouteID.get().isalpha()):
                    showerror("Error","Enter Route ID in no.s")
                elif(len(Station_Name.get())==0):
                    showerror("Missing","Please enter Station Name")
                elif(Station_Name.get().isnumeric()):
                    showerror("Error","Enter correct Station name")
                elif(len(Station_ID.get())==0):
                    showerror("Missing","Please enter Station ID")
                elif(Station_ID.get().isalpha()):
                    showerror("Error","Enter Station ID in no.s")
                else:

                    Route__ID=RouteID.get()
                    Station__Name=Station_Name.get()
                    Station__ID=Station_ID.get()
                    y=(RouteID.get(),Station_ID.get())
                    query1='select route_id,station_id from route where route_id=? and station_id=?'
                    cur.execute(query1,y)
                    res=cur.fetchall()
                    if(res):
                        showerror('Error','Bus ID and Station ID already Exixts')
                    else:
                        query='insert into route(route_id,station_name,station_id)values(?,?,?)'
                        value=(Route__ID,Station__Name,Station__ID)
                        cur.execute(query,value)
                        con.commit()
                        query2='select * from route where route_id=? and station_id=?'
                        y=(RouteID.get(),Station_ID.get())
                        cur.execute(query2,y)
                        result=cur.fetchall()
                        Label(root,text=result,font='arial 11 bold').grid(row=7,column=0,columnspan=200)

                        RouteID.delete(0,END)
                        Station_Name.delete(0,END)
                        Station_ID.delete(0,END)
                        
                        showinfo("Success","Route Added Successfully")

        def delete_route():
            if(askyesnocancel('?','Continue to Delete Bus Route Details?')):
                if(len(RouteID.get())==0):
                    showerror("Missing","Please enter Route ID")
                elif(RouteID.get().isalpha()):
                    showerror("Error","Enter Route ID in no.s")
                #elif(len(Station_Name.get())==0):
                #    showerror("Missing","Please enter Station Name")
                #elif(Station_Name.get().isnumeric()):
                #    showerror("Error","Enter correct Station name")
                elif(len(Station_ID.get())==0):
                    showerror("Missing","Please enter Station ID")
                elif(Station_ID.get().isalpha()):
                    showerror("Error","Enter Station ID in no.s")
                else:
                    Route__ID=RouteID.get()
                    Station__Name=Station_Name.get()
                    Station__ID=Station_ID.get()
                    y=(RouteID.get(),Station_ID.get())
                    query1='select route_id,station_id from route where route_id=? and station_id=?'
                    cur.execute(query1,y)
                    res=cur.fetchall()
                    if(res):
                        showinfo('Found','Bus ID and Station ID Exixts')
                        query1='delete from route where route_id=? and station_id=?'
                        y=(RouteID.get(),Station_ID.get())
                        cur.execute(query1,y)
                        con.commit()

                        #query2='select * from runs where bus_id=? and date=?'
                        #cur.execute(query2,value)
                        #result=cur.fetchall()
                        Label(root,text='      Deleted     ',font='arial 11 bold').grid(row=7,column=0,columnspan=200)

                        RouteID.delete(0,END)
                        Station_Name.delete(0,END)
                        Station_ID.delete(0,END)
                    
                        showinfo("Success","Route ID Deleted Successfully")
                    else:
                        showerror('not Found','Route ID and Station ID not Exixts')

        Button(root,text="Add Route",font="Arial 15 bold",bg="light green",fg="black",command=add_route).grid(row=3,column=37)
        Button(root,text="Delete Route",font="Arial 15 bold",bg="light green",fg="red",command=delete_route).grid(row=3,column=38)

        def Page2_Home_Page():
            root.destroy()
            self.Page2_Home_Page()
        Button(root,image=img_home,command=Page2_Home_Page).grid(row=3,column=39)

        def Page5_Add_New_Details_To_Database():
            root.destroy()
            self.Page5_Add_New_Details_To_Database()
        Button(root,text="BACK",font="Arial 15 bold",bg="yellow",fg="black",command=Page5_Add_New_Details_To_Database).grid(row=3,column=40)

        root.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------        
    def Page7_Add_Bus_Details(self):
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
        root=Tk()

        import sqlite3
        con=sqlite3.Connection('Bus_Booking')
        cur=con.cursor()

        cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,Name varchar(30),address varchar(40),phone number,email varchar(40))')
        cur.execute('create table if not exists bus(Bus_id number PRIMARY KEY,type varchar(30),capacity number,fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(Bus_id) references runs(Bus_id),foreign key(route_id) references route(route_id))')
        cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
        cur.execute('create table if not exists runs(Bus_id number,date date ,seat_avaiable number,PRIMARY KEY(Bus_id,date))')
        #cur.execute('drop table booking_history')
        cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile varchar(10) PRIMARY KEY,age number,bus_select number,t_o varchar(13),fr varchar(13),date date,fare number,current_date varchar(20))')


        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        #root.geometry('%dx%d+0+0'%(w,h))
        root.state("zoomed")

        root.configure(background='LightYellow2')

        root.title("Add Bus Details")

        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        img_home=PhotoImage(file=".\\home.png")
        Label(root,image=img_Bus).grid(row=0,column=0,padx=w//3+155,columnspan=81)
                                       

        Label(root,text="Online Bus Booking System",font="Arial 35 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=81)
        Label(root,text="Add Bus Details",font="Arial 25 bold",bg="light green",fg="dark green").grid(row=2,column=0,columnspan=81,pady=30)

        Label(root,text="Bus ID",font="bold").grid(row=3,column=31)
        Bus_ID=Entry(root)
        Bus_ID.grid(row=3,column=32)

        Label(root,text="Bus Type",font="bold").grid(row=3,column=33)
        bus_type=StringVar()
        bus_type.set("Bus Type")
        opt=("AC 2X2","AC 3X2","Non AC 2X2","Non AC 3X2","AC-Sleeper 2X1","Non AC-Sleeper 2X1")
        d_menu=OptionMenu(root,bus_type,*opt).grid(row=3,column=34)

        Label(root,text="Capacity",font="bold").grid(row=3,column=35)
        Capacity=Entry(root)
        Capacity.grid(row=3,column=36)

        Label(root,text="Fare Rs.",font="bold").grid(row=3,column=37)
        Fare=Entry(root)
        Fare.grid(row=3,column=38)

        Label(root,text="Operator ID",font="bold").grid(row=3,column=39)
        Operator_ID=Entry(root)
        Operator_ID.grid(row=3,column=40)

        Label(root,text="Route ID",font="bold").grid(row=3,column=41)
        Route_ID=Entry(root)
        Route_ID.grid(row=3,column=42)


        def add_bus():
            if(askyesnocancel('?','Continue to Add Bus Details?')):
                if(len(Bus_ID.get())==0):
                    showerror("Missing","Please enter Bus ID")
                elif(Bus_ID.get().isalpha()):
                    showerror("Error","Please enter correct Bus ID")
                elif(len(Capacity.get())==0):
                    showerror("Missing","Please enter Capacity")
                elif(Capacity.get().isalpha()):
                    showerror("Error","Please enter correct Capacity")
                elif(len(Fare.get())==0):
                    showerror("Missing","Please enter Fare")
                elif(Fare.get().isalpha()):
                    showerror("Error","Please enter correct Fare in Rs.")
                elif(len(Operator_ID.get())==0):
                    showerror("Missing","Please enter Operator ID")
                elif(Operator_ID.get().isalpha()):
                    showerror("Error","Please enter correct Operator ID")
                elif(len(Route_ID.get())==0):
                    showerror("Missing","Please enter Route ID")
                elif(Route_ID.get().isalpha()):
                    showerror("Error","Please enter correct Route ID")
                else:
                    Bus__ID=Bus_ID.get()
                    bus__type=bus_type.get()
                    Capacity_=Capacity.get()
                    Fare_=Fare.get()
                    Operator__ID=Operator_ID.get()
                    Route__ID=Route_ID.get()

                    query1='select Bus_id from bus where Bus_id=?'
                    cur.execute(query1,Bus__ID)
                    res=cur.fetchall()
                    if(res):
                        showerror('Error','Bus ID already Exixts')
                    else:
                        query='insert into bus(Bus_id,type,capacity ,fare, operator_id,route_id)values(?,?,?,?,?,?)'
                        value=(Bus__ID,bus__type,Capacity_,Fare_,Operator__ID,Route__ID)
                        cur.execute(query,value)
                        con.commit()
                        query2='select * from bus where Bus_id=?'
                        cur.execute(query2,Bus__ID)
                        result=cur.fetchall()
                        Label(root,text=result,font='arial 11 bold').grid(row=7,column=0,columnspan=200)

                        Bus_ID.delete(0,END)
                        #bus_type.delete(0,END)
                        Capacity.delete(0,END)
                        Fare.delete(0,END)
                        Operator_ID.delete(0,END)
                        Route_ID.delete(0,END)
                
                        showinfo("Success","Bus Details Added Successfully")

                        #print(result)

        def edit_bus():
            if(askyesnocancel('?','Continue to Edit Bus Details?')):
                if(len(Bus_ID.get())==0):
                    showerror("Missing","Please enter Bus ID")
                elif(Bus_ID.get().isalpha()):
                    showerror("Error","Please enter correct Bus ID")
                elif(len(Capacity.get())==0):
                    showerror("Missing","Please enter Capacity")
                elif(Capacity.get().isalpha()):
                    showerror("Error","Please enter correct Capacity")
                elif(len(Fare.get())==0):
                    showerror("Missing","Please enter Fare")
                elif(Fare.get().isalpha()):
                    showerror("Error","Please enter correct Fare in Rs.")
                elif(len(Operator_ID.get())==0):
                    showerror("Missing","Please enter Operator ID")
                elif(Operator_ID.get().isalpha()):
                    showerror("Error","Please enter correct Operator ID")
                elif(len(Route_ID.get())==0):
                    showerror("Missing","Please enter Route ID")
                elif(Route_ID.get().isalpha()):
                    showerror("Error","Please enter correct Route ID")
                else:
                    Bus__ID=Bus_ID.get()
                    bus__type=bus_type.get()
                    Capacity_=Capacity.get()
                    Fare_=Fare.get()
                    Operator__ID=Operator_ID.get()
                    Route__ID=Route_ID.get()

                    query1='select Bus_id from bus where Bus_id=?'
                    cur.execute(query1,Bus__ID)
                    res=cur.fetchall()
                    if(res):
                        showinfo('Found','Bus ID Exixts')

                        query1='update bus set type=?,capacity=?,fare=?,operator_id=?,route_id=? where bus_id=?'
                        value=(bus__type,Capacity_,Fare_,Operator__ID,Route__ID,Bus__ID)
                        cur.execute(query1,value)
                        con.commit()

                        query2='select * from bus where operator_id=?'
                        cur.execute(query2,Bus__ID)
                        result=cur.fetchall()
                        Label(root,text=result,font='arial 11 bold').grid(row=7,column=0,columnspan=200)

                        Bus_ID.delete(0,END)
                        #bus_type.delete(0,END)
                        Capacity.delete(0,END)
                        Fare.delete(0,END)
                        Operator_ID.delete(0,END)
                        Route_ID.delete(0,END)
                    
                        showinfo("Success","Edited Successfully")
                    else:
                        showerror('Not Found','Bus ID not Exixts')


        Button(root,text="Add Bus",font="Arial 15 bold",bg="light green",fg="black",command=add_bus).grid(row=5,column=35)
        Button(root,text="Edit Bus",font="Arial 15 bold",bg="light green",fg="black",command=edit_bus).grid(row=5,column=36)

        def Page2_Home_Page():
            root.destroy()
            self.Page2_Home_Page()
        Button(root,image=img_home,bg='green',command=Page2_Home_Page).grid(row=5,column=37,pady=20)

        def Page5_Add_New_Details_To_Database():
            root.destroy()
            self.Page5_Add_New_Details_To_Database()
        Button(root,text="BACK",font="Arial 15 bold",bg="yellow",fg="black",command=Page5_Add_New_Details_To_Database).grid(row=5,column=38)

        root.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------     
    def Page6_Add_Bus_Operator_Details(self):
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
        root=Tk()
        
        import sqlite3
        con=sqlite3.Connection('Bus_Booking')
        cur=con.cursor()

        cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,Name varchar(30),address varchar(40),phone number,email varchar(40))')
        cur.execute('create table if not exists bus(Bus_id number PRIMARY KEY,type varchar(30),capacity number,fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(Bus_id) references runs(Bus_id),foreign key(route_id) references route(route_id))')
        cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
        cur.execute('create table if not exists runs(Bus_id number,date date ,seat_avaiable number,PRIMARY KEY(Bus_id,date))')
        #cur.execute('drop table booking_history')
        cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile varchar(10) PRIMARY KEY,age number,bus_select number,t_o varchar(13),fr varchar(13),date date,fare number,current_date varchar(20))')

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        #root.geometry('%dx%d+0+0'%(w,h))
        root.state("zoomed")

        root.configure(background='LightYellow2')

        root.title("Add Bus Operator Details")

        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        img_home=PhotoImage(file=".\\home.png")
        Label(root,image=img_Bus).grid(row=0,column=0,padx=w//3+155,columnspan=81)
                                       

        Label(root,text="Online Bus Booking System",font="Arial 35 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=81)
        Label(root,text="Add Bus Operator Details",font="Arial 25 bold",bg="light green",fg="dark green").grid(row=2,column=0,columnspan=81,pady=30)

        Label(root,text="Operator ID",font="Arial 15 bold").grid(row=3,column=31)
        Operator_ID=Entry(root)
        Operator_ID.grid(row=3,column=32)

        Label(root,text="Name",font="Arial 15 bold").grid(row=3,column=33)
        Name=Entry(root)
        Name.grid(row=3,column=34)

        Label(root,text="Address",font="Arial 15 bold").grid(row=3,column=35)
        Address=Entry(root)
        Address.grid(row=3,column=36)

        Label(root,text="Phone",font="Arial 15 bold").grid(row=3,column=37)
        Phone=Entry(root)
        Phone.grid(row=3,column=38)

        Label(root,text="Email",font="Arial 15 bold").grid(row=3,column=39)
        Email=Entry(root)
        Email.grid(row=3,column=40)

        def add():
            if(askyesnocancel('?','Continue to Add Operator Details?')):
                if(len(Operator_ID.get())==0):
                    showerror("Missing","Please enter Operator ID")
                elif(Operator_ID.get().isalpha()):
                    showerror("Error","Please enter correcr Operator ID")
                elif(len(Name.get())==0):
                    showerror("Missing","Please enter Name")
                elif(Name.get().isnumeric()):
                    showerror("Error","Please enter correcr Name")
                elif(len(Address.get())==0):
                    showerror("Missing","Please enter Address")
                elif(Address.get().isnumeric()):
                    showerror("Error","Please enter correcr Address")
                elif(len(Phone.get())==0):
                    showerror("Missing","Please enter Phone")
                elif(Phone.get().isalpha() or len(Phone.get())!=10 ):
                    showerror("Error","Please enter correcr Mobile no.")
                elif(len(Email.get())==0):
                    showerror("Missing","Please enter Email")
                else:
                    operator_ID=Operator_ID.get()
                    operator_Name=Name.get()
                    address=Address.get()
                    phone=Phone.get()
                    email=Email.get()
                    query1='select operator_id from operator where operator_id=?'
                    cur.execute(query1,operator_ID)
                    res=cur.fetchall()
                    if(res):
                        showerror('Error','Operator ID already Exixts')
                    else:
                        query='insert into operator(operator_id,name,address,phone,email)values(?,?,?,?,?)'
                        value=(operator_ID,operator_Name,address,phone,email)
                        cur.execute(query,value)
                        con.commit()
                        query2='select * from operator where operator_id=?'
                        cur.execute(query2,operator_ID)
                        result=cur.fetchall()
                        Label(root,text=result,font='arial 11 bold').grid(row=5,column=0,columnspan=200)

                        Operator_ID.delete(0,END)
                        Name.delete(0,END)
                        Address.delete(0,END)
                        Phone.delete(0,END)
                        Email.delete(0,END)
                
                        showinfo("Success","Added Successfully")

                        #print(result)
                
        def edit():
            if(askyesnocancel('?','Continue to Edit Operator Details?')):
                if(len(Operator_ID.get())==0):
                    showerror("Missing","Please enter Operator ID")
                elif(Operator_ID.get().isalpha()):
                    showerror("Error","Please enter correcr Operator ID")
                elif(len(Name.get())==0):
                    showerror("Missing","Please enter Name")
                elif(Name.get().isnumeric()):
                    showerror("Error","Please enter correcr Name")
                elif(len(Address.get())==0):
                    showerror("Missing","Please enter Address")
                elif(Address.get().isnumeric()):
                    showerror("Error","Please enter correcr Address")
                elif(len(Phone.get())==0):
                    showerror("Missing","Please enter Phone")
                elif(Phone.get().isalpha() or len(Phone.get())!=10 ):
                    showerror("Error","Please enter correcr Mobile no.")
                elif(len(Email.get())==0):
                    showerror("Missing","Please enter Email")
                else:

                    operator_ID=Operator_ID.get()
                    operator_Name=Name.get()
                    address=Address.get()
                    phone=Phone.get()
                    email=Email.get()
                    
                    query1='select operator_id from operator where operator_id=?'
                    cur.execute(query1,operator_ID)
                    res=cur.fetchall()
                    if(res):
                        showinfo('Found','Operator ID Exixts')
                        query1='update operator set name=?,address=?,phone=?,email=? where operator_id=?'
                        value=(operator_Name,address,phone,email,operator_ID)
                        cur.execute(query1,value)
                        con.commit()

                        query2='select * from operator where operator_id=?'
                        cur.execute(query2,operator_ID)
                        result=cur.fetchall()
                        Label(root,text=result,font='arial 11 bold').grid(row=5,column=0,columnspan=200)

                        Operator_ID.delete(0,END)
                        Name.delete(0,END)
                        Address.delete(0,END)
                        Phone.delete(0,END)
                        Email.delete(0,END)
                    
                        showinfo("Success","Edited Successfully")
                    else:
                        showerror('Not found','Operator ID not exists')

        Button(root,text="Add",font="Arial 15 bold",bg="light green",fg="black",command=add).grid(row=3,column=41)
        Button(root,text="Edit",font="Arial 15 bold",bg="light green",fg="black",command=edit).grid(row=3,column=42)

        def Page2_Home_Page():
            root.destroy()
            self.Page2_Home_Page()   
        Button(root,image=img_home,bg="light green",fg="black",command=Page2_Home_Page).grid(row=3,column=43,pady=20)

        def Page5_Add_New_Details_To_Database():
            root.destroy()
            self.Page5_Add_New_Details_To_Database()
        Button(root,text="BACK",font="Arial 15 bold",bg="yellow",fg="black",command=Page5_Add_New_Details_To_Database).grid(row=3,column=44)

        root.mainloop()
    
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------    
    def Page5_Add_New_Details_To_Database(self):
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
        root=Tk()

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        #root.geometry('%dx%d+0+0'%(w,h))
        root.state("zoomed")

        root.configure(background='LightYellow2')

        root.title("Add New Details To DataBase")

        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        img_home=PhotoImage(file=".\\home.png")
        Label(root,image=img_Bus).grid(row=0,column=0,padx=w//3+155,columnspan=81)
                                       
        Label(root,text="Online Bus Booking System",font="Arial 35 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=81)
        Label(root,text="Add New Details To DataBase",font="Arial 25 bold",bg="light green",fg="dark green").grid(row=2,column=0,columnspan=81,pady=30)

        def Page6_Add_Bus_Operator_Details():
            root.destroy()
            self.Page6_Add_Bus_Operator_Details() 
        Button(root,text="New Operator",font="Arial 15 bold",bg="OliveDrab1",fg="black",command=Page6_Add_Bus_Operator_Details).grid(row=3,column=32)

        def Page7_Add_Bus_Details():
            root.destroy()
            self.Page7_Add_Bus_Details()
        Button(root,text="New Bus",font="Arial 15 bold",bg="orange",fg="black",command=Page7_Add_Bus_Details).grid(row=3,column=37)

        def Page8_Add_Bus_Route_Details():
            root.destroy()
            self.Page8_Add_Bus_Route_Details()
        Button(root,text="New Route",font="Arial 15 bold",bg="light blue",fg="black",command=Page8_Add_Bus_Route_Details).grid(row=3,column=42)

        def Page9_Add_Bus_Running_Details():
            root.destroy()
            self.Page9_Add_Bus_Running_Details()
        Button(root,text="New Run",font="Arial 15 bold",bg="RosyBrown2",fg="black",command=Page9_Add_Bus_Running_Details).grid(row=3,column=47)

        def Page2_Home_Page():
            root.destroy()
            self.Page2_Home_Page()                                                                                 
        Button(root,image=img_home,bg='green',command=Page2_Home_Page).grid(row=3,column=50)

        root.mainloop()



#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
    def signin_page(self):
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
        root=Tk()
        root.geometry('450x450')
        root.title('Sign_In_Page')

        import sqlite3
        con=sqlite3.Connection('Bus_Booking')
        cur=con.cursor()

        cur.execute('create table if not exists admin(name varchar(20), email varchar(50) PRIMARY KEY ,password varchar(15), question varchar(60),answer varchar(12))')

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        img_Bus=PhotoImage(file=".\\imgbin_computer-icons-avatar-user-login-png.png")
        img_Bus1=PhotoImage(file=".\\1234.png")
        img_Bus2=PhotoImage(file=".\\login_logo.png")

        Label(root,text="Create Account",font='Arial 15 bold',bg='light blue').grid(row=0,column=9,pady=10,columnspan=35)
        Label(root,image=img_Bus).grid(row=1,column=9,columnspan=35,pady=10)


        Label(root,text="Name",font='Arial 12 bold').grid(row=2,column=8,padx=20)
        a_name=Entry(root,font='cambria 11 bold')
        a_name.grid(row=2,column=9,columnspan=35)

        Label(root,text="Email",font='Arial 12 bold').grid(row=3,column=8,padx=20)
        a_email=Entry(root,font='cambria 11 bold')
        a_email.grid(row=3,column=9,columnspan=35)

        Label(root,text="Password",font='Arial 12 bold').grid(row=4,column=8,padx=20)
        a_password=Entry(root,font='cambria 11 bold')
        a_password.grid(row=4,column=9,columnspan=35)

        Label(root,text="Security Ques.",font='Arial 12 bold').grid(row=5,column=8,padx=20)
        a_question=Entry(root,font='cambria 11 bold')
        a_question.grid(row=5,column=9,columnspan=35)

        Label(root,text="Answer",font='Arial 12 bold').grid(row=6,column=8,padx=20)
        a_answer=Entry(root,font='cambria 11 bold')
        a_answer.grid(row=6,column=9,columnspan=35)


        def create_account():
            if(len(a_name.get())==0):
                showerror("Missing","Please enter Name")
            elif(a_name.get().isnumeric()):
                showerror("Error","Please Valid name")
            elif(len(a_email.get())==0):
                showerror("Missing","Please enter Email")
            elif(len(a_password.get())==0):
                showerror("Missing","Please enter Password")
            elif(len(a_question.get())==0):
                showerror("Missing","Please enter Question")
            elif(a_question.get().isnumeric()):
                showerror("Error","Please Valid Question")
            elif(len(a_answer.get())==0):
                showerror("Missing","Please enter Answer")
            elif(a_name.get().isspace() or a_email.get().isspace() or a_password.get().isspace()  or a_question.get().isspace()  or a_answer.get().isspace()):
                showerror("Error","Missing")
            else:
                n=a_name.get()
                e=a_email.get()
                p=a_password.get()
                q=a_question.get()
                an=a_answer.get()

                value=e
                cur.execute('select * from admin where email=(?)',[value])
                res=cur.fetchall()
                if(res):
                    showerror('Error','Email already used!')
                else:
                    value1=(n,e,p,q,an)
                    query1='insert into admin(name,email,password,question,answer) values(?,?,?,?,?)'
                    cur.execute(query1,value1)
                    con.commit()
                    showinfo('Confirm','Account Successfully Created!')
                    a_name.delete(0,END)
                    a_email.delete(0,END)
                    a_password.delete(0,END)
                    a_question.delete(0,END)
                    a_answer.delete(0,END) 

        Button(root,text='SIGN IN',font='Arial 11 bold',bg='light blue',fg='black',border=3,command=create_account).grid(row=8,column=24,pady=10)
        def admin_page():
            root.destroy()
            self.admin_page()
        Button(root,text='Back',font='Arial 11 bold',bg='pink',fg='black',border=3,command=admin_page).grid(row=9,column=24,pady=10)
            

        root.mainloop()





#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
    def reset_page(self):
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
        root=Tk()
        root.geometry('450x450')
        root.title('reset_page')

        import sqlite3
        con=sqlite3.Connection('Bus_Booking')
        cur=con.cursor()

        cur.execute('create table if not exists admin(name varchar(20), email varchar(50) PRIMARY KEY ,password varchar(15), question varchar(60),answer varchar(12))')

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        img_Bus=PhotoImage(file=".\\imgbin_computer-icons-avatar-user-login-png.png")
        img_Bus1=PhotoImage(file=".\\1234.png")
        img_Bus2=PhotoImage(file=".\\login_logo.png")
        img_Bus3=PhotoImage(file=".\\321.png")
        Label(root,text="Reset Account",font='Arial 15 bold',bg='light blue').grid(row=0,column=9,pady=10,columnspan=60)
        Label(root,image=img_Bus).grid(row=1,column=9,columnspan=60)

        Label(root,text="Username",font='Arial 11 bold',fg='green').grid(row=2,column=9)
        username=Entry(root,font='cambria 11 bold')
        username.grid(row=3,column=9)

        def check_user():
            if(len(username.get())==0):
                showerror('Error','Enter the username')
            elif(username.get().isspace()):
                showerror('Error','Enter the username')
            else:
                value=username.get()
                cur.execute('select question from admin where email=(?)',[value])
                res=cur.fetchall()
                if(res):
                    Label(root,text=res,font='Arial 11 bold',fg='red').grid(row=4,column=9)

                    Label(root,text="Answer",font='Arial 11 bold',fg='blue').grid(row=5,column=9)
                    answer=Entry(root,font='cambria 11 bold')
                    answer.grid(row=6,column=9)

                    def reset():
                        if(len(answer.get())==0):
                            showerror('Error','Enter the Answer')
                        elif(answer.get().isspace()):
                            showerror('Error','Enter the Answer')
                        else:
                            value=answer.get()
                            cur.execute('select * from admin where answer=(?)',[value])
                            res=cur.fetchall()
                            if(res):
                                showinfo('Reset','Password Reset Successfully!! Please set the new one')

                                Label(root,text="New Password",font='Arial 11 bold',fg='blue').grid(row=8,column=9)
                                new_password=Entry(root,font='cambria 11 bold')
                                new_password.grid(row=9,column=9)

                                def update_password():
                                    if(len(new_password.get())==0):
                                        ('Error','Enter the new password')
                                    elif(new_password.get().isspace()):
                                        showerror('Error','Enter the new password')
                                    else:
                                        m=new_password.get()
                                        n=username.get()
                                        v=(m,n)
                                        cur.execute('update admin set password=(?) where email=(?)',[m,n])
                                        con.commit()
                                        showinfo('Updated','Password Reset Successfully')

                        
                                Button(root,text='Set',font='Arial 11 bold',bg='light blue',fg='black',border=3,command=update_password).grid(row=10,column=9,pady=4)

                                
                            else:
                                showerror('Error','Incorrect answer')

                    Button(root,text='Reset',font='Arial 11 bold',bg='light blue',fg='black',border=3,command=reset).grid(row=7,column=9,pady=8)
                else:
                    showerror('Error','Username not exists')
                    
        Button(root,text='',font='Arial 11 bold',bg='green',fg='black',border=1,command=check_user).grid(row=3,column=10)


        Label(root,text=14*' ').grid(row=3,column=8,padx=50)


        def admin_page():
            root.destroy()
            self.admin_page()
        Button(root,text='Back',font='Arial 11 bold',bg='pink',fg='black',border=3,command=admin_page).grid(row=11,column=9,pady=3)

          

        root.mainloop()




#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
    def login_page(self):
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
        root=Tk()
        root.geometry('450x450')
        root.title('login_page')

        import sqlite3
        con=sqlite3.Connection('Bus_Booking')
        cur=con.cursor()

        cur.execute('create table if not exists admin(name varchar(20), email varchar(50) PRIMARY KEY ,password varchar(15), question varchar(60),answer varchar(12))')


        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        img_admin_logo=PhotoImage(file=".\\imgbin_computer-icons-avatar-user-login-png.png")
        img_Bus1=PhotoImage(file=".\\1234.png")
        img_Bus2=PhotoImage(file=".\\login_logo.png")
        img_Bus3=PhotoImage(file=".\\321.png")
        Label(root,text="Admin  Login",font='Arial 15 bold',bg='light blue').grid(row=0,column=9,pady=10,columnspan=60)
        Label(root,image=img_admin_logo).grid(row=1,column=9,columnspan=60)

        Label(root,image=img_Bus2).grid(row=2,column=8,padx=50)
        user=Entry(root,font='cambria 11 bold')
        user.grid(row=2,column=9)

        Label(root,image=img_Bus1).grid(row=3,column=8,padx=50)
        password=Entry(root,font='cambria 11 bold')
        password.grid(row=3,column=9)

        def login():
            if(len(user.get())==0):
                showerror("Missing","Please enter username")
            elif(len(password.get())==0):
                showerror("Missing","Please enter password")    
            elif(user.get().isspace() or password.get().isspace()):
                showerror('Error','Enter the fields')
            else:
                value1=user.get()
                value2=password.get()
                cur.execute('select * from admin where email=(?)',[value1])
                res1=cur.fetchall()
                cur.execute('select * from admin where password=(?)',[value2])
                res2=cur.fetchall()
                if(res1 and res2):
                    root.destroy()
                    self.Page5_Add_New_Details_To_Database()
                else:
                    showerror('Error','Incorrect Username or Password')
                    Label(root,text="Forgot  Password ?",font='Arial 11 bold',fg='red').grid(row=7,column=9)

                    def reset_page():
                        root.destroy()
                        self.reset_page()  
                    Button(root,text="Reset Here",font='Arial 11 bold',fg='red',command=reset_page).grid(row=8,column=9,pady=5)
               
        
        Button(root,text='LOG IN',font='Arial 11 bold',bg='light blue',fg='black',border=3,command=login).grid(row=4,column=9,pady=30)
           
        def admin_page():
            root.destroy()
            self.admin_page()
        Button(root,text='Back',font='Arial 11 bold',bg='pink',fg='black',border=3,command=admin_page).grid(row=9,column=9,pady=5)

        root.mainloop()

        
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
    def admin_page(self):
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
        root=Tk()
        #root.configure(background='orange')
        root.geometry('450x450')

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        img_Bus=PhotoImage(file=".\\imgbin_computer-icons-avatar-user-login-png.png")
        Label(root,text="Admin  Login",font='Arial 15 bold',bg='light blue').grid(row=0,column=8,pady=10)
        Label(root,image=img_Bus).grid(row=1,column=8)


        def login():
            root.destroy()
            self.login_page()
        Button(root,text='LOG IN',font='Arial 11 bold',bg='light blue',fg='black',border=3,command=login).grid(row=2,column=7,padx=50,pady=40)

        def signin():
            root.destroy()
            self.signin_page()
        Button(root,text='SIGN IN',font='Arial 11 bold',bg='light green',fg='black',border=3,command=signin).grid(row=2,column=10,padx=30)
            
        def Page2_Home_Page():
            root.destroy()
            self.Page2_Home_Page()
        Button(root,text='HOME',font='Arial 11 bold',bg='pink',fg='black',border=3,command=Page2_Home_Page).grid(row=4,column=8,padx=30)

        root.mainloop()



  
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------   
    def Page4_Check_Your_Booking(self):
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
        root=Tk()

        import sqlite3
        con=sqlite3.Connection('Bus_Booking')
        cur=con.cursor()

        cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,Name varchar(30),address varchar(40),phone number,email varchar(40))')
        cur.execute('create table if not exists bus(Bus_id number PRIMARY KEY,type varchar(30),capacity number,fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(Bus_id) references runs(Bus_id),foreign key(route_id) references route(route_id))')
        cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
        cur.execute('create table if not exists runs(Bus_id number,date date ,seat_avaiable number,PRIMARY KEY(Bus_id,date))')
        #cur.execute('drop table booking_history')
        cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile varchar(10) PRIMARY KEY,age number,bus_select number,t_o varchar(13),fr varchar(13),date date,fare number,current_date varchar(20))')

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        #root.geometry('%dx%d+0+0'%(w,h))
        root.state("zoomed")

        root.configure(background='LightYellow2')

        root.title("Check Your Booking")

        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        img_home=PhotoImage(file=".\\home.png")

        Label(root,image=img_Bus).grid(row=0,column=0,padx=w//3+155,columnspan=82)

        Label(root,text="Online Bus Booking System",font="Arial 35 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=82,pady=30)

        Label(root,text="Enter Your Mobile No.:",font="Arial 15 bold",fg="black",bg='pink').grid(row=3,column=40)
        mobile=Entry(root,font="Arial 10 bold")
        mobile.grid(row=3,column=41)

        def check_booking():
            if(mobile.get().isnumeric() and len(mobile.get())==10):
                frame=Frame(root,relief="groove",bd=5)
                frame.grid(row=6,column=2,columnspan=100)

                Label(root,text="Bus Ticket",font='Arial 12 bold',fg="firebrick2").grid(row=5,column=41,)
                value=mobile.get()
                cur.execute('select  * from booking_history where mobile=(?)',[value])

                res=cur.fetchall()
                if(res):
                    
                    Label(frame,text="Passenger:",font='Arial 10 bold').grid(row=3,column=0,)
                    Label(frame,text=res[0][0],font='Arial 10 bold',fg="magenta3").grid(row=3,column=1,)
                
                    Label(frame,text="Gender:",font='Arial 10 bold').grid(row=3,column=3,)
                    Label(frame,text=res[0][1],font='Arial 10 bold',fg="magenta3").grid(row=3,column=4,)
                
                    Label(frame,text="No. Of Seat:",font='Arial 10 bold').grid(row=4,column=0,)
                    Label(frame,text=res[0][2],font='Arial 10 bold',fg="magenta3").grid(row=4,column=1,)
                
                    Label(frame,text="Phone:",font='Arial 10 bold').grid(row=4,column=3,)
                    Label(frame,text=res[0][3],font='Arial 10 bold',fg="magenta3").grid(row=4,column=4,)
                
                    Label(frame,text="Age.:",font='Arial 10 bold').grid(row=5,column=0)
                    Label(frame,text=res[0][4],font='Arial 10 bold',fg="magenta3").grid(row=5,column=1,)
                
                    Label(frame,text="Bus.:",font='Arial 10 bold').grid(row=5,column=3,)
                    Label(frame,text=res[0][5],font='Arial 10 bold',fg="magenta3").grid(row=5,column=4,)
                
                    Label(frame,text="From:",font='Arial 10 bold').grid(row=6,column=0)
                    Label(frame,text=res[0][6],font='Arial 10 bold',fg="magenta3").grid(row=6,column=1,)
                
                    Label(frame,text="To:",font='Arial 10 bold').grid(row=6,column=3)
                    Label(frame,text=res[0][7],font='Arial 10 bold',fg="magenta3").grid(row=6,column=4)
                
                    Label(frame,text="Journey On:",font='Arial 10 bold').grid(row=7,column=0)
                    Label(frame,text=res[0][8],font='Arial 10 bold',fg="magenta3").grid(row=7,column=1)
                
                    Label(frame,text="Fare:",font='Arial 10 bold').grid(row=7,column=3)
                    Label(frame,text=res[0][2]*res[0][9],font='Arial 10 bold',fg="magenta3").grid(row=7,column=4)

                    Label(frame,text="Booked On:",font='Arial 10 bold').grid(row=8,column=0)
                    Label(frame,text=res[0][2]*res[0][10],font='Arial 10 bold',fg="magenta3").grid(row=8,column=1)
                    
                    value=str(res[0][2]*res[0][9])

                    Label(root,text="Your fare price is  Rs."+value,font='Arial 15 bold',fg='blue').grid(row=9,column=0,columnspan=82)
                else:
                    showerror('Error','No booking with this Mobile no.')
                    if(askyesno('Booking','Do you want to do booking?')):
                        root.destroy()
                        self.Page3_Enter_Journey_Details_Show_Bus_popup()                       
                
            else:
                showerror("Booking","Enter the correct mobile no.!")
                
        Button(root,text="Chek Booking",font="Arial 12 bold",fg="blue",bg='pink',command=check_booking).grid(row=3,column=42)

        def Page2_Home_Page():
            root.destroy()
            self.Page2_Home_Page()
        Button(root,image=img_home,bg='green',command=Page2_Home_Page).grid(row=3,column=43)

        root.mainloop()
        
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
    def Page3_Enter_Journey_Details_Show_Bus_popup(self):
        
        root=Tk()

        import sqlite3
        con=sqlite3.Connection('Bus_Booking')
        cur=con.cursor()

        cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,Name varchar(30),address varchar(40),phone number,email varchar(40))')
        cur.execute('create table if not exists bus(Bus_id number PRIMARY KEY,type varchar(30),capacity number,fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(Bus_id) references runs(Bus_id),foreign key(route_id) references route(route_id))')
        cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
        cur.execute('create table if not exists runs(Bus_id number,date date ,seat_avaiable number,PRIMARY KEY(Bus_id,date))')
        #cur.execute('drop table booking_history')
        cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile varchar(10) PRIMARY KEY,age number,bus_select number,t_o varchar(13),fr varchar(13),date date,fare number,current_date varchar(20))')

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        #root.geometry('%dx%d+0+0'%(w,h))
        root.state("zoomed")

        root.title("Enter Journey Details")
        bus_select=IntVar()
        Bus1=0
        Bus2=0

        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        img_home=PhotoImage(file=".\\home.png")
        Label(root,image=img_Bus).grid(row=0,column=0,padx=w//3+155,columnspan=81)                               

        Label(root,text="Online Bus Booking System",font="Arial 35 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=81)
        Label(root,text="Enter Journey Details",font="Arial 25 bold",bg="light green",fg="dark green").grid(row=2,column=0,columnspan=81,pady=30)

        Label(root,text="To",font="Arial 15 bold").grid(row=3,column=33)
        To=Entry(root,font="Arial 10 bold")
        To.grid(row=3,column=34)

        Label(root,text="From",font="Arial 15 bold").grid(row=3,column=35)
        From=Entry(root,font="Arial 10 bold")
        From.grid(row=3,column=36)

        Label(root,text="Journey Date",font="Arial 15 bold").grid(row=3,column=37)
        JDate=Entry(root,font="Arial 10 bold")
        JDate.insert(0,"DD/MM/YYYY")
        JDate.grid(row=3,column=38)
        #Label(root,text="DD//MM/YYYY",font="Arial 11 bold",fg='red').grid(row=4,column=38)
        
        dict={}
        def show_bus():
            if(To.get().isspace() or From.get().isspace() or JDate.get().isspace()):
                showerror("Error","Missing!")
            elif(len(To.get())==0 or len(From.get())==0 or len(JDate.get())==0):
                showerror("Missing","Enter all the fields")
         
            elif(To.get().isnumeric() or From.get().isnumeric()):
                showerror("Missing","Enter city names correctly!")
            
            else:
                to=To.get()
                fr=From.get()
                Jd=JDate.get()

                value=(to,fr,Jd)
                query='select name,type,seat_avaiable,capacity,fare,runs.bus_id from operator,bus,runs,route as t,route as f where operator.operator_id=bus.operator_id and bus.bus_id=runs.bus_id and bus.route_id=t.route_id and t.station_name=? and f.station_name=? and date=?'
                cur.execute(query,value)
                res=cur.fetchall()
                #print(res)
                
                i=1
                for a in res:
                    dict.update({i:a})
                    n=0
                    for b in a:
                        Bus1=Radiobutton(root,text="BUS"+str(i),variable=bus_select,value=i,font="Arial 10 bold")
                        Bus1.grid(row=6+i,column=33)
                        Label(root,text=b,font="Arial 10 bold").grid(row=6+i,column=34+n)
                        n=n+1
                    i=i+1
                #print(res)
                #print(dict)
                #print(dict[int(bus_select)])


                
                Label(root,text=" ").grid(row=4,column=0)
                Label(root,text="Select Bus",font="Arial 13 bold",fg="dark green").grid(row=5,column=33)
                Label(root,text="Operator",font="Arial 13 bold",fg="dark green").grid(row=5,column=34)
                Label(root,text="Bus Type",font="Arial 13 bold",fg="dark green").grid(row=5,column=35)
                Label(root,text="Available Seats",font="Arial 13 bold",fg="dark green").grid(row=5,column=36)
                Label(root,text="Total Seats",font="Arial 13 bold",fg="dark green").grid(row=5,column=37)
                Label(root,text="Fare",font="Arial 13 bold",fg="dark green").grid(row=5,column=38)
                Label(root,text="Bus ID",font="Arial 13 bold",fg="dark green").grid(row=5,column=39)
                Button(root,text="Proceed To Book",font="Arial 13 bold",bg="light green",fg="black",border=10,command=proceed_to_book).grid(row=6,column=40)

                ''''
                Bus1=Radiobutton(root,text="BUS1",variable=bus_select,value=1,font="Arial 10 bold")
                Bus1.grid(row=7,column=33)
                Bus2=Radiobutton(root,text="BUS2",variable=bus_select,value=2,font="Arial 10 bold")
                Bus2.grid(row=8,column=33)
                Bus3=Radiobutton(root,text="BUS3",variable=bus_select,value=3,font="Arial 10 bold")
                Bus3.grid(row=9,column=33)
                Bus4=Radiobutton(root,text="BUS4",variable=bus_select,value=4,font="Arial 10 bold")
                Bus4.grid(row=10,column=33)
        '''

                


        def proceed_to_book():
            if bus_select.get()==0:
                showerror('Select','Please Select Bus')
            else:
                #print(bus_select.get())
                k=bus_select.get()
                #print(dict[k])
                pass_details=dict[k]
                #print(ans[0],ans[3])
                Label(root,text="Fill Passenger Details To Book The Bus Ticket",font="Arial 20 bold",bg="light blue",fg="red").grid(row=13,column=0,columnspan=81,pady=30)

                Label(root,text="Name",font="Arial 15 bold").grid(row=14,column=33)
                name=Entry(root,font="Arial 10 bold")
                name.grid(row=14,column=34)

                Label(root,text="Gender",font="Arial 10 bold").grid(row=14,column=35)
                gender=StringVar()
                gender.set("Gender")
                opt=("Male","Female","Third")
                d_menu=OptionMenu(root,gender,*opt).grid(row=14,column=36)

                Label(root,text="No. Of Seats",font="Arial 15 bold").grid(row=14,column=37)
                seat=Entry(root,font="Arial 10 bold")
                seat.grid(row=14,column=38)

                Label(root,text="Mobile No.",font="Arial 15 bold").grid(row=14,column=39)
                mobile=Entry(root,font="Arial 10 bold")
                mobile.grid(row=14,column=40)

                Label(root,text="Age",font="Arial 15 bold").grid(row=14,column=41)
                age=Entry(root,font="Arial 10 bold")
                age.grid(row=14,column=42)
                def book_seat():
                    if(len(name.get())==0 or len(seat.get())==0 or len(age.get())==0 or len(mobile.get())==0):
                        showerror("Missing","Enter all the fields")
                    elif(name.get().isnumeric()):
                        showerror("Missing","Enter Name correctly!")
                    elif(seat.get().isalpha()):
                        showerror("Error","Enter the seat in numeric")
                    elif(len(mobile.get())!=10) or mobile.get().isalpha():
                        showerror("Error","Enter 10 digit Mobile no.")
                    elif(age.get().isalpha() or int(age.get())<=11 or int(age.get())>100 ):
                        showerror("Missing","Enter age correctly!")
                    else:
                        s=int(seat.get())
                        f=int(pass_details[4])
                        v=s*f
                        if(askyesno('Confirm','Do you want to proceed ? Total fare is Rs.'+str(v))):
                            m=int(pass_details[2])
                            n=int(seat.get())
                            if(m-n>=0):
                                query1='update runs set seat_avaiable=(?) where bus_id=? and date=?'
                                value1=((m-n),pass_details[5],JDate.get())
                                cur.execute(query1,value1)
                                con.commit()
                                d1=str(date.today())
                                value=(name.get(),gender.get(),seat.get(),mobile.get(),age.get(),pass_details[0],To.get(),From.get(),JDate.get(),pass_details[4],d1)
                                query='insert into Booking_history(passenger_name,Gender,No_of_seats,mobile,age,bus_select,t_o,fr,date,fare,current_date)values(?,?,?,?,?,?,?,?,?,?,?)'
                                cur.execute(query,value)
                                con.commit()
                                #value1=(mobile.get())
                                #query1='select * from Booking_history where mobile =?'
                        
                                #cur.execute(query1,value1)
                                #res=cur.fetchall()
                        
                                #Label(root,text=res,font="Arial 8 bold").grid(row=15,column=37) 
                                showinfo("Success","Booked Successfully")
                                s=int(seat.get())
                                f=int(pass_details[4])
                                v=s*f
                                showinfo('Fare','Fare is Rs.'+str(v))
                                if(askyesnocancel('Ticket','Want to get the TICKET')):
                                    root.destroy()
                                    self.Page4_Check_Your_Booking()
                                else:
                                    root.destroy()
                                    self.Page2_Home_Page()
                            else:
                                showerror('Error','Seats not available')
                            
                        
                
                    

                Button(root,text="Book Seat",font="Arial 13 bold",bg="light green",fg="black",command=book_seat,border=10).grid(row=14,column=43)
            


            
        Button(root,text="Show Bus",font="Arial 15 bold",bg="light green",fg="black",command=show_bus,border=10).grid(row=3,column=39)

        def Page2_Home_Page():
            root.destroy()
            self.Page2_Home_Page()
        Button(root,image=img_home,command=Page2_Home_Page,border=10).grid(row=3,column=40)
                                                                                        

        root.mainloop()
        


#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
    def Page2_Home_Page(self):
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
        root=Tk()

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        #root.geometry('%dx%d+0+0'%(w,h))
        root.state("zoomed")

        root.configure(background='LightYellow2')

        root.title("Home Page")

        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        Label(root,image=img_Bus).grid(row=0,column=0,padx=w//3+155,columnspan=5)

        Label(root,text="Online Bus Booking System",font="Arial 35 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=5,pady=30)

        def Page3_Enter_Journey_Details_Show_Bus_popup():
            if(askyesnocancel('?','Continue to book ticket ?')):
                root.destroy()
                self.Page3_Enter_Journey_Details_Show_Bus_popup()
             
        Button(root,text="Seat Booking",font="Arial 19 bold",bg="light green",fg="black",border=10,command=Page3_Enter_Journey_Details_Show_Bus_popup).grid(row=2,column=1,pady=30)

        def Page4_Check_Your_Booking():
            if(askyesnocancel('?','Continue to Check ticket ?')):
                 root.destroy()
                 self.Page4_Check_Your_Booking()
             
        Button(root,text="Check Booked Seat",font="Arial 19 bold",bg="green",fg="black",border=10,command=Page4_Check_Your_Booking).grid(row=2,column=2)

        def Page5_Add_New_Details_To_Database():
            if(askyesnocancel('?','Continue to Admin Page ?')):
                 root.destroy()
                 self.admin_page()
             
        Button(root,text="Add Bus Details",font="Arial 19 bold",bg="dark green",fg="black",border=10,command=Page5_Add_New_Details_To_Database).grid(row=2,column=3)

        Label(root,text="For Admin Only",font="Arial 15 bold",fg="Red").grid(row=3,column=3)

        root.mainloop()

        
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
    def Page1_Introduction_Page(self):
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
        root=Tk()

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        #root.geometry('%dx%d+0+0'%(w,h))
        root.state("zoomed")

        root.title("Introduction Page")

        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        Label(root,image=img_Bus).grid(row=0,column=0,padx=w//3+155)

        Label(root,text="Online Bus Booking System",font="Arial 35 bold",bg="light blue",fg="red").grid(row=1,pady=30)

        Label(root,text="Name : DEVENDRA YADAV",font="Arial 20 bold",fg="blue").grid(row=2,pady=10)

        Label(root,text="Er : 211B107",font="Arial 20 bold",fg="blue").grid(row=3,pady=10)

        Label(root,text="Mobile : 8299115905",font="Arial 20 bold" ,fg="blue").grid(row=4,pady=10)

        Label(root,text="Submitted To : Dr. Mahesh Kumar",font="Arial 25 bold",bg="light blue",fg="red").grid(row=5,pady=30)

        Label(root,text="Project Based Learning",font="Arial 15 bold" ,fg="red").grid(row=6)

        def Page2_Home_Page(e=0):
            root.destroy()
            self.Page2_Home_Page()
        root.bind('<KeyPress>',Page2_Home_Page)

        root.mainloop()
        
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------   
t=Test()
t.Page1_Introduction_Page()


    
