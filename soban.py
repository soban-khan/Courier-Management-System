from Tkinter import *
from tkMessageBox import *
import sqlite3

x=1
def park1():
    def displaypark():
        mobile1=mobile.get()
        conn=sqlite3.connect("c2.db")
        c3=conn.cursor()
        i=1
        for row in c3.execute("SELECT * FROM C5"):
            if(row[2]==mobile1):
                showinfo("Found","Dispatched")
                i=1
            else:
                i=i+1
        if i!=1:
            showinfo("Not Found","No record Found")
           
     
        
    window5=Toplevel(top)
    mobile=StringVar(None)
    reg01label=Label(window5,text="Mobile Number:").grid(row=0,column=0)
   
    emailentry=Entry(window5,textvariable=mobile,bd=5).grid(row=0,column=1)
    consignment=StringVar(None)
    reg01label1=Label(window5,text="Email:").grid(row=1,column=0)
   
    consignmententry=Entry(window5,textvariable=consignment,bd=5).grid(row=1,column=1)
    subpak=Button(window5,text="Track",relief=RAISED,width=15 ,height=1,activeforeground='blue',font='optima 10 bold',bg="green",bd=4,command=(displaypark)).grid(row=3,column=1)

def done():
    showinfo("Register","registerd")
           

def newuser():
    def newuser1():
        def pass1(a,b,c,d,e):
            print type(a),type(b),type(c),type(d),type(e)
            list1=[a,b,c,d,e]
            print list1
            conn=sqlite3.connect("c2.db")
            c=conn.cursor()
            
            c.execute("INSERT INTO C5 VALUES(?, ?, ?, ?,?)",list1)
            conn.commit()
           
            def alert():
                 showinfo( "Submission", "Succefully submitted")
            alert()
            window2.destroy()
            
        naam=abc.get()
        add=b.get()
        mobileno=m.get()
        emailid=e.get()
        passw=p.get()
        pass1(naam,add,mobileno,emailid,passw)
    window2=Toplevel(top)
    window2.title("New User")
    Name=Label(window2,text="Name").grid(row=0,column=0)
    abc=StringVar(None)
    
    en1=Entry(window2,textvariable=abc,bd=5).grid(row=0,column=1)
    reg=Label(window2,text="Address").grid(row=1,column=0)
    b=StringVar(None)
   
    en2=Entry(window2,textvariable=b,bd=5).grid(row=1,column=1)
    


    m=StringVar(None)

   
    mob=Label(window2,text="Mobile Number").grid(row=6,column=0)
    en3=Entry(window2,textvariable=m,bd=5).grid(row=6,column=1)
    email=Label(window2,text="Email Id").grid(row=7,column=0)
    e=StringVar(None)
  
    e4=Entry(window2,textvariable=e,bd=5).grid(row=7,column=1)

    
    password=Label(window2,text="Password").grid(row=8,column=0)
    p=StringVar(None)
  
    e5=Entry(window2,textvariable=p,bd=5).grid(row=8,column=1)
    submit=Button(window2,text="SUBMIT",relief=RAISED,width=15 ,height=1,activeforeground='blue',font='optima 10 bold',bg="green",bd=4,command=newuser1).grid(row=10,column=1)

def cancelorder():
    def cancel():
        username1=custname.get()
        password1=custemail.get()
        def connect(username1,password1):
            conn=sqlite3.connect("c2.db")
            c=conn.cursor()
            i=1
            for row in c.execute(" SELECT NAME,PASSWORD FROM C5"):
                if(username1==row[0] and password1==row[1]):
                    showinfo("Found","logged-in")
                    global x
                    x=0
                    i=1
                
                else:
                    i=i+1
                    continue
                
            if(i!=1):
                showinfo("Incorrect","wrong username/password")
            conn.close()     
        connect(username1,password1)
        
        
        window1.destroy()
        if(x==0):
            window12=Toplevel(top)
            conn = sqlite3.connect('c2.db')
            cursor = conn.execute("SELECT NAME,ADDRESS,MOBILE,EMAIL FROM C5")
            j=1
            pak1=Label(window12,text="Name",relief=RAISED,font='optima 10 bold',activeforeground='red', bg="#C0FFFF",height=2,width=15).grid(row=0,column=0)
            pak2=Label(window12,text="Address",relief=RAISED,font='optima 10 bold',activeforeground='red', bg="#C0FFFF",height=2,width=15).grid(row=0,column=1)
            pak3=Label(window12,text="Mobile",relief=RAISED,font='optima 10 bold',activeforeground='red', bg="#C0FFFF",height=2,width=15).grid(row=0,column=2)
            pak4=Label(window12,text="Email",relief=RAISED,font='optima 10 bold',activeforeground='red', bg="#C0FFFF",height=2,width=15).grid(row=0,column=3)
            
            for row in cursor:
                pak1=Label(window12,text=row[0],font='optima 15',activeforeground='red').grid(row=j,column=0)
                pak2=Label(window12,text=row[1],font='optima 15',activeforeground='red').grid(row=j,column=1)
                pak3=Label(window12,text=row[2],font='optima 15',activeforeground='red').grid(row=j,column=2)
                pak4=Label(window12,text=row[3],font='optima 15',activeforeground='red',).grid(row=j,column=3)
               
                j=j+1
                
            conn.close()
    window1=Toplevel(top)
        
   
    L1=Label(window1,text="Username").grid(row=0,column=0)
    custname=StringVar(None)
    E1=Entry(window1,textvariable=custname,bd=5).grid(row=0,column=1)
    L2=Label(window1,text="Password:").grid(row=1,column=0)
    custemail=StringVar(None)
    E2=Entry(window1,textvariable=custemail,bd=5)
    E2.grid(row=1,column=1)
    s=Button(window1,text="Login Now",relief=RAISED,width=15 ,height=1,activeforeground='blue',font='optima 10 bold',bg="green",bd=4,command=cancel)
    s.grid(row=2,column=1)
    s=Button(window1,text="New User",relief=RAISED,width=15 ,height=1,activeforeground='blue',font='optima 10 bold',bg="green",bd=4,command=newuser)
    s.grid(row=2,column=4)
def client():

    win=Toplevel(top)
    c=Canvas(win,height=250,width=250,bg="green")
    new=Button(win,text="New User",relief=RAISED,width=40 ,height=5 ,activeforeground='blue',font='optima -13 bold',bg="green",bd=4 ,command=newuser).grid(row=0,column=1)
    login=Button(win,text="Login",relief=RAISED,width=40 ,height=5 ,activeforeground='blue',font='optima 10 bold',bg="green",bd=4 ,command=cancelorder).grid(row=0,column=0)
    park=Button(win,text="Track Consignment",relief=RAISED,width=40 ,height=5 ,activeforeground='blue',font='optima 10 bold',bg="green",bd=4 ,command=park1).grid(row=0,column=2)
    filename = PhotoImage(file = "mobile.gif")
    image = c.create_image(580,520,anchor=CENTER, image=filename)
    

def reset():
    conn = sqlite3.connect('c2.db')
    cursor = conn.execute("DELETE FROM C5;")
    cursor = conn.execute("VACUUM;")
    conn.close()
    showinfo("RESET","Sucessful")
    
top=Tk()
top.geometry('1350x1350')
top.title('Client and Vendor')

c=Canvas(top,height=1000,width=450,bg="gray")
frame=Frame(c)
frame1=Frame(c)
frame1.pack(side=TOP)

loginclient=Button(frame,text="CMS",relief=RAISED,width=40 ,height=5 ,activeforeground='blue',font='optima 10 bold',bg="green",bd=4 ,command=client)
#newvedor=Button(frame,text="Register",relief=RAISED,width=40 ,height=5 ,activeforeground='blue',font='optima 10 bold',bg="Chocolate",bd=4 ,command=newuser)
reset=Button(frame,text="Reset",relief=RAISED,width=40 ,height=5 ,activeforeground='blue',font='optima 10 bold',bg="green",bd=4 ,command=reset)
loginclient.grid(row=3,column=0,padx=10,pady=5)
#newvedor.grid(row=3,column=3,padx=10,pady=10)
reset.grid(row=3,column=6,padx=10,pady=15)

frame.pack(side=BOTTOM)
filename = PhotoImage(file = "mobile.gif")
image2=c.create_image(580,520,image=filename)
c.pack(expand=YES,fill=BOTH)

top.mainloop()
